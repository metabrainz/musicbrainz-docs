.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Style/Unknown_and_untitled

Unknown and Untitled
====================

Status: **Official Style Guideline**

We have several guidelines which deal with those cases where something does not have a name, or where the name of something is not known.

.. _style_unknown_and_untitled_special_purpose_artist:

Special purpose artist
----------------------

Several special artists exist in the database to deal with unusual cases. There always are some unnoticed bogus artists, but those Special Purpose Artists (SPAs) listed here exist officially, used to handle each of these various types of special case artists.

List of official SPAs
+++++++++++++++++++++

   - `[anonymous] <https://musicbrainz.org/artist/f731ccc4-e22a-43af-a747-64213329e088>`_ - The track artist is both unknown and unknowable. If you are not sure whether to use [anonymous] or [unknown], use `[unknown] <https://musicbrainz.org/artist/125ec42a-7229-4250-afc5-e057484327fe>`_.

   .. newline between bullets

   - `[data] <https://musicbrainz.org/artist/33cf029c-63b0-41a0-9855-be2a3665fb3b>`_ - Used for data CDs and data tracks (additional tracks on audio CDs that contain data other than standard CD audio). Note that :ref:`data track style <style_unknown_and_untitled_special_purpose_track_title>` should also be used to title data tracks.

   .. newline between bullets

   - `[dialogue] <https://musicbrainz.org/artist/314e1c25-dde7-4e4d-b2f4-0a7b9f7c56dc>`_ - Used for tracks which consist solely of dialogue, and for which a better credit can't be found (as such, this can be seen as a more specific "unknown/anonymous"). If a better credit can be found, use that if it's at all sensible. For example, the "`Royale With Cheese <https://musicbrainz.org/recording/1220c6aa-41a5-47b4-99e1-9dd586e491cc>`_" discussion from Pulp Fiction would be best assigned to "Samuel L. Jackson & John Travolta", not to [dialogue], since the actors talking are known even if not directly credited on the tracklist. If it seems against common sense to list all speakers in the artist credit, such as for a recording including several dozen speakers, then using [dialogue] is always an acceptable option. In any case, the speakers' performances within the track should always be indicated by a :doc:`vocals relationship </relationships/vocals>` (generally *spoken vocals*), if at all possible.

   .. newline between bullets

   - `[no artist] <https://musicbrainz.org/artist/eec63d3c-3b81-4ad4-b1e4-7c147d4d2b61>`_ - There is no artist. (Recorded silence or noise, if it is attributed to any artist, should be assigned to that artist and not to [no artist].)

   .. newline between bullets

   - `[traditional] <https://musicbrainz.org/artist/9be7f096-97ec-4615-8957-8d40b5dcbc41>`_ - Used for writer/composer (and related) credits when the work in question pre-dates any written or recorded version(s), having originally been passed down from musician to musician. Rather than being attributable to one [anonymous] or [unknown] artist/collaboration, this work is better described as having emerged from a musical tradition.

   .. newline between bullets

   - `[unknown] <https://musicbrainz.org/artist/125ec42a-7229-4250-afc5-e057484327fe>`_ - Used when a particular artist is unknown, but is potentially discoverable with further research. **Please do some research before using this artist**; this artist should **not** be used simply as a "lazy easy solution" to an artist you don't happen to know offhand.

   .. newline between bullets

   - `Various Artists <https://musicbrainz.org/artist/89ad4ac3-39f7-470e-963a-56509c546377>`_ - Used only for compilation-type releases or release groups containing tracks by multiple different artists. This artist shouldn't generally be used for recordings, tracks or works.

Subsets
+++++++

**Subsets of [unknown]**

Sometimes it is useful to be a bit more specific when using [unknown]. You can use one of the following as the artist credit if applicable:

   - [christmas music]
   - `[Disney] <https://musicbrainz.org/artist/66ea0139-149f-4a0c-8fbf-5ea9ec4a6e49>`_
   - `[theatre] <https://musicbrainz.org/artist/a0ef7e1d-44ff-4039-9435-7d5fefdeecc9>`_
   - [classical music]
   - [soundtrack]

Always include the square brackets ([]) to indicate that this is not the artist as credited.

As with regular use of [unknown], these should only be used as a last resort, pending further research.

**Subsets of [no artist]**

Similarly, it may be useful to be more specific when using [no artist]. You can use one of the following as the artist credit if applicable:

   - `[church chimes] <https://musicbrainz.org/artist/90068d37-bae7-4292-be4a-704c145bd616>`_
   - `[language instruction] <https://musicbrainz.org/artist/80a8851f-444c-4539-892b-ad2a49292aa9>`_
   - [nature sounds]
   - [news report]

They should only be used if the category is applicable, and if you would otherwise use [no artist].


.. _style_unknown_and_untitled_special_purpose_label:

Special purpose label
---------------------

In a number of situations, it was convenient to create "phony" :doc:`label </terminology/entities/label>` entries in the database, to deal with some special cases.

Special purpose labels are similar in intent and functioning to :ref:`special purpose artists <style_unknown_and_untitled_special_purpose_artist>`.

Please note that you **shouldn't create new special purpose labels all by yourself** without prior discussion about it with other editors in the `forums <https://community.metabrainz.org/>`_.

Special cases
+++++++++++++

   - `[no label] <https://musicbrainz.org/label/157afde4-4bf5-4039-8ad2-5a15acc85176>`_: `White labels <https://wikipedia.org/wiki/White_label>`_, self-published releases and other "no label" releases (usually bootlegs) should all be stored under this entry in the database.

   .. newline between bullets

   - `[unknown] <https://musicbrainz.org/label/46caaa9e-3e26-49b5-827c-64ccc73c1b07>`_: This label is one that we can't prevent from appearing in the database, at least acknowledging its existence helps us steer it (via :doc:`label subscriptions </terminology/terms/subscription>`). Please note that you **mustn't** use this label. If you don't know what the label is for a given release, just leave the label entry blank in the release event.

   .. newline between bullets

   - `MusicBrainz Test Label <https://musicbrainz.org/label/02442aba-cf00-445c-877e-f0eaa504d8c2>`_: This test label is for internal use only and should never be used. Please do not attempt to "clean up" this label.


Advanced information
--------------------

**About white-labels**

Note that in a number of cases white labels releases are actually possible to track down to a proper label (either from information engraved in the vinyl, or from third party sources). While such research is not expected from casual editors, and while it's perfectly legit to add such releases to [no label], editors willing to go further can certainly use the proper label instead, if any.

**About auto-releases (or self-releases)**

In some (somewhat rare) cases there is an imprint on the release (possibly the artist wants to give his "label" an identity). You may use that instead of [no label].

For digital releases a label field is sometimes required by stores, and as such self-releases sometimes get assigned the artist name, or a code assigned by the distributor (such as "123456 Records DK"), as the designed "label". These are still self-releases and should generally be added as [no label].


.. _style_unknown_and_untitled_special_purpose_track_title:

Special purpose track title
---------------------------

There are three main types of tracks that are titled in a specific manner in MusicBrainz: untitled tracks, which are *known* to have no title, unknown tracks for which the title (or lack of it) is not known, and data tracks, which are not real audio tracks.

Untitled tracks
+++++++++++++++

For untitled tracks, enter [untitled] as the name. These tracks are clearly shown to lack a title on the release (album sleeve and liner notes) they appear on.

   - The recording and work used for the track will normally be also [untitled], but if the track is given an official name in another release, the recording and work should be updated.

   .. newline between bullets

   - If the track is widely known under an unofficial name, you can use that name between square brackets (conforming to the :doc:`Capitalization Standard </style_guides/language_guides/_language_guides>`) as track name instead.

   .. newline between bullets

   - For tracks that do not contain songs and that are not named by the artist, you can enter a descriptive name between brackets in all lowercase, or [untitled]. If the track contains only silence, use [silence].

Unknown tracks
++++++++++++++

For music tracks for which the name (or the lack of it) is unknown, enter [unknown] as the name.

   - A hidden track, or a bonus track that appears as just "Bonus Track", is not [untitled]; it is [unknown]. None of the two are clearly shown as lacking a title on the release -nor, in the case of hidden tracks, shown on the release at all.

   .. newline between bullets

   - If the artist gives the track a name somewhere else (for example, on their website) that name should be used instead of [unknown]. If the title of a track added as [unknown] is given at a later point, the [unknown] title should be updated. If the track is confirmed to have no title, it should be changed to [untitled].

Data tracks
+++++++++++

If an audio CD contains a data track at the end which is not visible in an audio CD player, it should not normally be included in the main part of the tracklist.

However, if such data tracks contain audio or video tracks, these tracks should be entered in the data tracks section of the tracklist (enabled by selecting the "This disc contains data tracks at the end" option in the release editor).

If an audio CD contains a data track which is visible in an audio CD player (typically as the first track), use [data track] as the track name. Only if the data track is on a Various Artists release, use `[data] <https://musicbrainz.org/artist/33cf029c-63b0-41a0-9855-be2a3665fb3b>`_ as the artist for that track.

Examples and specific indications
---------------------------------

**[untitled]**

   - A clear example of the use of [Unofficial Name] is `Aphex Twin's Selected Ambient Works Volume II <https://musicbrainz.org/release/ead065b1-b582-4ac1-9041-f0c09b0ac67a>`_, that has no titles on the `cover <https://coverartarchive.org/release/ead065b1-b582-4ac1-9041-f0c09b0ac67a/21166529227.jpg>`_, but images.

   .. newline between bullets

   - In some genres, like techno music, it is relatively common for releases to have a title, but no title for the individual tracks, as `Christian Wünsch's Proved Negligence <https://musicbrainz.org/release/69b5d797-0ef0-4b66-a70c-852d16fe9c67>`_. These tracks should be considered untitled tracks, and can be entered as [untitled] or, following the unofficial name guideline, as [Release Name, Part X] (always in square brackets).

   .. newline between bullets

   - As indicated above, the descriptive name option can be used, in lowercase, for live bootleg releases where there are tracks containing crowd noise, a guitar solo, etc. Corresponding names would be [crowd noise] and [guitar solo], e.g. `track 3 <https://musicbrainz.org/recording/6c791b84-6b81-4474-8709-d8cfd548e1e1>`_.

   .. newline between bullets

   - Some releases separate bonus tracks from the listed tracks by one or more tracks that contain only silence. A version of Nine Inch Nails' `Broken <https://musicbrainz.org/release/9c0b5a23-ca6e-4b4e-be2f-98280cf56c88>`_ uses the full 99 tracks available to the CD format; tracks 1 to 6 are music, tracks 7 to 97 are silence tracks, and tracks 98 and 99 are 'hidden' tracks. As indicated, these should be named [silence].

**[unknown]**

   - As mentioned above, [unknown] applies to "hidden" songs, e.g. `track 11 on Cords' No Guru No Method No Beeper <https://musicbrainz.org/recording/9362d9e2-899b-4a74-bf9a-4c339abb996f>`_. When they appear on a track that also has a listed song, this rule should be used in combination with :ref:`the one for multiple titles <style_guides_title_capitalization_multiple_titles>`, e.g. `track 13 on Bush's Razorblade Suitcase <https://musicbrainz.org/recording/de56b122-a175-4d52-afda-c130511a1725>`_.

   .. newline between bullets

   - The titles on a white label vinyl release are always [unknown], not [untitled]. As indicated, if any of these tracks are released in an official way and receive names, they should also be named in the white label release.

   .. newline between bullets

   - If a live bootleg includes a new, previously unreleased track that is not introduced with its name, it should be entered as [unknown] (and be changed to the official name when / if it is given one).

**[data track]**

   - Having a data track as the first track is most common in videogame CDs, as in `Magic & Mayhem <https://musicbrainz.org/release/9cd9e81a-2dab-46d0-988e-bb486ddc1b05>`_ and `Age of Empires II: The Age of Kings <https://musicbrainz.org/release/4efabf72-de25-4800-bd13-229753a4b2e3>`_.
