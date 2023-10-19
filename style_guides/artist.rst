.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Style/Artist

Artist
======

Status: **Official Style Guideline**

.. _style_guides_artist_name:

Name
----

The artist name is the official name of an artist, whether it is a person, band, or character. In most cases, it is the name as found on releases.

Note that you can change how an artist is credited on a release or track when you enter that release. There is usually no need to add a new artist to the database if the artist is already present in our database under a (slightly) different name.

Keep in mind MusicBrainz is an international site, and "official name" doesn't necessarily mean "most common English name". For example, the "official name" for the Japanese composer `Tōru Takemitsu <https://musicbrainz.org/artist/4e871dff-df89-45f5-857f-28067cdc9d5e>`_ is "武満徹", not "Tōru Takemitsu" (which is the primary English alias instead).

**Definite articles and titles**

Only include `definite articles <https://wikipedia.org/wiki/wikt:definite_article>`_ (like "The", "El" or "Der") and honorary titles (like "Sir" or "MBE") if they're actually used by the artist as part of its name. If it's not clear, leave them out, and just add them to the :doc:`artist credit </style_guides/artist_credits>` when printed.

   - `Glenn Miller Orchestra <https://musicbrainz.org/artist/ce8cacb6-c917-41f5-b403-8fb601c89e70>`_ doesn't have an article on their official name (but `In the Nutcracker Mood <https://musicbrainz.org/release/5b45204b-5de5-4192-a416-fd73dd1e2ca2>`_ is credited to "The Glenn Miller Orchestra").

   .. newline between bullets

   - `Paul McCartney <https://musicbrainz.org/artist/ba550d0e-adac-4864-b88b-407cab5e76af>`_ has been knighted. He doesn't usually perform or record as "Sir Paul McCartney", so "Sir" shouldn't be part the artist name (but he is credited as "Sir Paul McCartney" in `A Garland for Linda <https://musicbrainz.org/release/592302f9-09a8-4309-9113-9965cd6350e0>`_).

.. _style_guides_artist_performance_names_and_legal_names:

**Performance names and legal names**

Generally, use the name the artist mainly performs under as the artist name. Alternative names, including any legal names and name variations, should generally be entered as :doc:`aliases </terminology/terms/alias>`, and can be used in artist credits and relationship credits when appropriate.

   - `The Prodigy <https://musicbrainz.org/artist/4a4ee089-93b1-4470-af9a-6ff575d32704>`_ have an alias of (and some releases credited to) "Prodigy".
   - `t.A.T.u. <https://musicbrainz.org/artist/7c20f558-d664-42bd-b6f1-81acf9dbb72d>`_ were originally known as "Тату" in Russia (they later used "t.A.T.u." everywhere).
   - `Yazoo <https://musicbrainz.org/artist/42922db2-2e80-44b8-9cdf-0b3a6634c124>`_ are known as "Yaz" in the USA after a lawsuit from another American artist called Yazoo.

In some cases, a person (or, more rarely, a group) can perform under multiple names that they actually consider different projects, and not just alternative names. In that case, you should add each artist separately. If they're a person, a separate legal name artist should be added, and linked to all performance names with the :doc:`is person ("performs as") </relationships/is_person>` relationship. In this case, do not add legal name aliases to the performance names. If the legal name is not known but it is known that several performance names refer to the same artist, you can instead choose one performance name and link all other performance names to it. For groups, just link each group to their members.

   - `Tomoko Kawase <https://musicbrainz.org/artist/a343493e-42f5-47cf-9ccf-9f399aafbe10>`_ performs under two different personas, with different styles: `Tommy february⁶ <https://musicbrainz.org/artist/ec53333e-2067-44ba-8222-79a40cbef550>`_ and `Tommy heavenly⁶ <https://musicbrainz.org/artist/02b99ce4-adae-474b-bd30-37a00e0af272>`_.
   - `Calvin Broadus <https://musicbrainz.org/artist/965f5705-6eb1-49a1-b312-cd3d65bcc7c9>`_ is most known as `Snoop Dogg <https://musicbrainz.org/artist/f90e8b26-9e52-4669-a5c9-e28529c47894>`_, but has a reggae side project, `Snoop Lion <https://musicbrainz.org/artist/960db060-0ba8-4f6c-9770-49b81dc6e5ea>`_.

**Trans artists**

If a trans artist changes their performance name to match their gender, always use the current name, not a deadname, as the artist name (even if more releases exist under the deadname at the time of the edit).

.. _style_guides_artist_sort_name:

Sort name
---------

See the guideline for :doc:`sort names </style_guides/artist_sort_name>`.

.. _style_guides_artist_disambiguation:

Disambiguation comment
----------------------

Disambiguation comments should be short but informative. See more at :doc:`Disambiguation Comment </terminology/terms/disambiguation>`.

.. _style_guides_artist_area:

Area
----

**Main area**

For people, use the country where they were born and raised. For groups, use the country where the band was formed. For characters, use the country where the character was created. If the artist is predominantly active in a different country, use that country instead.

   - `Michael Jackson <https://musicbrainz.org/artist/f27ec8db-af05-4f36-916e-3d57f91ecf5e>`_ has the area `United States <https://musicbrainz.org/area/489ce91b-6658-3307-9877-795b68554c98>`_.
   - `The Beatles <https://musicbrainz.org/artist/b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d>`_ have the area `United Kingdom <https://musicbrainz.org/area/8a754a16-0027-3a29-b6d7-2b40ea0481ed>`_.

If an artist is most commonly associated with an area smaller than a country, select that instead.

   - `Berliner Philharmoniker <https://musicbrainz.org/artist/dea28aa9-1086-4ffa-8739-0ccc759de1ce>`_ has the area `Berlin <https://musicbrainz.org/area/c9ac1239-e832-41bc-9930-e252a1fd1105>`_.
   - `Mobb Deep <https://musicbrainz.org/artist/d75d1f08-bbb8-4eae-9877-399ca9121197>`_ have the area `Queensbridge <https://musicbrainz.org/area/675bbb61-a94a-4b54-9242-1fbf81a46ee6>`_.

**Begin and end area**

Use as precise an area as you can (city or region are better than just country). Remember for people this means birth and death locations, rather than where they started their career.

   - `John Lennon <https://musicbrainz.org/artist/4d5447d7-c61c-4120-ba1b-d7f471d385b9>`_ was born in `Liverpool <https://musicbrainz.org/area/c249c30e-88ab-4b2f-a745-96a25bd7afee>`_ and died in `Manhattan <https://musicbrainz.org/area/261962ea-d8c2-4eaf-a80c-f14376ffadb0>`_.

.. _style_guides_artist_gender:

Gender
------

Use the gender the artist identifies as. Use "non-binary" if the artist identifies as something other than "male" or "female". Also use "non-binary", as the widest option, for anything that would seem to require more than one gender, since that is not currently possible (e.g. "non-binary trans woman").

For characters, the fictional gender of the character should be used. This might not match the gender of a person who performed the character.

The "non-binary" gender is not intended for use with entities for which the concept of gender is illogical, such as companies. For those, use "Not applicable".

The "other" gender option is deprecated and should not be used.

.. _style_guides_artist_alias:

Aliases
-------

See the :doc:`guidelines for aliases </style_guides/aliases>`.
