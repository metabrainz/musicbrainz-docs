.. MusicBrainz Documentation Project

.. https://wiki.musicbrainz.org/Instrument

Instrument
==========

Instruments are devices created or adapted to make musical sounds. Instruments are primarily used in :doc:`relationships </terminology/entities/relationship>` between two other entities and for that, each instrument entity has a parallel :ref:`relationship attribute <entities_relationship_attribute>` with the same MBID. Instruments, like relationship attributes, can only be edited by :ref:`relationship editors <terms_editor_relationship_editor>`. See the `Instrument List <https://musicbrainz.org/instruments>`_ for the full list.


Examples
--------

   - `guitar <https://musicbrainz.org/instrument/63021302-86cd-4aee-80df-2270d54f4978>`_
   - `flute <https://musicbrainz.org/instrument/540280f1-d6cf-46bf-968b-695e99e216d7>`_
   - `erhu <https://musicbrainz.org/instrument/988026a0-2cb7-42bb-9407-9110874fa401>`_


Instrument properties
---------------------

**Name**

The instrument name is the name of the instrument, typically the most common name in English.

**Type**

The type categorises the instrument by the way the sound is created, similar to the `Hornbostel-Sachs <https://en.wikipedia.org/wiki/Hornbostel-Sachs>`_ classification. The possible values are:

   **Wind instrument**
      An `aerophone <https://en.wikipedia.org/wiki/Aerophone>`_, i.e. an instrument where the sound is created by vibrating air. The instrument itself does not vibrate.

   **String instrument**
      A `chordophone <https://en.wikipedia.org/wiki/Chordophone>`_, i.e. an instrument where the sound is created by the vibration of strings.

   **Percussion instrument**
      An `idiophone <https://en.wikipedia.org/wiki/Idiophone>`_, i.e. an instrument where the sound is produced by the body of the instrument vibrating, or a drum (most `membranophones <https://en.wikipedia.org/wiki/Membranophone>`_) where the sound is produced by a stretched membrane which is struck or rubbed.

   **Electronic instrument**
      An `electrophone <https://en.wikipedia.org/wiki/Electrophone>`, i.e. an instrument where the sound is created with electricity.

   **Family**
      A grouping of related but different instruments, like the different violin-like instruments.

   **Ensemble**
      A standard grouping of instruments often played together, like a string quartet.

   **Other instrument**
      An instrument which doesn't fit in the categories above.

**Description**

The description is a brief description of the main characteristics of the instrument.

**Alias**

Aliases are alternate names for an instrument, which currently have two main functions: localised names and search hints. Localised names are used to store the official names used in different languages and countries. These use the locale field to identify which language or country the name is for. Search hints are used to help both users and the server when searching and can be a number of things including alternate names, nicknames or even misspellings.

**MBID**

See the :doc:`page about MBIDs </terminology/terms/mbid>` for more information.

**Disambiguation comment**

See the :doc:`page about disambiguation comments </terminology/terms/disambiguation>` for more information.

**Annotation**

See the :doc:`page about annotations </terminology/terms/annotation>` for more information.
