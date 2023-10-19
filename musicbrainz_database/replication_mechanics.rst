.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Replication_Mechanics

.. FIXME

MusicBrainz Database Replication Mechanics
==========================================

In principal the broad approach that we've taken is to take the "dbmirror" PostgreSQL contributed code (which creates a log of changes to tables using triggers), but change data link between master and mirror from "direct Postgres connection" to some file-transfer system (e.g. FTP).

.. How will this work exactly?

Replication Control
-------------------

**replication_control** is a one-row table which records state information for the replication system. It's used slightly differently depending on whether we're the master or a mirror. Possibly this is a design weakness.

   - id (integer primary key) - this column is here solely because we want to replicate this table, and replicated tables need primary keys. The primary key of the one and only row should always be "1".
   - current_schema_sequence (integer not null)
   - current_replication_sequence (integer with null)


Schema Sequence Number
++++++++++++++++++++++

**current_schema_sequence** defines the sequence number of the current database schema. This value is also held in ``&DBDefs::DB_SCHEMA_SEQUENCE``.

   - When an mb_server codebase is checked out of Subversion, that codebase will always be associated with a particular schema sequence number. This number is therefore embedded into DBDefs.pm, and InsertDefaultRows.sql.
   - The main part of the server code should probably refuse to run unless current_schema_sequence == &DBDefs::DB_SCHEMA_SEQUENCE
   - All database export files (mbdump\*.tar.bz2) and replication packets (replication-\*.tar.bz2) will include a file, SCHEMA_SEQUENCE, which lists the schema sequence number used to generate that data. The file is simply an integer, followed by a newline.
   - The main data import (MBImport.pl), and the equivalent for replication data, should then refuse to process files where the SCHEMA_SEQUENCE value != current_schema_sequence.
   - After the user has progressed to the correct schema sequence number (upgrade the codebase, then upgrade the database), then the import can proceed once again.

**How the Master Advances to the Next Schema Sequence Number**

When upgrading to a new release (say from ``$OLD`` schema to ``$NEW`` schema, where ``$NEW=$OLD+1``):

   - The codebase is upgraded (setting ``&DBDefs::DB_SCHEMA_SEQUENCE`` to ``$NEW``)
   - We temporarily set ``&DBDefs::DB_SCHEMA_SEQUENCE`` back to ``$OLD``, and run ``ExportAllTables`` (with replication):
   - The replication packet (say, ``#N``) thus produced therefore has the following properties:

      - ``SCHEMA_SEQUENCE`` == ``$OLD``
      - all the changes described by the packet are to be applied to a database of the ``$OLD`` schema
      - after the packet is applied, the schema is still ``$OLD``, and replication_control.current_schema_sequence is still ``$OLD``

   - Now we reset ``&DBDefs::DB_SCHEMA_SEQUENCE`` back to ``$NEW`` again
   - Any database upgrade SQL scripts (create table, index, etc etc) are run
   - Replication triggers are added to any new tables
   - Any initial data is seeded in (and thus will become part of the next replication packet)
   - We manually update replication_control.current_schema_sequence to ``$NEW`` (again, this change will be part of the next replication packet)

At some point the master then produces its next replication packet (``#N+1``), which will have the following properties:

   - ``SCHEMA_SEQUENCE`` == ``$NEW``
   - all the changes described by the packet are to be applied to a database of the ``$NEW`` schema
   - one of the changes within the packet sets replication_control.current_schema_sequence to ``$NEW``

**How the Mirror Advances to the Next Schema Sequence Number**

When upgrading to a new release (say from ``$OLD`` schema to ``$NEW`` schema, where ``$NEW=$OLD+1``):

   - We ensure that we are up-to-date with all replication packets matching ``$OLD`` (i.e. by doing nothing until LoadReplicationChanges tells us that we must upgrade to the next schema)
   - The codebase is upgraded (setting ``&DBDefs::DB_SCHEMA_SEQUENCE`` to ``$NEW``)
   - Any database upgrade SQL scripts (create table, index, etc etc) are run
   - We manually update replication_control.current_schema_sequence to ``$NEW``

Now the database is of schema ``$NEW``, and replication_control.current_schema_sequence = ``$NEW``.

When the next replication packet is loaded:

   - SCHEMA_SEQUENCE == ``$NEW`` (which matches ``&DBDefs::DB_SCHEMA_SEQUENCE`` and replication_control.current_schema_sequence, so the packet can be loaded)
   - the packet will contain changes to add any "seed" data which was part of the release upgrade
   - the packet will contain a change to set replication_control.current_schema_sequence to ``$NEW`` (but in fact it will be ``$NEW`` already)

**Other Processing Details**

   - Master
      - ExportAllTables

         - if current_schema_sequence is missing, or != ``&DBDefs::DB_SCHEMA_SEQUENCE``, refuses to run
         - ``SCHEMA_SEQUENCE`` is written, containing current_schema_sequence

   - MBImport
      - reads ``SCHEMA_SEQUENCE``

         - if missing, warns that "Don't be surprised if this import fails"
         - if present but != ``&DBDefs::DB_SCHEMA_SEQUENCE``, refuses to run

   - Mirror
      - LoadReplicationChanges

         - refuses to run if ``&DBDefs::DB_SCHEMA_SEQUENCE`` != current_schema_sequence
         - refuses to load a packet if ``SCHEMA_SEQUENCE`` != current_schema_sequence


Replication Sequence Number
+++++++++++++++++++++++++++

**current_replication_sequence** has two slightly different meanings, depending on whether we're the master or a mirror.

   - Master
      - If NULL, then we've never started producing replication data. We've never yet produced a full export / replication packet which are "in synch".
      - Otherwise, the database currently consists of the listed replication point, plus whatever changes are in the Pending/PendingData tables (i.e. changes not yet exported to a replication packet).

   - Mirror
      - If NULL, then the database does not correspond to any replication point; you can't apply replication updates to this database when it's in this state.
      - Otherwise, the database currently exactly corresponds to the listed replication point.

**How the Replication Sequence Number Is Advanced**

   - On the master: when ExportAllTables is run *--with-replication*,

      - inside the serializable transaction, the master increases the current_replication_sequence value (say, to 123)
      - that change, like changes to other tables, is stored in the Pending/PendingData tables
      - the REPLICATION_SEQUENCE file is written (with the new value, e.g. 123)
      - all pending changes, and the REPLICATION_SEQUENCE file, are saved in the replication packet: replication-123.tar.bz2
      - thus, replication-123.tar.bz2 includes:

         - a REPLICATION_SEQUENCE number of 123
         - Pending/PendingData entries which, when applied, will change the current_replication_sequence to 123.

   - On the mirror, each time LoadReplicationChanges attempts to load the next replication packet,
      - next_replication_sequence := current_replication_sequence + 1
      - it attempts to download packet #<next_replication_sequence>
      - it verifies that REPLICATION_SEQUENCE matches <next_replication_sequence>
      - the Pending and PendingData files are loaded and processed (i.e. the changes are applied to the database)
      - it re-reads current_replication_sequence and verifies that is now == next_replication_sequence
      - it reads last_replication_date and verifies that it is == TIMESTAMP (from the packet)


Export
++++++

The same program is used both to perform a full database export and/or to produce replication packets.

All archives produced, whether a full export or a replication packet, include the replication sequence number in the file REPLICATION_SEQUENCE. If a full export is performed without a replication packet, however, then REPLICATION_SEQUENCE will be empty, indicating that this full export does not correspond to a replication point, and therefore cannot be used for replication.
