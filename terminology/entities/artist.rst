.. MusicBrainz Documentation Project

.. https://wiki.musicbrainz.org/Artist

Artist
======

An artist is generally a musician (or musician persona), group of musicians, or other music professional (like a producer or engineer). Occasionally, it can also be a non-musical person (like a photographer, an illustrator, or a poet whose writings are set to music), or even a :doc:`fictional character </terminology/terms/fictional_character>`. For some other special cases, see :ref:`special purpose artists <style_unknown_and_untitled_special_purpose_artist>`.


Examples
--------

   - `Coldplay <https://musicbrainz.org/artist/cc197bad-dc9c-440d-a5b5-d52ba2e14234>`_
   - `Snoop Dogg <https://musicbrainz.org/artist/f90e8b26-9e52-4669-a5c9-e28529c47894>`_
   - `John Williams <https://musicbrainz.org/artist/53b106e7-0cc6-42cc-ac95-ed8d30a3a98e>`_ (soundtrack composer & conductor)
   - `John Williams <https://musicbrainz.org/artist/8b8a38a9-a290-4560-84f6-3d4466e8d791>`_ (classical guitar player)
   - `Pink Floyd <https://musicbrainz.org/artist/83d91898-7763-47d7-b03b-b92132375c47>`_
   - `Seattle Symphony <https://musicbrainz.org/artist/0b51c328-1f2b-464c-9e2c-0c2a8cce20ae>`_
   - `Bill Porter <https://musicbrainz.org/artist/86437518-fca1-4117-b698-b371b72d76a5>`_


Style guidelines
----------------

Please see the :doc:`guidelines for artists </style_guides/artist>`.


Artist properties
-----------------

**Name**

The official name of an artist, be it a person or a band.

**Sort name**

The sort name is a variant of the artist name which would be used when sorting artists by name, such as in record shops or libraries. Among other things, sort names help to ensure that all the artists that start with "The" don't end up up under "T". The :ref:`guidelines for sort names <style_guides_artist_sort_name>` are the best place to check for more specific usage info.

**Type**

The type is used to state whether an artist is a person, a group, or something else.

   **Person**
      This indicates an individual person.

   **Group**
      This indicates a group of people that may or may not have a distinctive name.

   **Orchestra**
      This indicates an orchestra (a large instrumental ensemble).

   **Choir**
      This indicates a choir/chorus (a large vocal ensemble).

   **Character**
      This indicates an individual fictional character.

   **Other**
      Anything which does not fit into the above categories.

Note that not every ensemble related to classical music is an orchestra or choir. The `Borodin Quartet <https://musicbrainz.org/artist/598063d1-1fc6-496a-8e91-2c21c38d8c92>`_ and `The Hilliard Ensemble <https://musicbrainz.org/artist/c8db3d2b-19d8-4dc7-b2cb-deea37aa274a>`_, for example, are simply groups.

**Gender**

The gender is used to explicitly state whether a person or character identifies as male, female or neither. Groups do not have genders.

**Area**

The artist area, as the name suggests, indicates the area with which an artist is primarily identified with. It is often, but not always, its birth/formation country.

**Begin and end dates**

The begin and end dates indicate when an artist started and finished its existence. Its exact meaning depends on the type of artist:

   **For a person**
      Begin date represents date of birth, and end date represents date of death.

   **For a group (or orchestra/choir)**
      Begin date represents the date the group first formed, and the end date represents the date when the group last dissolved.

   **For a character**
      Begin date represents the date (in real life) when the character concept was created. The end date should not be set. These fields do not hold fictional birth and death dates.

   **For others**
      These fields are currently undefined for artists of the type Other.

**IPI code**

An IPI (interested party information) code is an identifying number assigned by the CISAC database for musical rights management. See :doc:`IPI </terminology/terms/ipi>` for more information, including how to find these codes.

**ISNI code**

The International Standard Name Identifier for the artist. See :doc:`ISNI </terminology/terms/isni>` for more information.

**Alias**

Aliases are used to store alternate names or misspellings. For more information and examples, see the :doc:`page about aliases </terminology/terms/alias>`.

**MBID**

See the :doc:`page about MBIDs </terminology/terms/mbid>` for more information.

**Disambiguation comment**

See the :doc:`page about comments </terminology/terms/disambiguation>` for more information.

**Annotation**

See the :doc:`page about annotations </terminology/terms/annotation>` for more information.


Additional information
----------------------

   - :doc:`How to add an artist </how-tos/add_artist>`
   - :doc:`How to use artist credits </how-tos/artist_credits>`
   - :doc:`How to split artists </how-tos/split_artists>`
   - :doc:`How to merge artists </how-tos/merge_artists>`
