.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Style/Titles

Titles
======

Status: **Official Style Guideline**

When entering a new release into MusicBrainz, the titles should be normalized by following these guidelines.

This page provides a summary of the important guidelines, please follow the links to the full guidelines when you need more information.


.. _style_guides_title_capitalization:

Capitalization standards
------------------------

Album and song titles are often found in upper-case on the back cover of CDs. For example, the album `Songs of Love and Hate <https://musicbrainz.org/release-group/964ccc52-2873-3bce-a806-73d71532c539>`_ is written as "SONGS OF LOVE AND HATE" on the cover. This is usually the choice of a graphic designer, not the artist. So, instead of copying the title from the cover, we follow certain rules to capitalize a title. The rules are different for each language.

Please see the :doc:`language-specific style guides </style_guides/language_guides/_language_guides>` for more information.


.. _style_guides_title_extra_title_information:

Extra title information
-----------------------

Additional information on a :doc:`release </terminology/entities/release>` or :doc:`track </terminology/entities/track>` name that is not part of its main title, but intended to distinguish it from different releases or tracks with the same main title (such as version/remix names or live recording info), should be entered in parentheses after the main title. Featured artists should **not** be entered like extra title information, but as part of the artist credits. See the :ref:`featured artists guideline <style_guides_artist_credits_featured_artists>`.

Titles and subtitles of mixes/versions are formatted according to the :doc:`appropriate language's guidelines </style_guides/language_guides/_language_guides>`; the other parts of this extra information should be in lower case except for words that would normally be capitalised in the language.

For :doc:`recordings </terminology/entities/recording>`, follow the same guidelines, with the exception of live performance data. For that, follow the :ref:`specific guidelines for live recordings <style_guides_recording_specific_types>`.

   - `Situations Like These (album version) <https://musicbrainz.org/track/dcee82bf-26f7-3e58-a1ed-f463a64ed647>`_
   - `Bear Witness (Automator's 2 Turntables and a Razorblade re-edit) <https://musicbrainz.org/recording/39060ef1-2616-4ddc-ae84-cb3fd6d56f88>`_

If your language requires the use of title caps or other non-standard capitalization rules (e.g. English), you may need to distinguish the title part and the descriptive part of the extra title information (ETI). If the ETI contains no names or title, keep to lower case. If it contains a distinct title, use the title capitalization rules. In case the ETI is a combination of title and descriptive parts, use lower case for the descriptive part only. The latter often contains words like mix, remix, live, remaster, edit, etc.

   - `Never Ending Story (power club vocal mix) <https://musicbrainz.org/recording/dc91f1db-c8a3-43ea-afc5-c3d18ca8d1ee>`_
   - `The Age of Love (Watch Out for Stella club mix) <https://musicbrainz.org/recording/91cb3f86-3f38-4045-9a2f-94868b63e1b9>`_

Some cases of additional information that is not part of the title and also not intended to distinguish the track should be removed:

   - "Song (bonus track)": just "Song"
   - "Song (new song)": just "Song"
   - "Song (The Beatles cover)": just "Song", with the recording linked to the appropriate The Beatles :doc:`work </terminology/entities/work>` with the :doc:`recording of </relationships/recording_of>` relationship (and the "cover" attribute).


.. _style_guides_title_subtitles:

Subtitles
---------

Use a colon (:) to separate any subtitles. If there is an alternative dividing punctuation mark such as the question mark (?) or exclamation point (!), use that mark instead of the colon.

   - `Biography: The Greatest Hits <https://musicbrainz.org/release-group/2a46ad10-e204-3e5c-b2ea-e717f83fa387>`_
   - `Who Cares a Lot? Greatest Hits <https://musicbrainz.org/release/0cb1e972-a21c-3410-8f04-c9d1f917557e>`_ (already has "?")
   - `Greatest Hits - Live Flash <https://musicbrainz.org/release/c9a82f65-f8ec-4a76-89b2-a50a012b7cfe>`_ (already has "-")


.. _style_guides_title_capitalization_multiple_titles:

Multiple titles / Splits
------------------------

When a release is a re-release of two or more other releases, a track includes two or more songs, or a `split release <https://en.wikipedia.org/wiki/Split_album>`_ has different titles for each artist, the title should be split as " Title 1 / Title 2" (space, slash, space). For otherwise unnamed split releases, use "Artist 1 / Artist 2" as the title.

The artist credit for tracks and recordings containing multiple songs by different artists, and for split releases and release groups should similarly be "Artist 1 / Artist 2".

   - `This Is the Modern World / All Mod Cons <https://musicbrainz.org/release/e5b6236b-874b-4862-b293-f46a02337eb2>`_ by `The Jam <https://musicbrainz.org/artist/23228f18-01d5-493e-94ce-cfcde82a8db2>`_ (two releases in one)
   - `Outsider / 14:31 / 110 Mistakes <https://musicbrainz.org/recording/3e40a6fd-d14d-4018-9385-9d22b131190d>`_ by `Burufunk <https://musicbrainz.org/artist/daec4ca8-7f91-4d7b-b362-1fbcae1390ea>`_ / `Global Communication <https://musicbrainz.org/artist/8179e236-86df-459f-bd51-0107138d0a6a>`_ / `MOT <https://musicbrainz.org/artist/b2e88c42-c535-43ad-b1a7-0c64f4cb961a>`_ (track with 3 songs)
   - `The Faith / Void <https://musicbrainz.org/release/86298e0a-4f20-4c36-8c33-a36c9d38c68f>`_ by `The Faith <https://musicbrainz.org/artist/f735a867-9a16-451f-8f83-669ed42e2574>`_ / `Void <https://musicbrainz.org/artist/960a1d2f-2b5f-4fcf-bf11-4957529a6508>`_ (split release)
   - `White Light/White Heat <https://musicbrainz.org/release/6d57f244-3b54-3b86-99b0-fdf6e2c44a2c>`_ (single title with a slash - the guideline only applies for multiple titles!).


.. _style_guides_title_series_numbering:

Series numbering
----------------

When a word such as “volume” (“vol.”) or “part” (“pt.”) is used in a title to indicate its position within a series (of releases, tracks, etc.), insert a comma before that word. If the word is already preceded by another punctuation mark, such as a question mark (?) or an exclamation point (!), keep that mark and do not insert a comma.

   - `Orchestral Songs, Volume 1 <https://musicbrainz.org/release/614c3594-6586-4527-83b6-5d4c15b5334a>`_ (“Volume” capitalized since it's English)
   - `Sonates, vol. 3 <https://musicbrainz.org/release/5855d2de-378b-499c-bb16-2c1c0aa18d7c>`_ (“vol.” lowercase since it's French)
   - `The Best Smooth Jazz… Ever! Vol. 4 <https://musicbrainz.org/release-group/ff7ce951-ad6c-4aec-a696-23c4d0a418c2>`_ (separated by !)
   - `Shine On You Crazy Diamond, Parts I-V <https://musicbrainz.org/recording/54029746-25ba-4f88-9885-387ac581e45f>`_
   - `Authority? Pt. 2 <https://musicbrainz.org/recording/bfe3e2a1-2b87-4bff-a0b8-a27cb5f8c1d4>`_ (separated by ?)
   - `The Piano Works 3 <https://musicbrainz.org/release-group/dca3c837-0725-43e6-ad76-a581ff9e692f>`_ (no volume/part word, so no separator needed)


.. _style_guides_title_format_descriptions:

Format designations
-------------------

If a release includes a designation such as **EP/E.P.**, **7"**, **CD**, **LP** or **single** as part of its title, include it in the release title. If a format designation is not explicitly part of the title, it should not be added.

   - `Flatline EP <https://musicbrainz.org/release/96b62482-e5b4-46bf-8539-da8342edee46>`_ (EP is on the title)
   - `Broken <https://musicbrainz.org/release/78bba056-8879-45c0-b8e3-f2146537568c>`_ (EP is just the release group type)


.. _style_guides_title_performers_in_titles:

Performers in titles
--------------------

Release and release group titles shouldn't generally contain performers unless they are clearly part of the title (either the performer includes it when mentioning the album, or the title seems "unfinished" without the performer name).

   - "`The Best of Tangerine Dream <https://musicbrainz.org/release/dc56e56f-6d14-4338-a97a-896069a2b18a>`_", not just "The Best Of" (compare with "`The Best <https://musicbrainz.org/release/e4062105-d0eb-344c-aef4-608186d593ca>`_").
   - "`Her Majesty the Decemberists <https://musicbrainz.org/release-group/5f135b33-c28f-36dc-aa9c-9a4851665226>`_", not just "Her Majesty" (per `performer usage <https://thedecemberists.bandcamp.com/album/her-majesty-the-decemberists>`_)
   - But "`Plays Metallica by Four Cellos <https://musicbrainz.org/release/f9f61db2-8d25-44aa-930f-3f00f6f45de0>`_", not "Apocalyptica Plays Metallica by Four Cellos", even though the title seems unfinished, because `artist intent <https://musicbrainz.org/edit/63252497>`_ supercedes the guidelines.


.. _style_guides_title_exceptions:

Exceptions and edge cases
-------------------------

Sometimes it isn't clear how the guidelines should be applied in a particular edge case. Currently, there are special guidelines for one edge case:

   - :doc:`OC ReMix series </style_guides/oc_remix_series>`
