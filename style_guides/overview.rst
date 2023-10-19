.. MusicBrainz Documentation Project

Style Guides
============

Users of MusicBrainz and the members of the :doc:`Style Council </style_guides/style_council>` put some great efforts in working out detailed style guidelines, which state how data should be formatted.

.. https://musicbrainz.org/doc/Style/Principle

.. _style_guides_principles:

The Style Principles
--------------------

Status: **Official Style Guideline**

If you ask yourself in what style something should be entered into MusicBrainz, the following principles apply:

   - Follow :ref:`Artist intent <style_guides_principles_artist_intent>`.
   - If no definite proof can be found for the correct spelling/punctuation, the **most common version** should be used.
   - Follow the :doc:`style guidelines </style_guides/_detailed_guides>`.


**Alternative phrasing**

This can also be explained from the bottom upwards:

   - Usually you stick to the :doc:`style guidelines </style_guides/_detailed_guides>`.
   - If you are still unsure how to enter something because it is labelled inconsistently on official sources, use the most common version.
   - Finally there is the notion of :ref:`Artist intent <style_guides_principles_artist_intent>`. If you can show that the artist intended something to be stylized a special way, then you should enter it like that into the database.


.. https://musicbrainz.org/doc/Style/Principle/Error_correction_and_artist_intent

Error correction and artist intent
----------------------------------

As a general rule, MusicBrainz editors should correct spelling and punctuation and, to a lesser extent, grammar errors in :doc:`artists' names </terminology/entities/artist>`, as well as the :doc:`titles </style_guides/titles>` of :doc:`works </terminology/entities/work>`, :doc:`recordings </terminology/entities/recording>`, :doc:`tracks </terminology/entities/track>` and :doc:`releases </terminology/entities/release>`. However, this rule does not apply if it can be shown that an :doc:`artist </terminology/entities/artist>` intentionally used unorthodox spelling, punctuation or grammar.


.. _style_guides_principles_error_correction:

Error Correction
++++++++++++++++

There are many cases of record companies incorrectly reproducing titles or even artist names, or breaking generally accepted rules of usage for stylistic purposes. In such cases it often makes sense to fix errors and standardize irregularities, valuing correct spelling, punctuation and grammar over faithfulness to the printed release cover. When the correction might be confusing, adding an annotation is encouraged.

A common example of error that should be fixed is tracks being printed in the incorrect order on a release's packaging. The release tracklist should match the real (rather than printed) order, and a note explaining the issue should be added to the release annotation.

**Examples**

- "`State of Mind <https://musicbrainz.org/release/5c7a551d-172f-41cc-8c45-001fe4c2a8df>`_" by `Front Line Assembly <https://musicbrainz.org/artist/b847e9d2-c931-4daf-900c-42c7b2c42e16>`_ (artist name misspelled on cover and CD)
- "`The Beatles <https://musicbrainz.org/release/d6213baf-e959-4817-9fa2-3ce97f131678>`_" (inconsistent capitalization of track titles on gatefold interior)
- "`EPs 1988-1991 <https://musicbrainz.org/release/15ff481d-0857-46d3-94ce-eee09c36f4bc>`_" by `My Bloody Valentine <https://musicbrainz.org/artist/8ca01f46-53ac-4af2-8516-55a909c0905e>`_ (incorrect apostrophe in release title on spine)
- "`Christmas in Carolina <https://musicbrainz.org/release/6f39c99c-8268-4c1a-982b-871ece7841dc>`_" by `Various Artists <https://musicbrainz.org/artist/89ad4ac3-39f7-470e-963a-56509c546377>`_ (tracks swapped/in the incorrect order on packaging)


.. _style_guides_principles_artist_intent:

Artist Intent
+++++++++++++

Artists sometimes choose to present names and titles in ways that deliberately contradict the rules of the language they're in (e.g. unorthodox spellings) and/or the MusicBrainz Style Guidelines. To describe the way we handle such choices, we use the term "artist intent." The general idea is that if an artist intended something to be written in a special way, then MusicBrainz should follow that intent.

Unfortunately, it can be difficult to find out what an artist intended. If you want to claim that some deviation from the Style Guidelines should be considered artist intent, the burden of proof lies on you. A seeming error may be considered evidence of artist intent if it is consistently found on all of an artist's official releases. The best evidence would be a statement of intent by the artist (e.g. `edit 6892422 <https://musicbrainz.org/edit/6892422>`_).

Words in Latin script used in Japanese releases present a special case and are generally treated as artist intent; see the :doc:`Japanese style guidelines </style_guides/language_guides/japanese>` for more information.

**Examples**

- `2raumwohnung <https://musicbrainz.org/artist/5579a23d-c411-4930-987d-ff89d77c1c12>`_, `a-ha <https://musicbrainz.org/artist/7364dea6-ca9a-48e3-be01-b44ad0d19897>`_ and `k.d. lang <https://musicbrainz.org/artist/675c1c5e-5625-4a5e-97a2-b02aab5db2fc>`_ (artist names in all lowercase)
- `Guns N' Roses <https://musicbrainz.org/artist/eeb1195b-f213-4ce1-b28c-8565211f8e43>`_ (artist name spelled with N' instead of 'n')
- `locomotor ataxia <https://musicbrainz.org/artist/f5248869-2609-43db-8234-3065e11f1e1a>`_ (all lowercase for artist name, release titles and track titles)
- `eMOTIVe <https://musicbrainz.org/release/92b36219-760b-4f32-94f7-4e323e6d431d>`_ (unusual capitalization of release title)
- "`Use ta Be My Girl <https://musicbrainz.org/work/6b275557-c755-4bed-8735-70dff76a03a1>`_" and "`Yer Blues <https://musicbrainz.org/work/4387e237-03c5-3d59-a602-0ba90d41f900>`_" (unorthodox spellings in work titles)


Old style practices
-------------------

This section talks about the things we used to do, but no longer need to now that the data can be entered properly.

The limitations of the structure of the database has often meant that we couldn't enter data in the most logical way and we needed to find other ways to enter the data. Since the database is very large, it can take quite some time for the data to be fixed when guidelines change or new features are added, so you may come across some of the things described on this page. If you do, feel free to help fix it.

There were a few things which were particularly problematic in the past:

- A release couldn't contain more than one disc. That meant that each disc had to be entered separately.
- Each release and track could only only be linked to one artist. One-off collaborations had to be entered as separate artist entries.
- Releases with the same track listing weren't separate releases, but were instead different release events in the same release. There was no way to specify exactly which version of a release information belonged to.

Discs
+++++

To handle releases with multiple discs, we developed a style (Disc Number Style) to standardise the disc numbers and disc titles. People would also often add links to the other discs in the annotation. Later, a “part of a set” relationship was added to link the discs together. You may still see releases using "(disc n)" in the title, with links to the other discs in the annotation or with those relationships if they haven't been fixed yet.

Examples of Disc Number Style:

- "Release Title (disc 1)"
- "Release Title (disc n: Disc Title)"
- "Release Title (bonus disc)"

Collaborations
++++++++++++++

Originally, in order to reduce the number of one-off collaborations in the database, we had a style guideline which said to enter a track such as "Song Name" by "Artist A & Artist B" as "Song Name (feat. Artist B)" by "Artist A". This was particularly controversial and was eventually removed, but you may still find collaborations credited in this way.

After that, we allowed people to add collaborations as new artists with a name such as “Artist A & Artist B”, and had a “collaboration” relationship to link to the artists involved.

With the introduction of :doc:`artist credits </terminology/entities/artist_credit>`, we can link to multiple artists and we don't need to use separate collaboration artists. Many of the existing collaborations with collaboration relationships were converted into artist credits, but you may still see some which couldn't be automatically converted. You may also see ones that didn't have the proper relationships at all.

Featured artists
++++++++++++++++

Featured artists used to be entered as part of track titles, as "Song Name (feat. Artist B)" by "Artist A". With artist credits, the decision was taken to move them to where they properly belong, the artist field (e.g. "Song Name" by "Artist A feat. Artist B"). You can still find some featured credits entered in the old way, which should be moved to the artist credit.

Additionally, historically we mandated standardizing all featuring credits to the word " feat. ". This is no longer the case (whatever is printed should generally be used) but you might still find a lot of featuring credits standardized in this way. Feel free to update them!

Release events
++++++++++++++

At first, instead of having a separate entry for each release, every version with the same track listing was part of the same entry and that entry had multiple release events which consisted of both a date and a country. Later, support for labels, catalogue numbers, barcodes and formats was added and the date and country were made optional.

The way the data was stored also meant that a release could only have one release title, so if a later version had a slightly different title, we couldn't store that information. Releases also only had one status, so we couldn't mark certain release events as promos or bootlegs either.

Lastly, release relationships also belonged to the release and not to specific release events. There was no way to say which release event that relationships such as cover art, ASIN, Discogs or purchase relationships belonged to, so you may find releases where these links are on the wrong releases.

Annotations
+++++++++++

We often use annotations to store information which doesn't fit into the database at the time. There are far too many things to list here, so this is just a list of some of the most common things you're likely to see. Of course, once data has been entered properly, it can be removed from the annotation.

Some things which annotations have been used for include:

- Labels, catalogue numbers, barcodes and formats (see the "Release events" section).
- The release country or the release date, from the time when a release event had to have both a date and country.
- Whether some releases were bootlegs or promos.
- Which version of a release an ASIN corresponded to.
- "iTunes", "limited edition", etc. These can now be added to release comments.
- Links to the other discs in the set (see the "Discs" section).
- Credits which couldn't be added because there wasn't an appropriate relationship (e.g. instruments which weren't in the list).
- Clarifying credits where the relationships weren't flexible enough.

Earliest release relationship
+++++++++++++++++++++++++++++

Originally it wasn't possible to share recordings (then called tracks) between releases. If a recording was identical, they could be linked with the "earliest release" relationship. Most of these were automatically merged, but there were some which weren't. Now that recordings can be merged, if they're the same, they should simply be merged.
