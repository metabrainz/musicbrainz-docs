.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Aliases

Alias
=====

Aliases are alternative names for all types of :doc:`MusicBrainz entities </terminology/entities/_entities>`. There is no limit on the number of aliases set for an entity. In MusicBrainz, aliases have several uses:

   - In a **search**, when an entity's alias matches a search term (even if the entity's actual name does not), the entity will be given as a result.
   - Aliases are used to **localize** an entity's main name into a different language, especially into a different script (e.g. the Russian name `Чайковский <https://musicbrainz.org/artist/9ddd7abc-9e1b-471d-8031-583bc6bc8be9>`_ is known in English as "Tchaikovsky" and in German "Tschaikowski").
   - The **change over time** of an entity's name can be documented by aliases (e.g. `Carnegie Hall <https://musicbrainz.org/place/68b175f6-242d-40db-a376-ca0e2dd10c41>`_ was known as "Music Hall" from 1891 to 1893).
   - The **legal name** of an artist who normally performs under a stage name can be documented by an alias, among other methods (e.g. `Lady Gaga <https://musicbrainz.org/artist/650e7db6-b795-4eb5-a702-5ea2fc46c848>`_'s legal name is Stefani Joanne Angelina Germanotta).

A normal user can add aliases to :doc:`artists </terminology/entities/artist>`, :doc:`events </terminology/entities/event>`, :doc:`labels </terminology/entities/label>`, :doc:`places </terminology/entities/place>`, :doc:`recordings </terminology/entities/recording>`, :doc:`releases </terminology/entities/release>`, :doc:`release groups </terminology/entities/release_group>`, :doc:`series </terminology/entities/series>` and :doc:`works </terminology/entities/work>`, whereas only privileged users may add aliases to :doc:`areas </terminology/entities/area>` and :doc:`instruments </terminology/entities/instrument>`.

Except for search hints, each alias can be paired with extra information. For example, you can set a locale to reflect the area in which an alias is used. If possible, you should also set the start and end dates for an alias, indicating when the alias came into use and was it was abandoned. You can also supply a sort name, which is used in place of the alias's primary name when sorting.


Guidelines
----------

For guidance on style, please see the :doc:`guidelines for aliases </style_guides/aliases>`.


Alias types
-----------

Aliases come in two main types: {entity} name and search hint. For example, aliases for a work can either be a work name or a search hint. {Entity} name aliases show how people refer to the entity. Search hints are mainly used for common misspellings, name variants with different encoding and other correct ways of displaying the entity's name.

Unlike other entities, artists can be assigned three types of aliases: artist name, legal name and search hint. Please see the :doc:`artist guidelines </style_guides/artist>` on the difference between an artist name and a legal name. Another exception is instruments, which can be assigned a brand name alias besides an instrument name alias or a search hint.

Aliases can also be an unspecified type. These should be used sparingly and be assigned only when you are unsure of the alias type entered. If you see an unspecified-type alias, please try to assign it to another type after doing research on it.


When to use aliases
-------------------

Using aliases is appropriate in many cases:

   #. Misspellings:
         These are the most common use cases. They function as a simplistic automatic spelling corrector and should be entered as a search hint. Example: *Led Zepplin* = `Led Zeppelin <https://musicbrainz.org/artist/678d88b2-87b0-403b-b63d-5da7465aecc3>`_

   #. Variants:
         An entity may have similar names that are used interchangeably, without a clear rule indicating which name is used in which cases. These should be entered as an entity name, not as search hints. Examples: *Hootie and the Blowfish* = `Hootie & the Blowfish <https://musicbrainz.org/artist/b3120863-d98d-4bad-a637-8abd8cde6685>`_; *ESP* = `ESP-Disk’ <https://musicbrainz.org/label/8f200b94-5233-432a-9d7a-6347577dfc09>`_

   #. Numbers:
         Even if there is a preferred option (spelled out or in numerical form), an entity name with numbers may or may not be spelled out by users. These should be entered as entity names. Examples: *The 3 Tenors* = `The Three Tenors <https://musicbrainz.org/artist/986ff361-7c8d-4662-8bfc-5a01da5f09ed>`_; *Six Sonatas, op. 3* = `6 Sonatas, op. 3 <https://musicbrainz.org/work/617ead5a-6eaa-403e-b8cb-f7551a1ced14>`_

   #. Stylized Names:
         Many artists feel a need to spell their names or the names of their songs with strange spacing, odd characters and punctuation, etc. Example: *NSync* = `'N Sync <https://musicbrainz.org/artist/603ba565-3967-4be1-931e-9cb945394e86>`_

   #. Missing Titles:
         Titles, monikers and/or articles are usually added/dropped from entities' names. Examples: *The Sex Pistols* = `Sex Pistols <https://musicbrainz.org/artist/e5db18cb-4b1f-496d-a308-548b611090d3>`_; *Tiësto* = `DJ Tiësto <https://musicbrainz.org/artist/aabb1d9f-be12-45b3-a84d-a1fc3e8181fd>`_; *End of the World* = `The End of the World <https://musicbrainz.org/work/b3b0060d-94b7-30b6-bedb-e56f325c28b1>`_

   #. Acronyms:
         Artists and labels with long and unwieldy names are often better known by their acronyms, which may be used on release covers. Examples: *B.D.P.* = *BDP* = `Boogie Down Productions <https://musicbrainz.org/artist/ff7466a5-c538-4d2b-8450-54f11b20f2f4>`_; *SME* = `Sony Music Entertainment <https://musicbrainz.org/label/9e6b4d7f-4958-4db7-8504-d89e315836af>`_

   #. Initials:
         Overlaps somewhat with acronyms, but there are sometimes middle initials not generally used in an artist's name. Example: *J.S. Bach* = `Johann Sebastian Bach <https://musicbrainz.org/artist/24f1766e-9635-4d58-a4d4-9413f9f98a4c>`_

   #. Lead Performers:
         Sting is a member of The Police; this is not a collaboration, and the band does not officially include his name in theirs, however compilations often list featured members explicitly by name in this way. Example: *Sting & The Police* = `The Police <https://musicbrainz.org/artist/9e0e2b01-41db-4008-bd8b-988977d6019a>`_

   #. Misencodings:
         Names entered in FreeDB using non-UTF-8 encodings; these are somewhat like typos, but in non-Unicode locales, these may in fact be more accurate than an automatic conversion from UTF-8. Note: due to a bug (`MBS-5193 <https://tickets.metabrainz.org/browse/MBS-5193>`_), badly encoded aliases cannot be set at the moment. Example: *©PªN­Û­* = `Jay Chou <https://musicbrainz.org/artist/a223958d-5c56-4b2c-a30a-87e357bc121b>`_

   #. Localization:
         While English speakers are used to "Tchaikovsky", that is not the composer's native name. He is known elsewhere in the world by different spellings. This is also relatively common with labels and work names. In these cases, an alias locale should be added to indicate the language the alias is written in. Examples: *Pyotr Ilyich Tchaikovsky* (EN) and *Piotr Ilitch Tchaïkovski* (FR) = `Пётр Ильич Чайковский <https://musicbrainz.org/artist/9ddd7abc-9e1b-471d-8031-583bc6bc8be9>`_; *Music for Chamber Orchestra* = `Muusika kammerorkestrile <https://musicbrainz.org/work/1d07b69e-18ce-45e2-ba7b-58476e8c54f5>`_

   #. Transliterations:
         There are often several ways to transliterate non-Roman characters according to different standards. Example: *Jay Chow* = `Jay Chou <https://musicbrainz.org/artist/a223958d-5c56-4b2c-a30a-87e357bc121b>`_

   #. "Translated" Names:
         Many Asian artists have English names in addition to their given names in Chinese, Japanese, etc. In some cases, artists prefer their English name even in non-English text. Example: Chou Jie Lun = `Jay Chou <https://musicbrainz.org/artist/a223958d-5c56-4b2c-a30a-87e357bc121b>`_

   #. Legal Changes:
         Artists are often forced to change their names for legal reasons, sometimes only in part of the world. In this last case, an alias locale should be added to indicate in which countries the alternate name is used. Example: *Yaz* (EN-US) = `Yazoo <https://musicbrainz.org/artist/42922db2-2e80-44b8-9cdf-0b3a6634c124>`_


When not to use aliases
-----------------------

   #. Performance names:
         Before aliases and :doc:`artist credits </terminology/entities/artist_credit>` were available, performance names of an artist were entered separately in the database. Now, whether performance names should be entered as aliases or as a new artist depends on :ref:`artist intent <style_guides_principles_artist_intent>`. For example, `Snoop Dogg <https://musicbrainz.org/artist/f90e8b26-9e52-4669-a5c9-e28529c47894>`_'s side-project name `Snoop Lion <https://musicbrainz.org/artist/960db060-0ba8-4f6c-9770-49b81dc6e5ea>`_ requires a separate artist to be created, because Snoop Dogg has consistently used Snoop Lion for his side-project work. Please research into whether an artist intends for a separate persona to be created. Also see the :ref:`relevant guideline <style_guides_artist_performance_names_and_legal_names>` for more information.

   #. Different imprints:
         Labels that change names, or different imprints by the same company (for example, `Sony Music Entertainment <https://musicbrainz.org/label/b54769e4-b75e-4f60-884a-c4714687bb4c>`_ and `Sony Classical <https://musicbrainz.org/label/10920823-9ed8-45d9-adb3-69fc22475ab0>`_), should be :doc:`entered as separate labels </relationships/label-label/label_rename>`.
