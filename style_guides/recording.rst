.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Style/Recording

Recording
=========

Status: **Official Style Guideline**

.. _style_guides_recording_title:

Title
-----

The :doc:`recording </terminology/entities/recording>` title should generally be based on the titles of tracks using that recording:

   - If the recording has tracks from official releases, choose the most common title from official tracks as the basis for the recording title.
   - Otherwise, choose the most common track title.
   - For :doc:`standalone recordings </terminology/terms/standalone_recording>`, the title should be based on the title given by the original source.

For almost all recordings, :ref:`extra title information <style_guides_title_extra_title_information>` should be kept in the recording title. The exception is :ref:`live recordings <style_guides_recording_specific_types>`, where any performance information should be transferred to the disambiguation using the Live recordings guideline.

Examples:

   - The majority of the official tracks using the recording `…Baby One More Time <https://musicbrainz.org/recording/9aa77fa3-1a7d-4ff9-a5ce-8c3dc072fa52>`_ are called "…Baby One More Time", so the recording title should be "…Baby One More Time" and not "Baby One More Time" or "…Baby One More Time (radio version)".

   .. newline between bullets

   - The recording `Mailman, Bring Me More Blues <https://musicbrainz.org/recording/d0a7f90b-9d4f-4737-80ff-1f87704999f4>`_ is actually the song "Mailman, Bring Me No More Blues". But because there is only one track using the recording, the title of this track should be used as the recording title.


.. _style_guides_recording_artist:

Artist
------

The artist should usually be the same as in the track listing of the first release of the recording (see the section on :ref:`track artist <style_release_track_artist>` in the Release Guideline).

**Trans artists**

If a trans artist changes their performance name to match their gender and re-releases a release under said name, use that name, not a deadname, as the recording artist credit for recordings in that release (even if most releases list the recording under the deadname at the time of the edit).


.. _style_guides_recording_using_recordings:

Using recordings
----------------

In many cases, a released track will feature the original recording produced from a performance. However, there are some important cases to consider where this is not true - these are discussed in the following section.

**Different performances**

Different performances of the same work should always be given separate recordings, no matter how similar they may sound. This applies to both studio performances and live performances.

**Different sources**

Audio recordings of the same performance from different sources will always have different audio. A new MusicBrainz Recording should be created for each track created from different audio recordings.

**Remixes**

A group of audio tracks used in a recording can be mixed and possibly edited in a different way. For example, the volume or tone of individual tracks may be altered, or effects may be applied to them. The result is often labelled on a track list as a remix, mix, dub, overdub or version, and should always be given a new recording in MusicBrainz.

**Edits**

An existing recording can itself be edited to produce a new recording. For example, a "radio edit" or "single edit" may be produced by removing an intro or outro, verses, bridges or interludes to shorten the existing recording, and/or by censoring some of the content. Other examples include an edit using only a section of a recording or an "extended edit" which repeats parts of an existing recording to increase the duration.

Where a fade is added to the first or last section of an existing recording, this is not an edit, as the section is not removed.

**Number of audio channels**

It may be the case that very similar released tracks have different numbers of audio channels. The most common audio channel configuration is stereo (two channels; left and right). However, there are several common audio channel configurations used in recordings, including mono (one channel), quadraphonic (four channels) and surround sound (various multi-channel configurations).

These different configurations should generally be distinguished by using separate recordings. However, the original multi-channel recording should be used when multiple channels have been combined into a single channel without actually creating a new mix from the source audio tracks. A similar exception should be made where a mono channel has been split into two stereo channels - for example, in `Duophonic <https://wikipedia.org/wiki/Duophonic>`_ recordings.

**Video recordings**

A video recording (such an official music video for a studio track or a live video from a concert) should always be a different recording from any audio-only recording, even if the audio content is the same for both.


.. _style_guides_recording_merging_recordings:

Merging recordings
------------------

In addition to the above guidelines, it is extremely important to take the following into consideration when thinking of merging recordings.

**Recordings with different durations**

Recordings of different durations can be merged, as long as there is no evidence to suggest that differences in mixing or editing have caused the change in lengths.

Variations in the length of silence at either end of tracks is not a reason to keep recordings separate, since no changes have been made to the audio itself. Similarly, different volume fades at either end of multiple tracks are not reasons to maintain separate recordings - they are considered mastering differences unless they cause the structure of the song to change. The same is true for variations in playback speed between recordings.

**Recordings with different mastering**

As mentioned in :doc:`Recording </terminology/entities/recording>`, in MusicBrainz, mastering is a process that is applied to recordings to prepare them for release in a particular format. This means that tracks should not use separate recordings because of mastering differences.

Following on from this, separate recordings should not be created for remastered tracks, since remastered tracks generally feature the original recording with different mastering applied. Remastering should be described using the :doc:`remaster relationship type </relationships/remaster>` between releases, or in the release annotation where tracks are mastered differently across a release. The exception to this is where a track labelled as a remaster is in fact a remix - in this case, follow the remix guidelines above.

**Recordings with conflicting relationships**

Generally, don't merge recordings if they have conflicting relationships. However, if you're certain that two recordings are the same and relationships are wrong, merge the recordings and correct the relationships.


.. _style_guides_recording_specific_types:

Specific types of recording
---------------------------

**Live recordings**

For live recordings, enter the recording title as described in the :ref:`recording title <style_guides_recording_title>` guideline, and use "live" as the recording :doc:`disambiguation comment </terminology/terms/disambiguation>`. If the date and/or location is known, this should also be added to the disambiguation comment following the same format as used on :doc:`live bootlegs </style_guides/types_of_releases/_specific_types_of_releases>`.

Examples:

   - `Train in Vain <https://musicbrainz.org/recording/3a4fa843-ccfe-4f1d-8bd7-6f718bc5cbe7>`_ (live, 1998-12-14: Telewest Arena, Newcastle, UK)
   - `Wake Up <https://musicbrainz.org/recording/69d6f35a-806f-470c-aa09-363f74318c38>`_ (live, Los Angeles, CA, USA)
   - `The Dance <https://musicbrainz.org/recording/3f8c8e54-278d-4805-9365-af1b39dc56bb>`_ (live, 2002)
   - `Candle in the Wind (single edit) <https://musicbrainz.org/recording/1527433f-8e9a-45f4-a21e-947d64e8d293>`_ (live)


.. _style_guides_recording_examples:

Examples
--------

When `The Beatles <https://musicbrainz.org/artist/b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d>`_' studio albums were originally released as CDs in 1987, they were remastered from the original mixes with the exception of `Help! <https://musicbrainz.org/release-group/0d44e1cb-c6e0-3453-8b68-4d2082f05421>`_ and `Rubber Soul <https://musicbrainz.org/release-group/dca03435-8adb-30a5-ba82-5a162267ff38>`_, which were remixed. `A Day in the Life <https://musicbrainz.org/recording/17c75743-6fc2-4c72-8152-25c5b45dfea7>`_ is used on both the 1967 and the 1987 stereo releases of `Sgt. Pepper's Lonely Hearts Club Band <https://musicbrainz.org/release-group/9f7a4c28-8fa2-3113-929c-c47a9f7982c3>`_, while the `Yesterday <https://musicbrainz.org/recording/8aefa373-2858-4643-b691-cad4ac7c971a>`_ from the `original stereo release <https://musicbrainz.org/release/40825ca0-0568-3de0-bbe7-d5e07ed9a191>`_ of Help! is a different recording to the `Yesterday <https://musicbrainz.org/recording/c05194a3-f6f0-4f52-b78a-13fb5580bc0f>`_ remix from the `1987 CD release <https://musicbrainz.org/release/7c94c6f8-4c5b-3ad1-bfef-18cdf3fce009>`_.

The original recording `Don't Push <https://musicbrainz.org/recording/29d74a35-6058-4b2d-ba4b-0c93a28e6850>`_ appears on tracks which vary in length from 3:45 to 3:55 because they have been mastered at different speeds. Therefore, the pitch of the audio is different on these tracks, but because there is no difference in mixing they are considered the same recording. The album version, `Don't Push <https://musicbrainz.org/recording/0163ad9b-1e55-455b-8b8d-86a842420c4d>`_, appears on many releases at different levels of loudness, with differences in dynamic range and with different tonal qualities. However, again there is no evidence that this was the result of mixing and therefore these different tracks are one recording.

The tracks on the `1973 stereo edition <https://musicbrainz.org/release/b84ee12a-09ef-421b-82de-0441a926375b>`_ of `Pink Floyd <https://musicbrainz.org/artist/83d91898-7763-47d7-b03b-b92132375c47>`_'s `The Dark Side of the Moon <https://musicbrainz.org/release-group/f5093c06-23e3-404f-aeaa-40f72885ee3a>`_ all use different recordings to the `1973 quadrophonic edition <https://musicbrainz.org/release/b8ee4313-2915-40f1-913d-ac0315b4ba3d>`_ of the same album, since each version was mixed independently for different numbers of audio channels.

Four different studio recordings of the song `Punky Reggae Party <https://musicbrainz.org/work/b6c87eb3-db61-33ed-ac5e-26bd53aca788>`_ were released by `Bob Marley & The Wailers <https://musicbrainz.org/artist/c296e10c-110a-4103-9e77-47bfebb7fb2e>`_. The `B side of the 12" "Jamming" single <https://musicbrainz.org/recording/cfd90954-89a3-4d28-9537-808cd3a7b1c4>`_ and the `B side of the 7" "Jamming" single <https://musicbrainz.org/recording/9b664a0e-3e78-4d74-8ead-27f30d0c7ee5>`_ are shortened edits of the `A side of the 12" "Punky Reggae Party" single <https://musicbrainz.org/recording/e1b01ebe-da8f-4d42-a7b8-a83af503190e>`_, reducing the length of the original from 9:18 to 6:52 and 4:25 respectively. The `B side of the 12" "Punky Reggae Party" single <https://musicbrainz.org/recording/11b337fa-0d67-4a73-8f44-69aa55acd81c>`_ is a different mix, with many of the vocals removed and other effects applied during the mix.

`Glenn Gould <https://musicbrainz.org/artist/7002bf88-1269-4965-a772-4ba1e7a91eaa>`_ has performed and recorded at least two different interpretations of `Bach <https://musicbrainz.org/artist/24f1766e-9635-4d58-a4d4-9413f9f98a4c>`_'s `Goldberg Variations <https://musicbrainz.org/work/1d51e560-2a59-4e97-8943-13052b6adc03>`_. As these are two different performances, there is a separate recording for each; `the 1955 performance <https://musicbrainz.org/recording/7fb6932b-f2df-44f2-b0a6-e419c3aa429c>`_ and `the 1981 performance <https://musicbrainz.org/recording/4cf2bb2e-a4de-461c-905c-eb0c739fd6cc>`_. Although these recordings have similar lengths and relationships, they should definitely not be merged.
