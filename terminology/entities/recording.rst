.. MusicBrainz Documentation Project

.. https://wiki.musicbrainz.org/Recording

Recording
=========

A recording is an entity in MusicBrainz which can be linked to :doc:`tracks </terminology/entities/track>` on :doc:`releases </terminology/entities/release>`. Each track must always be associated with a single recording, but a recording can be linked to any number of tracks.

A recording represents distinct audio that has been used to produce at least one released track through copying or :ref:`mastering <terminology_mix_terminology>`. A recording itself is never produced solely through copying or mastering.

Generally, the audio represented by a recording corresponds to the audio at a stage in the production process before any final mastering but after any editing or :ref:`mixing <terminology_mix_terminology>`.

The diagram below shows some examples of recorded audio, recordings and released tracks and the relationships between them:

.. image:: /images/Recordings_Helper_Diagram.svg
   :alt: Recordings Helper Diagram


Examples
--------

These are all different Recordings:

   - Studio recording: `Into the Blue <https://musicbrainz.org/recording/9ce76fe1-769f-481a-afbb-3b9b81c6f433>`_ by `Moby <https://musicbrainz.org/artist/8970d868-0723-483b-a75b-51088913d3d4>`_
   - Remixed recording: `Into the Blue (Beatmasters mix) <https://musicbrainz.org/recording/023b1e14-0e7e-4dc1-9ab4-9ef4f0e70ce0>`_ by `Moby <https://musicbrainz.org/artist/8970d868-0723-483b-a75b-51088913d3d4>`_
   - Studio recording: `Voulez-Vous <https://musicbrainz.org/recording/f449e449-503b-4ca4-967b-4aff18bc218e>`_ by `ABBA <https://musicbrainz.org/artist/d87e52c5-bb8d-4da8-b941-9f4928627dc8>`_
   - Live recording: `Voulez-Vous <https://musicbrainz.org/recording/d97813dc-a5fb-4ddb-b22e-7990cd253aae>`_ by `ABBA <https://musicbrainz.org/artist/d87e52c5-bb8d-4da8-b941-9f4928627dc8>`_


Style Guidelines
----------------

Please see the :doc:`guidelines for recordings </style_guides/recording>`.


Properties
----------

**Title**

The title of the recording.

**Artist**

The artist(s) that the recording is primarily credited to.

**Length**

The length of the recording. It's only entered manually for :doc:`standalone recordings </terminology/terms/standalone_recording>`. For recordings that are being used on releases, the recording length is the median length of all tracks (that have a track length) associated with that recording. If there is an even number of track lengths, the smaller median candidate is used.

**ISRC**

The :doc:`International Standard Recording Code </terminology/terms/isrc>` assigned to the recording.

**MBID**

See :doc:`MusicBrainz Identifier </terminology/terms/mbid>`.

**Disambiguation comment**

See :doc:`Disambiguation Comment </terminology/terms/disambiguation>`.

**Annotation**

See :doc:`Annotation </terminology/terms/annotation>`.
