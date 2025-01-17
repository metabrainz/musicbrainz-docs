.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Disambiguation_Comment

Disambiguation Comments
=======================

Disambiguation comments are used to distinguish identically or similarly named artists, labels, and other entities. They are visible on entity pages, as well as in search results.

- Comments should be in English and kept short. A few words are usually enough to disambiguate the entity.
- Follow the same capitalization guidelines as for :ref:`extra title information <style_guides_title_extra_title_information>`, as these comments are not part of the name.

When creating an artist, label, or place [#]_ that shares its name with an existing one, you will be prompted to enter a disambiguation comment. However, you will **not** be prompted to add a disambiguation comment for the pre-existing entity with the same name. It is ideal to add comments to the existing entities as well to avoid confusion for other editors.

Examples
--------

- `Randy Jackson <https://musicbrainz.org/artist/593abf14-4292-4d62-b365-79c7674cd1a5>`_ has the disambiguation comment "brother of Michael and Janet."
- `Randy Jackson <https://musicbrainz.org/artist/39828c81-cc39-4e8a-8e00-f0874c657d47>`_ has the disambiguation comment "former bassist with Journey and American Idol Judge."
- The album `Weezer <https://musicbrainz.org/release-group/9b8af98f-8214-32ee-9b05-96b8c557f7f0>`_ has the disambiguation comment "Red Album."
- The album `Weezer <https://musicbrainz.org/release-group/923d5ba6-7eee-3bce-bcb2-c913b2bd69d4>`_ has the disambiguation comment "Green Album."

When Not to Disambiguate
------------------------

Disambiguation comment fields should **not** be used to store general background information. Such information belongs in the :doc:`annotation </terminology/terms/annotation>`.

Certain entity types, such as recordings, releases, release groups, and works, are usually distinguishable by their artist data, type, and other information. Only add disambiguations when they provide details not already displayed in the general interface or search results.

Examples of usually **not-useful** disambiguation comments (where the bracketed information is already displayed elsewhere):

- `[release] (barcode)`
- `[release group] (album/EP/single)`
- `[recording] (by artist)`

Examples of usually **useful** disambiguation comments:

- `[work] (1999 revision)`
- `[release] (red vinyl)`
- `[recording] (mono/stereo/5.1 surround)`

.. [#] If the places are in the same area, or the area isn't set.
