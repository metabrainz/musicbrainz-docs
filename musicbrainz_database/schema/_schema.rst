.. MusicBrainz Documentation Project

Database Schema
===============

.. https://wiki.musicbrainz.org/MusicBrainz_Database/Schema

This section is intended for developers querying the MusicBrainz database directly through PostgreSQL.

.. |clear_float|  raw:: html

   <div style="clear: both;"></div>

.. |image_network_overview| image:: /images/entity_network_overview.svg
   :alt: Overview of tables connecting core entities
   :width: 400
   :height: 300

.. |image_network_details| image:: /images/entity_network_details.svg
   :alt: Tables specifically related to core entities
   :width: 240
   :height: 300

.. |image_network_all| image:: /images/soup.svg
   :alt: All tables (exhaustive but indigestible)
   :width: 37
   :height: 300

.. .. |image_area| image:: /images/area_entity_details.svg
..    :alt: Tables for the "area" core entity type properties
..    :width: 10%

.. |image_relationship_overview| image:: /images/relationship_overview.svg
   :alt: Tables for relationship connections
   :width: 250
   :height: 300

.. |image_relationship_details| image:: /images/relationship_details.svg
   :alt: Tables for relationship properties
   :width: 350
   :height: 300


Overview
--------

The SQL scripts that create the schema can be found in our `source code repository <https://github.com/metabrainz/musicbrainz-server/tree/master/admin/sql>`_.

The database is structured around primary entities which can be edited, searched for, referred to by MBID, and linked to each other through relationships or foreign key constraints in some case. Secondary entities cannot be linked through relationships, instead they are directly linked through foreign key constraints only. Each primary entity type has a main table sometimes accompanied by complementary tables of which a few are unique but most are common.

- The first diagram below shows the main tables for primary entity types and unique tables connecting these tables, that is, beyond relationships. The main tables are highlighted. All tables are shortened to focus on foreign key constraints.

- The second diagram additionally shows the main tables for primary entity types and tables unique to some of these, that is, beyond aliases, annotations, edits, redirects, relationships, ratings, tags.

- The third diagram shows all the tables but is too dense to just distinguish foreign key constraints for example, thus the many following sections.

|image_network_overview| |image_network_details| |image_network_all|


Primary entities
----------------

Each primary entity has a main table with the same name as the entity, containing its basic data.

:doc:`Area </terminology/entities/area>`
   .. image:: /images/area_entity_details.svg
      :alt: Tables for the "area" core entity type properties
      :width: 10%
      :align: right

   A country, region, city or the like.

   Areas that can be used for filling in the *Release country* field of releases are listed, by ID, in the ``country_area`` table.

   The table ``area_containment`` is `materialized (m) <https://github.com/metabrainz/musicbrainz-server/blob/88e3d5ce55179aa23e9deccf171e4e1a77efe46e/INSTALL.md#build-materialized-tables>`_.

|clear_float|


:doc:`Artist </terminology/entities/artist>`
   .. image:: /images/artist_entity_details.svg
      :alt: Tables for the "artist" core entity type properties
      :width: 10%
      :align: right

   An artist is generally a musician, a group of musicians, or another music professional (composer, engineer, illustrator, producer, etc.)

   The tables ``artist_release`` and ``artist_release_group`` are `materialized (m) <https://github.com/metabrainz/musicbrainz-server/blob/88e3d5ce55179aa23e9deccf171e4e1a77efe46e/INSTALL.md#build-materialized-tables>`_.

|clear_float|


:doc:`Event </terminology/entities/event>`
   .. image:: /images/event_entity_details.svg
      :alt: Tables for the "event" core entity type properties
      :width: 10%
      :align: right

   An event refers to an organised event which people can attend, and is relevant to MusicBrainz. Generally this means live performances, like concerts and festivals.

|clear_float|


:doc:`Genre </terminology/entities/genre>`
   .. image:: /images/genre_entity_details.svg
      :alt: Tables for the "genre" core entity type properties
      :width: 10%
      :align: right

   A genre is a descriptor for the style and conventions followed by a piece of music.

|clear_float|


:doc:`Instrument </terminology/entities/instrument>`
   .. image:: /images/instrument_entity_details.svg
      :alt: Tables for the "instrument" core entity type properties
      :width: 10%
      :align: right

   Instruments are devices created or adapted to make musical sounds. We also list common instrument groupings (such as string quartet) as instruments.

|clear_float|


:doc:`Label </terminology/entities/label>`
   .. image:: /images/label_entity_details.svg
      :alt: Tables for the "label" core entity type properties
      :width: 10%
      :align: right

   Labels represent mostly (but not only) imprints.

|clear_float|


:doc:`Place </terminology/entities/place>`
   .. image:: /images/place_entity_details.svg
      :alt: Tables for the "place" core entity type properties
      :width: 10%
      :align: right

   A venue, studio or other place where music is performed, recorded, engineered, etc.

|clear_float|


:doc:`Recording </terminology/entities/recording>`
   .. image:: /images/recording_entity_details.svg
      :alt: Tables for the "recording" core entity type properties
      :width: 10%
      :align: right

   Represents a unique mix or edit. Has title, artist credit, duration, list of :doc:`ISRCs </terminology/terms/isrc>`. Examples (all are different Recordings):

   - Album version of the track "*Into the Blue*" by "*Moby*"
   - Remix "*Into the Blue (Buzz Boys Main Room Mayhem mix)*" by "*Moby*"
   - Remix "*Into the Blue (Underground mix)*" by "*Moby*"

   The table ``recording_first_release_date`` is `materialized (m) <https://github.com/metabrainz/musicbrainz-server/blob/88e3d5ce55179aa23e9deccf171e4e1a77efe46e/INSTALL.md#build-materialized-tables>`_.

|clear_float|


:doc:`Release </terminology/entities/release>`
   .. image:: /images/release_entity_details.svg
      :alt: Tables for the "release" core entity type properties
      :width: 10%
      :align: right

   Real-world release object you can buy in your music store. It has release date and country, list of catalog number and label pairs, :doc:`packaging type </terminology/terms/packaging_type>` and release status. Example:

   - 1984 US release of "The Wall" by "`Pink Floyd <https://musicbrainz.org/artist/83d91898-7763-47d7-b03b-b92132375c47>`_", release on label "Columbia Records" with catalog number "C2K 36183" and UPC "074643618328", it's an official release and comes with two CDs in jewel case.

   The tables ``artist_release`` and ``release_first_release_date`` are `materialized (m) <https://github.com/metabrainz/musicbrainz-server/blob/88e3d5ce55179aa23e9deccf171e4e1a77efe46e/INSTALL.md#build-materialized-tables>`_.

|clear_float|


:doc:`Release group </terminology/entities/release_group>`
   .. image:: /images/release_group_entity_details.svg
      :alt: Tables for the "release group" core entity type properties
      :width: 10%
      :align: right

   Represents an abstract "album" (or "single", or "EP") entity. Technically it's a group of releases, with a specified type. Examples:

   - Single "Under Pressure" by "`Queen <https://musicbrainz.org/artist/0383dadf-2a4e-4d10-a46a-e9e041da8eb3>`_ & `David Bowie <https://musicbrainz.org/artist/5441c29d-3602-4898-b1a1-b77fa23b8e50>`_"

   - Album "The Wall" by "`Pink Floyd <https://musicbrainz.org/artist/83d91898-7763-47d7-b03b-b92132375c47>`_"

   The table artist_release_group is `materialized (m) <https://github.com/metabrainz/musicbrainz-server/blob/88e3d5ce55179aa23e9deccf171e4e1a77efe46e/INSTALL.md#build-materialized-tables>`_.

|clear_float|


:doc:`Series </terminology/entities/series>`
   .. image:: /images/series_entity_details.svg
      :alt: Tables for the "series" core entity type properties
      :width: 10%
      :align: right

   A series is a sequence of separate release groups, releases, recordings, works or events with a common theme. The theme is usually prominent in the branding of the entities in the series and the individual entities will often have been given a number indicating the position in the series.

|clear_float|


:doc:`URL </terminology/entities/url>`
   .. image:: /images/url_entity_details.svg
      :alt: Tables for the "url" core entity type properties
      :width: 10%
      :align: right

   This entity represents a URL pointing to a resource external to MusicBrainz, i.e. an official homepage, a site where music can be acquired, an entry in another database, etc.

|clear_float|


:doc:`Work </terminology/entities/work>`
   .. image:: /images/work_entity_details.svg
      :alt: Tables for the "work" core entity type properties
      :width: 10%
      :align: right

   One layer above recordings ("song", "composition", etc.). While a *recording* represents audio data, a *work* represents the composition behind the *recording*. Relationships are used to link *recordings* and *works*. For example:

   - Song "*Into the Blue*" by "*Moby*" - all the recordings listed above will be linked to this object

|clear_float|


Secondary entities
------------------

Each secondary entity has a main table with the same name as the entity, containing its basic data.

:doc:`Artist credit </terminology/entities/artist_credit>`
   List of artists, variations of artist names and pieces of text to join the artist names. Examples:

   - "`Queen <https://musicbrainz.org/artist/0383dadf-2a4e-4d10-a46a-e9e041da8eb3>`_ & `David Bowie <https://musicbrainz.org/artist/5441c29d-3602-4898-b1a1-b77fa23b8e50>`_" - two artists ("Queen" and "David Bowie"), no name variations, joined with " & "

   - "`Jean-Michel Jarre <https://musicbrainz.org/artist/86e2e2ad-6d1b-44fd-9463-b6683718a1cc>`_" - one artist ("Jean Michel Jarre"), name variation "Jean-Michel Jarre"

   - "`Tracy W. Bush <https://musicbrainz.org/artist/4d78d8f5-f2e4-4eaa-86b2-952307aabd9f>`_, `Derek Duke <https://musicbrainz.org/artist/ef8d7a94-64a3-4362-b81f-b5999fb246de>`_, `Jason Hayes <https://musicbrainz.org/artist/7fd43bc8-b5ff-45ed-8ce5-1b0c17114a9e>`_ and `Glenn Stafford <Glenn Stafford>`_" - four artists, no name variations, joined with commas and an "and".

:doc:`Medium </terminology/entities/medium>`
   This entity represents a piece of media, included in a release. It contains information about the format of the media, its position in the release, an optional title, and most importantly, a list of tracks. CD TOCs are attached to mediums, not releases or release_groups.

   Examples:

   - CD1 of the 1984 US release of "The Wall" by "Pink Floyd"
   - CD2 of the 2005 UK release of "Aerial" by "Kate Bush", named "A Sky of Honey"

:doc:`Track </terminology/entities/track>`
   This entity is not visible to users on its own, only in the context of a release. It has an MBID, and contains a link to a recording, a title, artist credit and position on its associated medium.


Entity complementary data
-------------------------

**Aliases**
   All the primary entities except URL (i.e. area, artist, event, genre, instrument, label, place, recording, release, release group, series and work) have ``*_alias`` tables, all of which have the same structure. They contain alternate names for instances of those entities.

**Annotations**
   All the primary entities except URL (i.e. area, artist, event, genre, instrument, label, place, recording, release, release group, series and work) have a corresponding ``*_annotation`` table that links entities of that type to entries in the main ``annotation`` table which contains the actual text of the annotation, along with the changelog and the identity of the editor who created it.

**Edits**
   Edits to the database are stored in ``edit`` table, with the edit notes/comments stored in ``edit_note``. The 13 other ``edit_*`` tables are used to link edits to the entity they modify; there is one such table for each primary entity type. They all have the same structure: just two foreign keys, one to the entity table and the other to ``edit`` table.

**IPIs and ISNIs**
   The primary entities artist and label can have multiple :doc:`IPI </terminology/terms/ipi>` and :doc:`ISNI </terminology/terms/isni>` codes attached to them. These tables ``*_ipi`` and ``*_isni`` are used to store those mappings. They contain a foreign key pointing to the entity, the actual value of the code, and ``edits_pending`` and *created* fields with the usual meaning.

**MBID redirects**
   There are 15 ``*_gid_redirect`` tables, one for each of the 13 primary entity types, plus ones for *track* and *artist_credit*. They are used to redirect one MBID to another when entities are merged.

**Ratings**
   There is one ``*_rating_raw`` table for each of the primary entities that can be rated: artist, event, label, place, recording, release group and work. The ``*_rating_raw`` tables all have the same structure, consisting of the actual rating, expressed as an integer between 0 and 100, and two foreign keys, one linked to the associated entity, and the other linked to the ``editor`` table, to specifying who made the rating. For privacy reasons, the ``*_rating_raw`` tables aren't included in the database dumps.

   The aggregate rating of each entity is stored in the corresponding ``_meta`` table, in the **rating** field. There is also a **rating_count** field that specifies how many ratings have been entered for the entity.

   The ``release_group_meta`` table also contains other fields, and the *release* entity, even though it cannot be rated, still has a ``release_meta`` table, which is used to store other data.

**Tags**
   All primary entities but the genre and URL (i.e. area, artist, event, instrument, label, place, recording, release, release group, series and work) have ``*_tag`` and ``*_tag_raw`` tables, with the same structure. These tables contain two foreign keys, linked to the associated entity and to the ``tag`` table. The ``*_tag_raw`` tables contain a foreign key, **editor**, which specifies who added the tag, while the ``*_tag`` tables instead contain a **count** of how many times a tag is applied to a particular entity, and a **last_updated** timestamp. For privacy reasons, the ``*_tag_raw`` tables aren't included in the database dumps.

   The ``tag`` table contains the actual names of the tags, and a *ref_count* indicating how often the tag has been used.

**Types**
   ``*_type`` tables are simply mappings between strings and ID numbers, representing various sets of types. Areas, artists, events, instruments, labels, places, series and works are the only primary entities with each have a ``*_type`` and an ``*_alias_type`` table. Release groups have ``release_group_primary_type`` and ``release_group_secondary_type`` tables. Genres, recordings and releases only have ``*_alias_type`` tables, and URLs do not have ``*_type`` tables at all.

Relationship table structure
----------------------------

The first below diagram shows minimal foreign keys needed to define a relationship between two entities. :doc:`Artist-Work </relationships/artist-work/artist-work>` is just an example of a relationship type. The main table is highlighted. All other tables are shortened to focus on foreign key constraints. The second diagram complementarily shows tables for the detailed representation of a link. The main tables are highlighted.

|image_relationship_overview| |image_relationship_details|


**l_* tables**
   There are tables for every possible combination of the primary entities (*area*, *artist*, *event*, *instrument*, *genre*, *label*, *place*, *recording*, *release*, *release_group*, *series*, *url* and *work*) all prefixed with *l_* and all with the same format. Two of them are shown in the diagram. They contain a field, **edits_pending** that is a count of pending changes to the Advanced Relationship (AR), a **last_updated** field, and three foreign keys: **link** that points back to the associated entry in the *link* table, and **entity0** and **entity1** that point to the associated entry in the corresponding entity table (i.e. **artist**, **recording**, **url**, etc.).

There are two tables that help to avoid unnecessary duplication:

**link & link_attribute tables**
   The *link* table contains the begin and end date info, and the **link_type** foreign key field that specifies what kind of AR it is. It also has a count of how many other attributes that particular link has in the **attribute_count** field, and a **created** field that specifies when it was created.

   Each AR attribute either applies to a particular AR or it doesn't. The *link_attribute* table stores this information, having a record for each **attribute_type** (a foreign key field for *link_attribute_type*) of each **link**.

**link_type, link_attribute_type, & link_type_attribute_type tables**
   The AR types and attributes are defined in these three tables, shown at the top of the diagram. They can only be modified by the AR editors.

   The *link_type* table defines the types of ARs available. AR types are arranged in a number of trees, for ease of finding. This tree structure is expressed with the **parent** and **child_order** fields; **parent** is the **id** of the parent AR type, or null if it's at the root, and **child_order** orders the children of a given parent AR type. Each AR type has a unique uuid, stored in the *gid* field, for use in permalinks and external applications. The link between a particular AR type and the corresponding *l_* table is formed by the **entity_type0** and **entity_type1 fields**.

   The attributes are themselves defined in the *link_attribute_type* table. Like AR types, attributes form a number of trees (the vast majority of them are individual musical instruments). Besides the **parent** and **child_order** fields shared with the *link_type* table, the *link_attribute_table* also has a **root** field, showing the root of the tree that the attribute is part of. Attributes also have **names** and **descriptions** which appear in various places where they are displayed, as well as **gids** and a **last_updated timestamp**.

   The *link_type_attribute_type* table specifies what attributes can be applied to particular types of ARs; it has the necessary foreign key fields (**link_type** and **attribute_type**) and it also specifies how many instances of the attribute (or one of its children) can be added to the particular AR type in the **min** and **max** fields. Currently, most of them allow the attributes to merely be present or absent, while a few allow any number of copies of the attribute, or none. The "creative commons licensed download" attribute has to be included exactly once, while the *instrument* attribute (of the *instrument* type AR), requires at least one instance.


Cover Art Archive table structure
---------------------------------

.. image:: /images/cover_art_details.svg
   :alt: Tables for cover art
   :width: 20%
   :align: right

The :doc:`Cover Art Archive </terminology/terms/cover_art_archive>` table structure is fairly simple. The *cover_art* table stores the actual cover art and associations to edits. *art_type* stores the acceptable cover art types, and *cover_art_type* links the two together. *release_group_cover_art* links a release group to the release whose cover art should represent the release group.

This image also shows the links to tables in the main diagram (as well as the *edit* table), but not their full schemas; please see other diagrams or the real schema specification for details.

There is one view not shown, which is the *index_listing* view - this makes for a slightly nicer interface than joining the tables manually, by providing an array of cover art types and easy pointers for **is_front** and **is_back**. Otherwise it largely resembles the *cover_art* table.

|clear_float|


CDStubs table structure
-----------------------

.. image:: /images/cdstub_details.svg
   :alt: Tables for CD stub
   :width: 20%
   :align: right

The :doc:`CDStubs </terminology/entities/cd_stub>` table structure consists of only 3 tables: cdtoc_raw, release_raw and track_raw.

The *release_raw* table contains basic metadata about the stub release, such as the artist and title.

The individual tracks of each stub release are in the *track_raw* table, which holds the track title and its track number (in the sequence column). A track's artist can be different than the artist of the release, so there's an artist column which can optionally contain the name of the track's artist.

Each CDStub needs an associated :doc:`Disc ID </terminology/terms/disc_id>`, which is stored in the *cdtoc_raw* table, together with the track count of the disc, as well as the leadout and track offset (:doc:`Disc ID Calculation </how-tos/calculate_disc_id>` contains more information about the latter two).

|clear_float|


Frequent use cases
------------------

.. image:: /images/for_tagging_audio_files.svg
   :alt: Tables for tagging audio files
   :width: 20%
   :align: right

Tagging audio files
   When roughly tagging audio files with basic metadata, you will mainly be looking for:

   - Primary entity types: artist, recording, release, release group
   - Secondary entity types: artist credit, medium, track

|clear_float|


.. image:: /images/for_finding_song_authors.svg
   :alt: Tables for finding song authors
   :width: 20%
   :align: right

Finding song authors
   When retrieving the authors (composer, lyricist…) of a recorded song, you will mainly be looking for:

   - Primary entity types: artist, recording, work
   - Secondary entity types: artist credit
   - Relationship types: artist-work, recording-work

|clear_float|


Undocumented tables
-------------------

The following tables have not yet been documented in this page. Help is gratefully appreciated!

.. code::

   CREATE TABLE artist_credit_name

   CREATE TABLE cdtoc

   CREATE TABLE gender

   CREATE TABLE iso_3166_1
   CREATE TABLE iso_3166_2
   CREATE TABLE iso_3166_3

   CREATE TABLE isrc
   CREATE TABLE iswc

   CREATE TABLE language

   CREATE TABLE link_creditable_attribute_type
   CREATE TABLE link_attribute_credit

   CREATE TABLE medium_cdtoc
   CREATE TABLE medium_format

   CREATE TABLE medium_index

   CREATE TABLE release_country
   CREATE TABLE release_unknown_country
   CREATE TABLE release_coverart
   CREATE TABLE release_label
   CREATE TABLE release_packaging
   CREATE TABLE release_status

   CREATE TABLE release_group_secondary_type_join

   CREATE TABLE replication_control

   CREATE TABLE script
   CREATE TABLE script_language

   CREATE TABLE tag_relation

   CREATE TABLE work_attribute_type
   CREATE TABLE work_attribute_type_allowed_value
   CREATE TABLE work_attribute

The following tables are not publicly available for download thus are not relevant in this page.

.. code::

   CREATE TABLE application

   CREATE TABLE autoeditor_election
   CREATE TABLE autoeditor_election_vote

   CREATE TABLE edit_note_change

   CREATE TABLE editor
   CREATE TABLE editor_collection
   CREATE TABLE editor_collection_release
   CREATE TABLE editor_language
   CREATE TABLE editor_oauth_token
   CREATE TABLE editor_preference
   CREATE TABLE editor_subscribe_artist
   CREATE TABLE editor_subscribe_artist_deleted
   CREATE TABLE editor_subscribe_collection
   CREATE TABLE editor_subscribe_label
   CREATE TABLE editor_subscribe_label_deleted
   CREATE TABLE editor_subscribe_editor
   CREATE TABLE editor_subscribe_series
   CREATE TABLE editor_subscribe_series_deleted

   CREATE TABLE unreferenced_row_log

   CREATE TABLE vote
