.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Replication

Database Replication
====================

The MusicBrainz :doc:`Live Data Feed </products/live_data_feed>` is based on a concept of replication. You can read about how it works at :doc:`Replication Mechanics </musicbrainz_database/replication_mechanics>` and :doc:`Trigger Based Replication </musicbrainz_database/trigger_based_replication>`. The list of tables to be replicated can be found in the codebase at admin/sql/CreateReplicationTriggers.sql and other CreateReplicationTriggers.sql files in subdirectories of admin/sql/; the list as of this writing is:

Included in replication
-----------------------

**Tables in mbdump.tar.bz2**
    - artist
    - artist_alias
    - artist_alias_type
    - artist_ipi
    - artist_credit
    - artist_credit_name
    - artist_gid_redirect
    - artist_name
    - artist_type
    - cdtoc
    - clientversion
    - country
    - gender
    - isrc
    - iswc
    - l_artist_artist
    - l_artist_label
    - l_artist_recording
    - l_artist_release
    - l_artist_release_group
    - l_artist_url
    - l_artist_work
    - l_label_label
    - l_label_recording
    - l_label_release
    - l_label_release_group
    - l_label_url
    - l_label_work
    - l_recording_recording
    - l_recording_release
    - l_recording_release_group
    - l_recording_url
    - l_recording_work
    - l_release_release
    - l_release_release_group
    - l_release_url
    - l_release_work
    - l_release_group_release_group
    - l_release_group_url
    - l_release_group_work
    - l_url_url
    - l_url_work
    - l_work_work
    - label
    - label_alias
    - label_alias_type
    - label_ipi
    - label_gid_redirect
    - label_name
    - label_type
    - language
    - link
    - link_attribute
    - link_attribute_type
    - link_type
    - link_type_attribute_type
    - medium
    - medium_cdtoc
    - medium_format
    - puid
    - recording
    - recording_gid_redirect
    - recording_puid
    - release
    - release_gid_redirect
    - release_label
    - release_packaging
    - release_status
    - release_group
    - release_group_gid_redirect
    - release_group_primary_type
    - release_group_secondary_type
    - release_group_secondary_type_join
    - release_name
    - replication_control
    - script
    - script_language
    - track
    - track_name
    - tracklist
    - url
    - url_gid_redirect
    - work
    - work_alias
    - work_alias_type
    - work_gid_redirect
    - work_name
    - work_type

**Tables in mbdump-derived.tar.bz2**
    - annotation
    - artist_annotation
    - artist_meta
    - artist_tag
    - label_annotation
    - label_meta
    - label_tag
    - recording_annotation
    - recording_meta
    - recording_tag
    - release_annotation
    - release_meta
    - release_group_annotation
    - release_group_meta
    - release_group_tag
    - tag
    - tracklist_index
    - work_annotation
    - work_meta
    - work_tag

**Tables in mbdump-stats.tar.bz2**
    - statistics.statistic
    - statistics.stastitic_event
    - Tables in mbdump-cover-art-archive.tar.bz2
    - cover_art_archive.art_type
    - cover_art_archive.cover_art
    - cover_art_archive.cover_art_type
    - cover_art_archive.release_group_cover_art

Not included in replication
---------------------------

**Tables in mbdump-derived.tar.bz2**
    - release_tag (see http://tickets.musicbrainz.org/browse/MBS-5978)
    - tag_relation

**Tables in mbdump-editor.tar.bz2**
    - editor

**Tables in mbdump-edit.tar.bz2**
    - edit
    - edit_area
    - edit_artist
    - edit_label
    - edit_note
    - edit_recording
    - edit_release
    - edit_release_group
    - edit_url
    - edit_work
    - vote
    - Tables in mbdump-cdstubs.tar.bz2
    - cdtoc_raw
    - release_raw
    - track_raw
