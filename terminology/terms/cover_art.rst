.. MusicBrainz Documentation Project

Cover Art
=========

Cover art, also known as "album art" or "album artwork," is artwork that provides a visual representation of a :doc:`release </terminology/entities/release>`. Normally, it refers to the front of the release packaging, but the `Cover Art Archive <https://coverartarchive.org/>`_ can store images of the back of the release packaging, the media itself, and many other pieces — right down to the sticker on the shrinkwrap.

Why Should I Submit Cover Art?
------------------------------

Throughout the history of the public internet, many databases have been built to provide cover art for music releases. Although MusicBrainz supports cover artwork being uploaded and linked to releases, it is not the primary focus of the website.

Cover art on MusicBrainz is often used as a form of evidence for the data in the database. This can include elements such as:

- Tracklist sequencing
- Performance and composition credits
- Licensing and publishing information
- Details about locations of recordings and performances
- Information about recording and transfer technologies used
- Pressing information for physical releases

By submitting cover art with your submission, another contributor can quickly check and confirm the accuracy of the supplied information. Accuracy is paramount to the goal of MusicBrainz.

For this reason, sourcing cover art can be slightly tricky and not as simple as copying the first image returned from a search engine.

- **For physical releases**: Use an imaging device such as a scanner or camera to take a clear and legible representation of the article in question.
- **For digital releases**: Take a copy of the artwork directly from the distribution platform where the digital release is available (e.g., Bandcamp, Spotify, Apple Music).

If sourcing cover art from an existing database or archive, take additional care to ensure it accurately matches the release to which it will be attached.

See the *Usage* section for more information about how to add cover art to a release.

Fan Art
-------

Any fan-made or edited artwork must not be uploaded to any release, except for bootleg releases where such artwork was part of the unofficial release. Fan art can be added to `fanart.tv <https://fanart.tv/>`_, which is linked to MusicBrainz release groups and can be used by Picard.

This restriction includes:

- Alterations to graphical elements in the image (e.g., advisory, hype, or point-of-sale stickers)
- "Image improvements," such as upscaling a small image using AI tools

In MusicBrainz Website Display
------------------------------

Due to legal licensing and copyright issues, MusicBrainz can display cover art only from:

- The `Cover Art Archive <https://coverartarchive.org/>`_
- Approved `cover art sites <https://musicbrainz.org/doc/Has_Cover_Art_At_Relationship_Type/Whitelist>`_
- Sites linked via a :doc:`cover art relationship </relationships/release-url/cover_art>` or an :doc:`ASIN relationship </relationships/release-url/asin>`

In Media Files
--------------

Media players that support cover art display do so in several ways, often supporting more than one mechanism. Images can be:

- Stored within the media player's internal library/database
- Stored as a separate file in the same folder/directory as the release, using a naming convention (e.g., *folder.jpg*)
- Embedded within each :doc:`track </terminology/entities/track>`'s metadata (e.g., ID3 tags)

`Picard <https://picard.musicbrainz.org/>`_ supports the second and third options out of the box via the `Cover Art Archive <https://coverartarchive.org/>`_ or various `third-party providers <https://picard.musicbrainz.org/docs/options/#cover-art-providers>`_.

Usage
-----

We welcome your contribution of cover art images. See :doc:`How to Add Cover Art </how-tos/add_cover_art>` for instructions. For a list of pieces of a release (e.g., *Front*, *Back*, *Medium*, *Obi*, etc.) that images can be labeled with, see `Cover Art Types <https://musicbrainz.org/doc/Cover_Art/Types>`_.

