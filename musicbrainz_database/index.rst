.. MusicBrainz Documentation Project

MusicBrainz Database
====================

https://wiki.musicbrainz.org/MusicBrainz_Database


The MusicBrainz Database is built on the PostgreSQL relational database engine and contains all of MusicBrainz' music metadata. This data includes information about :doc:`artists </terminology/entities/artist>`, :doc:`release groups </terminology/entities/release_group>`, :doc:`releases </terminology/entities/release>`, :doc:`recordings </terminology/entities/recording>`, :doc:`works </terminology/entities/work>`, and :doc:`labels </terminology/entities/label>`, as well as the many :doc:`relationships </terminology/entities/relationship>` between them. The database also contains a full history of all the changes that the MusicBrainz community has made to the data.

For details on commercial use, please visit the `MetaBrainz Foundation <https://metabrainz.org/supporters/account-type>`_ site.


Data overview
-------------

Core data
+++++++++

:doc:`Areas </terminology/entities/area>`
   Name, aliases, type, ISO codes, begin and end dates, disambiguation comment, MBID

:doc:`Artists </terminology/entities/artist>`
   Name, sort name, areas, IPI, ISNI, aliases, type, begin and end dates, disambiguation comment, MBID

:doc:`Events </terminology/entities/event>`
   Name, aliases, type, begin and end dates, time, setlist, disambiguation comment, MBID (performers / location indicated through relationships)

:doc:`Genres </terminology/entities/genre>`
   Name, aliases, disambiguation comment, MBID

:doc:`Instruments </terminology/entities/instrument>`
   Name, description, aliases, type, disambiguation comment, MBID

:doc:`Labels </terminology/entities/label>`
   Name, area, IPI, ISNI, aliases, type, code, begin and end dates, disambiguation comment, MBID

:doc:`Mediums </terminology/entities/medium>`
   Format, list of tracks (title, artist credit, duration)

:doc:`Places </terminology/entities/place>`
   Name, aliases, area, type, code, begin and end dates, disambiguation comment, MBID

:doc:`Recordings </terminology/entities/recording>`
   Title, artist credit, duration, ISRC, PUIDs, disambiguation comment, MBID

:doc:`Release Groups </terminology/entities/release_group>`
   Title, artist credit, type, disambiguation comment, MBID

:doc:`Releases </terminology/entities/release>`
   Title, artist credit, type, status, language, date, country, label, catalog number, barcode, medium(s), disc ID(s), ASIN, disambiguation comment, MBID

:doc:`Series </terminology/entities/series>`
   Name, aliases, type, disambiguation comment, MBID (parts indicated through relationships)

:doc:`Works </terminology/entities/work>`
   Title, ISWC, disambiguation comment, MBID (writers indicated through relationships)

:doc:`Relationships </terminology/entities/relationship>` & :doc:`URLs </terminology/entities/url>`
   Relationships are a way to link the above entities together and allow MusicBrainz to capture most of the data contained in the liner notes of a CD.

:doc:`CD Stubs </terminology/entities/cd_stub>`
   Title, artist, barcode, disc ID, disambiguation comment

Supplementary data
++++++++++++++++++

Supplementary data includes:

- user submitted annotations, tags (including genre associations) and ratings
- derived statistics
- search indexes
- edit history
- non-personal user data

License
-------

**Core data**
   The core data, as noted above, is licensed under the `CC0 <http://creativecommons.org/publicdomain/zero/1.0/>`_, which is effectively placing the data into the Public Domain. This means that anyone can download and use the core data in any way they see fit. No restrictions, no worries!

**Supplementary data**
   The supplementary data, as noted above, is released under the Creative Commons `Attribution-NonCommercial-ShareAlike 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>`_ license. This allows for non-commercial use of the data as long as MusicBrainz is given credit and that derivative works (works based on the CC licensed data) are also made available under the same license.

Commercial Use & Live Data Feed
-------------------------------

All of our data is available for commercial licensing. For details on commercial use, please visit the `MetaBrainz Foundation <https://metabrainz.org/supporters/account-type>`_ site.

Consumers of our database may be interested in our replicated :doc:`Live Data Feed </products/live_data_feed>`. This feed operates in conjunction with the :doc:`MusicBrainz Server </musicbrainz_server/index>` software and enables a local database to automatically stay in sync with the main server. To access the Live Data Feed for commercial or personal use, please sign up at the `MetaBrainz Foundation <https://metabrainz.org/supporters/account-type>`_ site.
