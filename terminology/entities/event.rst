.. MusicBrainz Documentation Project

.. https://wiki.musicbrainz.org/Event

Event
=====

An event refers to an organised activity that people can attend, and is relevant to the performance, production or celebration of music. In most cases, this means live concerts, festivals and other similar activities.

Examples
--------

   - `BOB goes Matrix <https://musicbrainz.org/event/d801c6c8-7870-4506-9709-af3890bf1e74>`_
   - `Glastonbury Festival 2010 <https://musicbrainz.org/event/157fc8ff-5638-48b0-99b6-fc0f33ef63e0>`_
   - `コミックマーケット65 <https://musicbrainz.org/event/10b5e28b-95f5-482e-9524-c51be37f943d>`_


Style guidelines
----------------

Please see the :doc:`guidelines for events </style_guides/event>`.


Event properties
----------------

**Name**

The name is the official name of the event if it has one, or a descriptive name (like "Main Artist at Place") if not.

**Type**

The type describes what kind of event the event is. The possible values are:

   **Concert**
      An individual concert by a single artist or collaboration, often with supporting artists who perform before the main act.

   **Festival**
      An event where a number of different acts perform across the course of the day. Larger festivals may be spread across multiple days.

   **Stage performance**
      A performance of one or more plays, musicals, operas, ballets or other similar works for the stage in their staged form (as opposed to a `concert performance <https://en.wikipedia.org/wiki/Concert_performance>`_ without staging).

   **Award ceremony**
      An event that is focused on the granting of prizes, but often includes musical performances in between the awarding of said prizes, especially for musical awards.

   **Launch event**
   A party, reception or other event held specifically for the launch of a release.

   **Convention/Expo**
      A convention, expo or trade fair is an event which is not typically orientated around music performances, but can include them as side activities.

   **Masterclass/Clinic**
      A masterclass or clinic is an event where an artist meets with a small to medium-sized audience and instructs them individually and/or takes questions intended to improve the audience members' playing skills.

**Cancelled**

The cancelled field describes whether or not the event took place.

**Setlist**

The setlist stores a list of songs performed, optionally including links to artists and works. See the :doc:`setlist documentation </how-tos/add_event_setlist>` for syntax and examples.

**Begin and end dates**

The begin and end dates indicate when an event started and finished.

**Time**

The time is the start time of the event.

**Alias**

Aliases are alternate names for an event, which currently have two main functions: localised names and search hints. Localised names are used to store the official names used in different languages and countries. These use the locale field to identify which language or country the name is for. Search hints are used to help both users and the server when searching and can be a number of things including alternate names, nicknames or even misspellings.

**MBID**

See the :doc:`page about MBIDs </terminology/terms/mbid>` for more information.

**Disambiguation comment**

See the :doc:`page about disambiguation comments </terminology/terms/disambiguation>` for more information.

**Annotation**

See the :doc:`page about annotations </terminology/terms/annotation>` for more information.
