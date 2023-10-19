.. MusicBrainz Documentation Project

.. https://wiki.musicbrainz.org/MusicBrainz_Database/Download

Database Download
=================

A complete data snapshot of the entire database is generated twice a week. These snapshots are split into several different files organized by license and contents.

Introduction
------------

Please read the :doc:`MusicBrainz Database </musicbrainz_database/index>` product page and the :doc:`database schema </musicbrainz_database/schema/_schema>` documentation if you are not familiar with the MusicBrainz Database.

The data dumps are made available in a format that can be loaded into a local instance of **PostgreSQL** using a local instance of MusicBrainz Server. See :doc:`MusicBrainz Server Setup </musicbrainz_server/setup>` for information regarding how to do it. Instructions and scripts are provided to download the data.

If you are interested in keeping the data in sync with MusicBrainz using our :doc:`live data feed </products/live_data_feed>`, make sure to enable replication.

Alternatively, if you are not interested in having a local MusicBrainz website and web service, you can use `mbdata <https://github.com/lalinsky/mbdata>`_ that includes replication without the rest of MusicBrainz Server.


Download
--------

The data dumps are available for download from our `datasets download page <https://metabrainz.org/datasets/postgres-dumps#musicbrainz>`_.


File Descriptions
-----------------

Each data dump snapshot includes a number of different files. Depending on your use cases, you may or may not require all of them. Here's a rundown of what they contain:

**The Basics**
    If you're only looking for music metadata, you can start here with the basics. These files should help you get everything you need to replicate the core catalog.

    If you're looking for more advanced, or more analytical data, you should still have a look at these basics, but make sure to also see the Advanced section below.


**ASC files**
    All of the ".asc" files contain the PGP signatures for their respective files. You can use these to verify the PGP signatures of the files after you've downloaded.

    In order to verify the downloads, you must first fetch the MusicBrainz public key:

   .. code-block:: console

      $ gpg --recv-keys C777580F
      gpg: requesting key C777580F from hkp server keys.gnupg.net
      gpg: /home/kevin/.gnupg/trustdb.gpg: trustdb created
      gpg: key C777580F: public key "MusicBrainz (MusicBrainz data dump signing key) <support@musicbrainz.org>" imported
      gpg: no ultimately trusted keys found
      gpg: Total number processed: 1
      gpg:               imported: 1  (RSA: 1)`

   Now you can verify the GPG signatures. For example, if you download the SHA256SUMS files, you can run:

   .. code-block:: console

      $ gpg --verify SHA256SUMS.asc SHA256SUMS
      gpg: Signature made Sat 18 Jul 2015 03:10:45 AM UTC using RSA key ID C777580F
      gpg: Good signature from "MusicBrainz (MusicBrainz data dump signing key) <support@musicbrainz.org>"
      gpg: WARNING: This key is not certified with a trusted signature!
      gpg:          There is no indication that the signature belongs to the owner.
      Primary key fingerprint: D5E6 3B4B DCCE 1956 4294  8684 B8FC 2375 C777 580F

   .. note::

         If you don't use "gpg" very frequently, and haven't marked the key as trusted (or marked any other key as trusted), you'll see the above warning that the key is not certified. It doesn't mean that the signature is invalid, just that "gpg" won't be convinced that the source of the key you received is authentic until you tell it that you think it is.


**MD5SUM and SHA25SUM**
   These files contain the checksums for the hosted files. You can run "md5sum" and "sha256sum" on the downloaded .tar.bz2 files to validate the checksums:

   .. code-block:: console

      $ sha256sum mbdump-stats.tar.bz2
      5ad5de5c6804c6c937729382f7a0db50f46dc9ae0a4a143e7720fb1d4bbbfeba  mbdump-stats.tar.bz2

   You can also verify the checksum of all downloaded files at once.

   .. code-block:: console

      $ sha256sum -c SHA256SUMS
      mbdump-cdstubs.tar.bz2: OK
      mbdump-cover-art-archive.tar.bz2: OK
      mbdump-derived.tar.bz2: OK
      mbdump-documentation.tar.bz2: OK
      sha256sum: mbdump-edit.tar.bz2: No such file or directory
      mbdump-edit.tar.bz2: FAILED open or read
      mbdump-editor.tar.bz2: OK
      mbdump-stats.tar.bz2: OK
      mbdump-wikidocs.tar.bz2: OK
      mbdump.tar.bz2: OK
      sha256sum: WARNING: 1 listed file could not be read

   If you did not download a specific file, you can ignore the error regarding this file.


**mbdump.tar.bz2**
   This is the core MusicBrainz database, including the tables for Artist, Release, Recording, etc.

   Most normal catalog use cases only require this database, and the derived data.


**mbdump-derived.tar.bz2**
   The derived data consists of annotations, user ratings, user tags, and search indexes. Combining this with the core database should cover most music-metadata-related use cases. Keep in mind you will certainly need this if you want genre data, since the association of genres with entities is done via user tags.

   .. note::

      If you want to use this data in a standalone (rather than mirror) setup, you will also need the editor dump below, since annotation data is linked to editors through foreign keys.


**mbdump-edit.tar.bz2**
   This is the complete edit history for the core database. If you want to see how metadata has evolved, make sure to grab this dump in addition to the core.

   The history includes things like open and closed edits, edit notes, votes, and auto-editor elections. It does not include information about the people who made the edits. For that information, you'll need the next item as well.


**mbdump-editor.tar.bz2**
   This table includes non-personal user data about the people who've enacted the edits enumerated in the database above.


**mbdump-cdstubs.tar.bz2**
   The :doc:`CD Stub </terminology/entities/cd_stub>` data is described over on its dedicated page. As mentioned there, the stubs are submitted anonymously, and are treated as an untrusted source of data, separate from the core database.


**mbdump-stats.tar.bz2**
   Metadata about the metadata (very meta!). The statistics database includes things that you might find over at http://musicbrainz.org/statistics.


**mbdump-cover-art-archive.tar.bz2**
   This dump includes the tables that show connections between MusicBrainz and the :doc:`Cover Art Archive </terminology/terms/cover_art_archive>` (keep in mind it does not include the actual images in the archive).


**mbdump-event-art-archive.tar.bz2**
   This dump includes the tables that show connections between MusicBrainz and the Event Art Archive (keep in mind it does not include the actual images in the archive). Since the Event Art Archive is not yet in use, there's currently no data here.


**mbdump-documentation.tar.bz2**
   This dump includes the tables that specify which relationships in the database are used as examples for each relationship type, as well as the specific guidelines for each relationship type, when available.


**mbdump-wikidocs.tar.bz2**
   The *wikidocs_index* table, containing info about what revision is transcluded for each wiki page covered by our :doc:`WikiDocs </miscellaneous/wikidocs>` system.


Licenses
--------

**Public Domain**
   .. image:: /images/CC0_button.svg

   The following database dumps are distributed under the `CC0 <http://creativecommons.org/publicdomain/zero/1.0/>`_ license, which is effectively placing the data into the Public Domain:

   - mbdump.tar.bz2
   - mbdump-cdstubs.tar.bz2

**Creative Commons**
   .. image:: /images/CC_BY-NC-SA_icon_88x31.png

   The following database dumps are distributed under the `Attribution-NonCommercial-ShareAlike 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>`_ license:

   - mbdump-derived.tar.bz2
   - mbdump-edit.tar.bz2
   - mbdump-editor.tar.bz2
   - mbdump-stats.tar.bz2
