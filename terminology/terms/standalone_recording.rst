.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Standalone_Recording

Standalone Recording
====================

Standalone recordings (previously called non-album tracks) are :doc:`recordings </terminology/entities/recording>` which are not linked to a :doc:`release </terminology/entities/release>`. To enter one, just use the "Add recording" link from an artist page or the Edit menu.

Standalone recordings shouldn't be used as a dumping ground for "dodgy internet sourced mp3s". To help prevent this, an :doc:`edit note </terminology/terms/edit_note>` is always required when adding a standalone recording.

When to use standalone recordings
---------------------------------

Although the :doc:`Style Guidelines </style_guides/recording>` don't spell this out explicitly there are a few valid reasons for creating a standalone recording:

**Internet-only release**
    Often, before an album is released, songs from the album may be available on an internet site for download, and may be entered as standalone recordings. Less frequently, some such songs are available for download, but are never included in any album or compilation.

**Tracks captured from broadcast performance**
    A song may be performed as part of a TV or radio show or other non-concert performance; tracks captured from these events may be entered as standalone recordings if they are not part of any live album or bootleg compilation.

**Multiple songs in one track**
    If multiple songs share one track (one after another, possible separated by long silence or noise), it is recommended to add additional standalone recordings for each of them, except when the recording exists as distinct track on another release. It is required to link each of the distinct recordings to the combined recording using :doc:`compilation relationships </relationships/recording-recording/compilation>`. For the duration of the new standalone recordings, try to find a popular source (Last.fm, bootleg download, etc.).

When not to use standalone recordings
-------------------------------------

Conversely, there are some cases that should not use standalone recordings, even though it might seem applicable:

**MP3 CD-ROM collections**
    If a number of songs are released as MP3 files on a CD-ROM rather than as an audio disc; these should be entered as normal releases. If there is no explicit track order in the filenames, they should be listed in alphabetical order as that is how most MP3 CD-ROM capable players will play them.

**Track "99"**
    :doc:`Hidden tracks </terminology/terms/hidden_track>` which *are* separate tracks, but are preceded by dozens of short tracks of **[silence]** can and should be listed as tracks of the release, e.g. `Broken <https://musicbrainz.org/release/9c0b5a23-ca6e-4b4e-be2f-98280cf56c88>`_ by Nine Inch Nails

**Pregap (track 0) tracks**
    These are now supported and should be entered as part of the release. There is a `list of releases with pregap tracks <https://musicbrainz.org/doc/Releases_With_Pregap_Tracks>`_ which need fixing.

Other recommendations
---------------------

Finally, there are some other recommendations for use of standalone recordings:

**Use the disambiguation field**
    Since standalone recordings don't have release dates or other information associated with them, adding information like "(live, 2002-05-13: Radio One)" is very helpful. Using titles like "[untitled]" or "[unknown]" without adding a disambiguation is sure to get the recording voted down or removed.

**Submit fingerprints**
    Standalone recordings with associated :doc:`AcoustIDs </terminology/terms/acoustid>` are much more helpful, since they cannot be matched by track number or disc ID, and matching by track name only is usually quite hard. If you have an MP3 or other sound file for your standalone recording, tagging your file with :doc:`MBIDs </terminology/terms/mbid>` is only half the work; it's much better if you also submit the fingerprint to the MusicBrainz database so that the entry is more useful to others.

**Link to a download or streaming source**
    If a direct download (e.g. from the artist's website) or stream (e.g. from Soundcloud) is available, it should be linked to the recording with a :doc:`relationship </relationships/relationships>`. They are not only the best proof for the recording's existence when adding it, but also the best documentation as to where it's from.