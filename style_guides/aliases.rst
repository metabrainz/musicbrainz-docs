.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Style/Aliases

Aliases
=======

Status: **Official Style Guideline**

Localised names
---------------

The locales should be used to indicate an alias is a name used for an entity in a particular language and/or country. The main alias for each locale (the most recent one, or the most common if otherwise equivalent) should be marked as primary.

The locale should not be more specific than it needs to be, so the country should only be included when necessary, e.g. If an entity's name is the same in all English speaking countries, "English" with no country is sufficient. If the name is normally the same, but is different (usually for legal reasons) in certain countries, then the country should only be used to identify where the name is different from the usual name for that language.

**Examples**

   - `Пётр Ильич Чайковский <https://musicbrainz.org/artist/9ddd7abc-9e1b-471d-8031-583bc6bc8be9>`_ is most often known as "Pyotr Ilyich Tchaikovsky" in English, so that's its primary English alias. Other names that see some use, like "Peter Tchaikovsky", are added as non-primary English aliases.

   .. newline between bullets

   - `The Beatles <https://musicbrainz.org/artist/b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d>`_ are known as "ザ・ビートルズ" in Japanese.

   .. newline between bullets

   - `Yazoo <https://musicbrainz.org/artist/42922db2-2e80-44b8-9cdf-0b3a6634c124>`_ are normally known as "Yazoo" in English, but are known as "Yaz" in English in the United States.


Sort name
---------

The sort name should be in the appropriate form for the alias locale, since different languages sort names differently (for example, use kana for Japanese sort names).

   - `Johann Sebastian Bach <https://musicbrainz.org/artist/24f1766e-9635-4d58-a4d4-9413f9f98a4c>`_ has the Russian alias "Иоганн Себастьян Бах", with the sort name "Бах, Иоганн Себастьян".

   .. newline between bullets

   - `日本武道館 <https://musicbrainz.org/place/4d43b9d8-162d-4ac5-8068-dfb009722484>`_ (Nippon Budokan) has the Japanese alias "日本武道館", with the sort name "にっぽんぶどうかん"

For artists, aliases should follow the normal :doc:`artist sort name guidelines </style_guides/artist_sort_name>`.

In most cases, sort names for non-artist aliases should be the same as the entity name, with the following exceptions:

Articles (e.g. "the", "a" and equivalents in other languages) at the beginning of the name should be moved to the end, separated by ", " (comma and space).

   - The sort name for `The Electric Record Company <https://musicbrainz.org/label/c1da9ced-1d50-42ac-9c28-b2561362cc3f>`_ is "Electric Record Company, The"

Stylised characters (e.g. the use of symbols like "$" to represent "s") should be changed to the letters they represent (but diacritics should not be removed).

   - The sort name for `Sm:)e Communications <https://musicbrainz.org/label/0a49c20c-984f-4142-a318-66dac1876c05>`_ is "Smile Communications"


Deadnames
---------

Do not add `deadnames <https://wikipedia.org/wiki/Deadnaming>`_ as artist aliases unless they have specifically been used as credits in the artist's music and as such are needed to identify who an old credit in a release is referring to. Deadnames that do not fulfill an explicit need should be removed.
