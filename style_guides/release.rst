.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Style/Release

Release
=======

Status: **Official Style Guideline**

.. _style_release_title:

Title
-----

See the :doc:`titles guidelines </style_guides/titles>` for the release, medium and track titles.

If several versions of a title are provided, such as when release title differs between cover and spine, or the track titles differ between the back cover and a booklet tracklist, it's generally better to follow the more detailed one.


.. _style_release_artist:

Artist
------

In general, you should just enter the artist(s) as shown on the release (see the :doc:`guidelines for artist credits </style_guides/artist_credits>`). If no artist is credited, but a company is (such as a video game studio or a production music library), you can credit the company as a release artist. Otherwise, see :ref:`Special Purpose Artist <style_unknown_and_untitled_special_purpose_artist>` for what to enter when there is no proper artist or the artist is unknown.


.. _style_release_track_artist:

Track artist
------------

Track artists should follow the release artist, except where another artist is credited in the track listing of the release. This can include various artists releases, :ref:`featured artists <style_guides_artist_credits_featured_artists>`, and tracks credited to another artist. If the release artist is a Special Purpose Artist, the performer should be credited if known, or `[unknown] <https://musicbrainz.org/artist/125ec42a-7229-4250-afc5-e057484327fe>`_ otherwise.


.. _style_release_date:

Date
----

The :doc:`release date </terminology/terms/release_date>` is the day when this specific release was first made available. It should not be used to store the performance/recording date, the copyright date or the import date.

For a reissue of an earlier release, this is the date when the reissue was released (for example, do not use the original vinyl date for a CD reissue).

For digital music, note that online platforms often do not display release dates, or will display the release date from an earlier physical release instead (which may sometimes be even earlier than the date the platform itself was launched). In cases where you are not certain that a release date is correct, it's better to not enter a date at all, or to indicate it in the annotation only while listing your misgivings about it.


.. _style_release_barcode:

Barcode
-------

Only one barcode can currently be stored in this field. If a release has add-on codes, store them in the annotation. Similarly, if a release has multiple full barcodes, enter all others in the annotation.

The actual (machine-readable) barcode should be chosen over the printed (human-readable) number in cases where the second is incomplete (e.g. missing the check digit) or incorrect.


.. _style_release_label:

Label
-----

If the release is a white label, self released or has no label, check the guidelines for :ref:`special purpose labels <style_unknown_and_untitled_special_purpose_label>`.


.. _style_release_catalog_number:

Catalog number
--------------

If the release has no catalog number, use "[none]".


.. _style_release_status:

Status
------

**Bootleg** should be used for pirated/counterfeit/unofficial releases, but not every unofficial release should be added as a MusicBrainz bootleg. An exact digital rip of an official physical release does not qualify for a separate bootleg release, even if no official digital release exists.

Examples:

   - `1972-02-20: Dark Side of the Sky: Rainbow Theatre, London, UK <https://musicbrainz.org/release/6395109f-4d23-4324-9670-79b12eb8555f>`_ is a :doc:`live bootleg </style_guides/types_of_releases/live_bootlegs>`, from the audience or from the soundboard at a show

   - `Silent Hill 2 <https://musicbrainz.org/release/cabaa10d-dd1d-42d5-94b4-3f15473dbecc>`_ is an illegal version of an official CD

   - `Silent Hill 2: Complete <https://musicbrainz.org/release/d20dfff3-8607-46dc-9ec1-4de7f9e64331>`_ contains audio 'ripped' from a game (a game-rip)

**Pseudo-release** should be used for translations or transliterations that do not appear on an actual release (even if they appear on an official site). Pseudo-releases should be linked to the original tracklist using the transl(iter)ation relationship where possible. Not all translations and transliterations are pseudo-releases.

If the release has tracks listed in multiple languages, the entry with both languages included is considered to be the official release. Entries with only one of the languages on the cover should be set to pseudo-release.

In situations where the physical release can not be obtained and the artist's official site lists multiple languages, default to the native release language of the artist as the official version and the others as pseudo-releases.

Examples:

   - `千と千尋の神隠し <https://musicbrainz.org/release/7a16f215-079e-4c55-abda-06f9a4228b6a>`_ is the original Japanese tracklist. This is the same as the Japanese release, so it is set to official.

   - `Spirited Away <https://musicbrainz.org/release/7327ef89-e214-4f90-8d5d-3e56ffe21d0b>`_ is the same tracklist translated into English. This is the same as the American release, so it is also set to official.

   - `Sen to Chihiro no Kamikakushi <https://musicbrainz.org/release/9fe92739-5bcd-4f6e-b2f2-d2db97cabc32>`_ is a transliterated version of the Japanese tracklist. There is no known release which has this tracklisting, so it is set to pseudo-release.

**Withdrawn** is to be used for previously official releases that were actively withdrawn from circulation. This does not include releases that have reached the end of their 'natural' lifecycle, such as an album being sold out, replaced by a shinier version, or retired from a streaming service. The artist (or label) also needs to consider it expunged from their discography.

Use the initial release date, before they were withdrawn, for these releases.

Examples:

   - An attempt was made to cancel `Play Date (100 gecs remix) <https://musicbrainz.org/release/5d2b4d08-e7c5-4d71-88b7-49bd2d62ea94>`_, but it was available briefly in at least one time zone before being withdrawn.

   - The original pressing of `逆転裁判＋逆転裁判２ オリジナル・サウンドトラック <https://musicbrainz.org/release/0376559a-5544-46cc-8d2d-8651bc38a5e6>`_ was recalled due to a mastering error.

   - `U2 <https://musicbrainz.org/release/78df1542-37a6-3051-a939-899634a3e673>`_ by Negativland was withdrawn due to a trademark infringement lawsuit.

   - Sony BMG `recalled <https://web.archive.org/web/20181106182152/https://www.ft.com/content/e9e41f72-56f4-11da-b98c-00000e25118c>`_ all CDs with the 'XCP' copyright protection software, after pressure from consumer advocacy groups.

**Cancelled** is to be used for a planned official release that was cancelled before being released, but for which enough information is known to still confidently list it (for example because it was available for preorder).

Examples:

   - `命の花 <https://musicbrainz.org/release/e057ba4b-fc6f-4319-9ec0-343499d21065>`_ was cancelled in the wake of the Great Hanshin Earthquake.

   - `GOLDEN☆BEST <https://musicbrainz.org/release/e9fc3793-a07e-4233-965a-5c0afbc4302c>`_ was cancelled after the artist's arrest.

   - `Erotica <https://musicbrainz.org/release/635a583d-fbce-4bd3-909d-c8ad3320e46f>`_ was cancelled because of potentially controversial imagery.

   - The masters for `[New Mexico demo] <https://musicbrainz.org/release/ab7b87df-1f48-45c3-badf-cda3ae05bbf4>`_ were lost, but later released in a compilation.


.. _style_release_language_and_script:

Language and script
-------------------

The language attribute should be used for the language used for the release title and track titles. It should not be used for the language the lyrics are written in, nor for the language used for other extra information on the cover.

If several languages are used in the titles, choose the most common language. For releases where there's an equal mix of two or more languages and hence no obvious answer, 'Multiple Languages' may be the best choice. But remember that it is quite common for languages to borrow words and phrases, and so "Je ne sais quoi" in an English title does not make something multiple languages, nor do a few English words in a foreign language title. (Some languages borrow quite extensively, and especially for Japanese, unless most of the titles are in other languages, Japanese is probably the best choice.)

If several scripts are used in the titles, choose the most common script. For releases where there's an equal mix of two or more scripts and hence no obvious answer, 'Multiple Scripts' may be the best choice. However, as the Latin script is common in many languages that primarily use another script, Latin should only be chosen if there are no more than one or two titles (or a few characters) in other scripts. For example, a Japanese release with a mix of English and Japanese titles should normally use 'Japanese' as the script.


.. _style_release_medium_format:

Medium format
-------------

For dual layer/side formats (Hybrid SACD, DualDisc, DVDplus) a medium should be added for each layer, set to the specific layer sub-format (e.g. "DualDisc (CD side)"). When a hybrid SACD has the same tracklist on both layers it is acceptable (for the sake of convenience) to enter it as just a single medium (set to "Hybrid SACD"), but any hybrid SACD that has been entered as two layers shouldn't be changed to the one medium style.

For SACD-related formats, two additional sub-formats are available to represent the 2 channel and multichannel table of contents (TOCs) on SACDs. When entering SACDs, it is preferred to specifically enter mediums for any TOC available on the disc (be it one of each, only 2 channel or, in rare cases, only multichannel). While it's acceptable to just use the standard format if you're not sure about the TOCs, please do not change SACDs entered with separate TOC mediums to the one medium style.


.. _style_release_medium_title:

Medium title
------------

Medium titles should only be added if each medium in a multi-disc set has an actual title (e.g. "The Early Years" vs. "The Late Years" in a best of compilation). "CD n" or "Disc n" should not be entered as a medium title.


.. _style_release_single_release:

What should be added as a single release?
-----------------------------------------

For physical media, most differences will mean a different release (see the section below). Whether different CD matrix info should always be separated is an open question; for now, do not merge them if another editor has made the effort to split them.

For digital media, which is very often made available from multiple online sources, don't create a new release when the only differences appear in the following list:

   - **Different streaming services or digital storefronts.** The services offering a release should instead be linked via :doc:`URL relationships </relationships/urls>`.

   .. newline between bullets

   - **Differences in available regions that are not due to artist or label intent.** Different services operate in different countries, and availability is often further limited due to geopolitics or legal requirements.

   .. newline between bullets

   - **Minor differences in artist name, release title, or track titles.** Most services impose their own metadata rules, and minor differences are rarely due to artist intent. Typographical errors are frequently introduced during data entry, and :ref:`extra title information <style_guides_title_extra_title_information>` may be displayed in different ways. :ref:`Artist intent <style_guides_principles_artist_intent>`, the :doc:`official style guidelines </style_guides/_detailed_guides>`, and the way that the release is presented on other platforms should all be considered when determining what to enter into MusicBrainz.

   .. newline between bullets

   - **Different audio formats (e.g. MP3, FLAC, AAC, ALAC) or bitrates or "hi-res" releases.** Digital media can easily be converted from one format to another, and lossless formats like FLAC and ALAC are sometimes used to re-encode files that were previously encoded in lossy formats like MP3 and AAC.

   .. newline between bullets

   - **Service-specific mastering, e.g. Apple Digital Masters or Tidal Masters.**


.. _style_release_multiple_releases:

What should be added as multiple releases?
------------------------------------------

For physical media, most differences will mean a different release. Specifically, **any difference in artwork requires a different release**. This includes differences in the legal text on the back cover, even if everything else is the same. An exception should be made for releases where every cover will necessarily be different (like hand-printed, hand-made or even knit covers): in this case, it can be assumed that all the different versions are equivalent and qualify as just copies of the same release, unless a difference is explicitly made by the artist or label. Whether different CD matrix info should always be separated is an open question; for now, do not merge them if another editor has made the effort to split them. Different pressing plants require different relationships and as such different releases.

For digital media releases, only add a new release to MusicBrainz when there was clear intent by the artist or label to create multiple releases. This requirement can be satisfied by the following:

   - **Different recordings in the tracklist.** For example, separate releases should be created for the clean and explicit versions of an album.

   .. newline between bullets

   - **Different song ordering, or songs being included or excluded.** For example, a deluxe edition containing bonus tracks should be represented by a separate release. If additional tracks are added to an already-released album, a new release should be created with the new tracklist.

   .. newline between bullets

   - **Differing** :doc:`barcodes </terminology/terms/barcode>`. Not all services list releases' barcodes, however, so do not automatically assume that no barcode being visible means a new release must be added.

   .. newline between bullets

   - **Differing** :doc:`labels </terminology/entities/label>` **responsible for the release.** Note that online services are often inconsistent or unreliable in how they credit labels, so only split these if you're sure.

   .. newline between bullets

   - **Different** :doc:`cover art </terminology/terms/cover_art>`. Any differences beyond size/quality changes and minor color differences justify multiple releases.


.. _style_release_cover_art:

Cover art
---------

The cover art for a release must **always** exactly match the actual art for **that specific release**. Artwork for a release should not be added to another release: for example, digipaks are not square, and a square digital front cover should not be uploaded to a digipak release.

While high quality scans are preferable for all physical releases, it is acceptable to add a square digital front cover to a CD release if you are completely sure that it is exactly the same (both on shape and design) as on the CD. For example, if you have the disc but do not have a scanner, a good quality digital image that looks the same is an acceptable substitute. If you're not sure, do **not** upload the image to the CD (you should of course still upload it to the corresponding digital release).


.. _style_release_replaced_releases:

Replaced releases
-----------------

Sometimes an artist will take down or recall an existing official release and then immediately reissue it with some changes; this is especially common for digital media releases. In these cases, mark the taken down release with the Withdrawn status and add a new release to the release group with the appropriate changes (and a release date matching whenever the change happened, if known). You can link these releases with the :doc:`"replaced by" relationship </relationships/replaced_by>`. For example, if a trans artist re-releases their releases after a name change, the old releases should be marked as Withdrawn (not edited nor removed) and new releases should be added to replace them.

Keep in mind this applies only for straight replacements; a release being reissued of course doesn't mean the previous versions should be marked as Withdrawn.
