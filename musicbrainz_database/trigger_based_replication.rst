.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Trigger_Based_Replication

.. FIXME

Trigger Based Replication
=========================

This approach is based on the following idea:

   - Each table to be replicated gets three trigger functions added:

      - One trigger for added rows
      - One trigger for removed rows
      - One trigger for changed rows

   - Each of these triggers will write rows into a replication changes table
   - A bot will fire off periodically (once an hour) and traverse the replication changes table and dump all the rows since the last bot run to a dump file.
   - This dump file will be timestamped, compressed and placed onto the FTP server.
   - An XML file that contains a list of the recent update packages will be available on the FTP server. Clients can download this file to discover what packages they will need in order to come up to speed.

Slaves that wish to keep their data up to date will follow these steps:

   - Go to the main FTP site and download the update package(s) since it last checked the FTP site.
   - For each packet, in serial number order, unpack and apply the data with the following steps:

      - For each new row, add the row.
      - For an update, replace the row with the new row from the update package
      - For a deletion, delete the row in question.

The above mentioned replication table will have the following columns:

.. table::
   :widths: auto

   ========== =========== ==================================================
   Type       Field Name  Comment
   ========== =========== ==================================================
   integer    tableid     What is the best way to enumerate this in SQL?
   integer    rowid
   timestamp  ts
   tinyint    operation   One of ADD (0), UPDATE (1), REMOVE (2)
   ========== =========== ==================================================


The dump packets will have the following format, one line per row to be replicated:

.. code::

   tableid <tab> rowid <tab> timestamp <tab> operation <tab> [optional <tab> separated row values for ADD/UPDATE ops]

.. Is the opensourcing of Postrges's replication solution relevant here? The press release can be found at http://lwn.net/Articles/46576/
