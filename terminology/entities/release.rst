.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Release

Release
=======

A MusicBrainz release represents the unique release (i.e. issuing) of a product containing at least one audio :doc:`medium </terminology/entities/medium>` (a disc, for example, on a CD release). Each release has one or more identifying properties, such as a release date and country, a label, a barcode, a specific type of packaging or a specific cover art.

If you walk into (or digitally browse) a store and see the standard edition of an album next to a deluxe edition of that same album, you're looking at two different MusicBrainz releases, which are grouped as part of the same :doc:`release group </terminology/entities/release_group>`.

Mediums have a format (such as CD, DVD, vinyl or cassette) and can optionally also have a title. For physical releases, each medium is the actual physical medium that stores the audio content. This means that each CD in a multi-disc release will be entered as separate mediums within the release, and that both sides of a vinyl record or cassette will exist on one medium. For digital releases, mediums are a more fluid concept, and should generally just follow the structure set by the artist or label. For example, a digital album that claims to include "disc 1" and "disc 2" should be added with two digital mediums, even if it can be purchased as one single folder of files or streamed in a single sitting.

Keep in mind there are some exceptional cases where the one disc to one medium equivalence does not apply. For example, the two sides of a hybrid SACD (the CD side and the SACD side) should be entered as two mediums. These exceptions are indicated in the :doc:`release guidelines </style_guides/release>`.

Every medium can (and should ideally) have a tracklist, which represents the set and ordering of :doc:`tracks </terminology/entities/track>` included in the medium, as listed on a liner, a digital store page, or any other official source. A medium can be empty (missing its tracklist) if its contents are not yet known to MusicBrainz users.

Examples:

   - CD single: `Creep <https://musicbrainz.org/release/ed118c5f-d940-4b52-a37b-b1a205374abe>`_
   - 2x CD album: `The Fragile <https://musicbrainz.org/release/a4864e94-6d75-4ade-bc93-0dabf3521453>`_
   - Vinyl single: `Feel the Music <https://musicbrainz.org/release/e6e4ae10-4241-43a5-a9ae-911277348c59>`_
   - 2x vinyl album: `Blonde on Blonde <https://musicbrainz.org/release/2b259ee4-06b0-4dbb-a248-be983aee6fbd>`_
   - 4x digital media album: `Terraria: Official Soundtrack <https://musicbrainz.org/release/51031f3d-033a-4ab1-9739-a33b4e3eef02>`_
   - Digital audiobook: `Der Schattenkrieg <https://musicbrainz.org/release/594687cc-bdc1-4fff-858f-25bb5ec0d87d>`_

Style guidelines
----------------

Please see the :doc:`guidelines for releases </style_guides/release>`.

Release properties
------------------

.. _entities_release_title:

**Title**

The title of the release.


.. _entities_release_artist:

**Artist**

The artist(s) that the release is primarily credited to, as :doc:`credited on the release </terminology/entities/artist_credit>`.


.. _entities_release_date:

**Date**

The :doc:`date </terminology/terms/release_date>` the release was issued.


.. _entities_release_country:

**Country**

The :doc:`country </terminology/terms/release_country>` the release was issued in.


.. _entities_release_label:

**Label**

The :doc:`label </terminology/entities/label>` which issued the release. There may be more than one.


.. _entities_release_catalog_number:

**Catalogue number**

This is a number assigned to the release by the label which can often be found on the spine or near the barcode. There may be more than one, especially when multiple labels are involved. This is not the ASIN — there is a :doc:`relationship </relationships/release-url/asin>` for that — nor the :doc:`label code </terminology/terms/label_code>`.


.. _entities_release_barcode:

**Barcode**

The :doc:`barcode </terminology/terms/barcode>`, if the release has one. The most common types found on releases are 12-digit `UPCs <https://wikipedia.org/wiki/Universal_Product_Code>`_ and 13-digit `EANs <https://wikipedia.org/wiki/European_Article_Number>`_.


.. _entities_release_status:

**Status**

The :ref:`status <style_release_status>` describes how "official" a release is. Possible values are:

   - **official** - Any release officially sanctioned by the artist and/or their record company. Most releases will fit into this category.

   .. newline between bullets

   - **promotion** - A give-away release or a release intended to promote an upcoming official release (e.g. pre-release versions, releases included with a magazine, versions supplied to radio DJs for air-play).

   .. newline between bullets

   - **bootleg** - An unofficial/underground release that was not sanctioned by the artist and/or the record company. This includes unofficial live recordings and pirated releases.

   .. newline between bullets

   - **pseudo-release** - An alternate version of a release where the titles have been changed. These don't correspond to any real release and should be linked to the original release using the transl(iter)ation relationship.

   .. newline between bullets

   - **withdrawn** - An official release that was actively withdrawn from circulation by the artist and/or their record company after being released, whether to replace it with a new version or to retire it altogether. This does not include releases that have reached the end of their “natural” life cycle, such as being sold out and out of print.

   .. newline between bullets

   - **expunged** - A previously official release that was actively expunged from an artist or records company’s discography. This should not be used in cases where the release was just withdrawn, there needs to be known artist or label intent to disown the release and no longer consider it part of their discography. If it is unclear, use Withdrawn.

   .. newline between bullets

   - **cancelled** - A planned official release that was cancelled before being released, but for which enough info is known to still confidently list it (e.g. it was available for preorder).


.. _entities_release_packaging:

**Packaging**

The physical packaging that accompanies the release. See the :doc:`list of packaging types </terminology/terms/packaging_type>` for more information.


.. _entities_release_language:

**Language**

The language a release's track list is written in. The possible values are taken from the `ISO 639-3 <https://wikipedia.org/wiki/ISO_639-3>`_ standard.


.. _entities_release_script:

**Script**

The script used to write the release's track list. The possible values are taken from the `ISO 15924 <https://wikipedia.org/wiki/ISO_15924>`_ standard.

Guide to common scripts:

   - **Latin (also known as Roman or, incorrectly, "English")** - Latin is the most common script, and usually the correct choice. It is used for all Western European languages, and many others. It is also the most common script used for transliterations.

   .. newline between bullets

   - **Arabic العربية** - The Arabic script is used for languages in the Middle East and Central Asia such as Arabic, Persian and Urdu.

   .. newline between bullets

   - **Cyrillic Кириллица** - Cyrillic is used for languages in Eastern Europe such as Russian, Ukrainian, Belarusian and Bulgarian.

   .. newline between bullets

   - **Greek Ελληνικά** - The Greek script is used for Greek, but several characters have also been adopted for mathematical uses.

   .. newline between bullets

   - **Han 漢字/汉字** - Han characters are used by Chinese, Japanese and Korean. Han (simplified), Han (traditional), Japanese, or Korean should be used instead when the variant is known.

   .. newline between bullets

   - **Han (simplified) 简体字** - The simplified variant of Han characters is used to write Chinese in mainland China, Malaysia and Singapore.

   .. newline between bullets

   - **Han (traditional) 繁體字/正體字** - The traditional variant of Han characters is used to write Chinese in Hong Kong, Macao and Taiwan.

   .. newline between bullets

   - **Korean 한글** - This covers any combination of Hangul and Hanja for Korean.

   .. newline between bullets

   - **Hebrew עברית** - The Hebrew script is used for Hebrew, but a few characters have also been adopted for mathematical uses.

   .. newline between bullets

   - **Japanese 漢字 & ひらがな & カタカナ** - This covers any combination of Kanji, Hiragana and Katakana for Japanese.

   .. newline between bullets

   - **Katakana カタカナ** - Katakana should only be used for transliterations into Japanese (example, English->Japanese). Japanese language titles with words written in Katakana should use Japanese.

   .. newline between bullets

   - **Thai ไทย** - The Thai script is used for Thai, as well as some minor languages in south-east Asia.


.. _entities_release_mbid:

**MBID**

See the :doc:`page about MBIDs </terminology/terms/mbid>` for more information.


.. _entities_release_disambiguation:

**Disambiguation comment**

See the :doc:`page about comments </terminology/terms/disambiguation>` for more information.


.. _entities_release_annotation:

**Annotation**

See the :doc:`page about annotations </terminology/terms/annotation>` for more information.


.. _entities_release_data_quality:

**Data quality**

Data quality indicates how good the data for a release is. It is not a mark of how good or bad the music itself is - for that, use :doc:`ratings </terminology/terms/rating_system>`.

   - **High quality** - All available data has been added, if possible including cover art with liner info that proves it.
   - **Default quality** - This is the default setting - technically "unknown" if the quality has never been modified, "normal" if it has.
   - **Low quality** - The release needs serious fixes, or its existence is hard to prove (but it's not clearly fake).

Currently, data quality has no further effect than helping users know what to expect from the data. Until 2012, data quality also used to influence the voting requirements for edits made to the release. While this is no longer the case, we mention it here because it can explain the notes and voting results of some very old edits.


Medium properties
-----------------

.. _entities_release_medium_title:

**Title**

The title of this particular medium.


.. _entities_release_medium_format:

**Format**

The :doc:`format </terminology/terms/release_format>` of the medium.
