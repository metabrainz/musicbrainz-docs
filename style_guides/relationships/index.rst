.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Style/Relationships

Relationships
=============

Status: **Official Style Guideline**

This page outlines general guidelines that should be followed when adding :doc:`relationships </relationships/relationships>`. Many relationships also have their own guidelines which, should they conflict, supersede the ones on this page.

For relationships which link an entity to a URL, see the :doc:`URL guidelines </style_guides/relationships/url>` as well.

For assistance in determining the correct relationship types to use when describing compiling, DJ mixing, mastering, mixing, remastering, remixing and sampling, please refer to :ref:`Mix Terminology <terminology_mix_terminology>`.

Prefer most specific level
--------------------------

Often a relationship could be added at multiple levels. For example, the liner notes on a release can just say "violin: Artist X", or "recorded at the 1988 Foo Festival, Bar Concert Hall, Baz City". You should always prefer the most specific level that you can, and avoid adding redundant relationships.

If you have a relationship that applies to an event, always link to the event, not the place nor the area (nor to any series of events the event might be part of).

If you have a relationship that applies to a series of events (for example, the data for a recording only says it was recorded at "Foo Festival", but not which year), link to the series.

   - If the series of events has always happened in the same place (for example, a run of concerts in a specific venue), do not link to the place nor the area, since that is already known by the series (do make sure the series is already linked to the place/area and add that data if not).

   .. newline between bullets

   - If the series of events moves around (such a tour) and you are given the place or area this specific recording was recorded at, but you still do not have enough data to create a specific event, you can also link to the place, since that is not redundant. For example, if all you know is "Recorded at Venue X during Tour Y" and the tour had more than one concert at Venue X, you can link to both tour and venue. If there was only one concert, then you have all the data you need to link only to the concert itself.

If you have a relationship (such as performer) that is given at the release level in the liner notes:

   - If you know the relationship is applicable to all tracks on a release (for example, it's the only credited violinist in an album of solo violin pieces, or the only credited composer), apply it to every work or recording on the release, and do not apply it to the release itself.

   .. newline between bullets

   - If the relationship applies to only a few tracks, and you know which ones, apply it only to those works or recordings, and do not apply it to the release itself.

   .. newline between bullets

   - If you are unsure which tracks a relationship applies to, enter it at release level. A basic effort to determine to which tracks the relationship is applicable is appreciated, but do not guess if you can't figure it out with certainty.

   .. newline between bullets

   - If the credit is release level, and does not apply on a track by track basis (e.g. graphic design for the album's cover), then apply the relationship to the release, not the recordings or works.

If you find a relationship which is redundant, or that is set at a higher level than it can be discerned with the information you have, please fix it.


Personal and business relationships
-----------------------------------

It is not part of MusicBrainz' mission to capture all the aspects of the personal life of artists nor the economic life of the recording industry.

A person should **not** be added to the database only to allow a link to indicate that they went out with, were married to, or were related to an artist. The only exception is when a non-musical person can be connected to two or more artists, allowing those artists to indirectly be linked together.

Label entries should **not** be added solely to represent investors, share-holders, etc. Relationship types which would represent fine-grained ownership details (or the entire economic macrocosm) have not been created, and the existing relationship types should not be misused for the purpose.

While proposals for new relationships are always welcomed by the community, be forewarned that proposals which would add relationship types to allow tracking finer-grained personal details or company or economic details will face a greater degree of scrutiny.


Prefer specific relationship types
----------------------------------

You should try to make the relationship type as specific as possible. This means that you should avoid the generic types if:

   - the liner or another source specifies which of the subtypes apply, or
   - you can easily deduce which of the subtypes apply.

In these cases, you should use the specific relationship types, and omit a relationship of the generic type. If you feel the generic type is more appropriate (for example, if the evidence provides conflicting information, or if no specific information is available), then add your reasons and justification to the edit note and an annotation. This will help voters confirm your analysis and will make sure other editors are aware of the background when doing later edits.

**Generic types**

Here is a list of "generic types", and examples of preferred specific types:

   - Arranger: prefer "instrument arranger", "vocal arranger" and/or "orchestrator".
   - Engineer: prefer the subtypes of engineer ("audio", "mastering", "sound", "mix", "recording", "programming", "editor", "balance").
   - Performer: prefer the subtypes "instruments" and/or "vocal", "performing orchestra", "conductor", "chorus master", "concertmaster".

**Examples**

   - `Larry Luddecke <https://musicbrainz.org/artist/fe59ad15-3cd4-4f00-8a79-a0fe9b884dec.html>`_ recorded and mixed `Old Dogs <https://musicbrainz.org/release/c154a6fd-a3b7-4c64-a93e-abe3fd1de897>`_, as confirmed by the `author's website <http://www.acousticmusic.com/staines/olddogs.htm>`_. He is linked to the release with :doc:`Recording </relationships/artist-release/recording>` and :doc:`Mix </relationships/artist-release/mix>` relationships. No generic Engineer relationship is created.

   .. newline between bullets

   - `Mogwai <https://musicbrainz.org/artist/d700b3f5-45af-4d02-95ed-57d301bda93e>`_ wrote `I Know You Are but What Am I? <https://musicbrainz.org/work/03b84c40-beeb-4dd1-a1a7-4edc0c735f09>`_ . As this is an instrumental track, the writing credit clearly does not apply to any lyrics or libretto. Instead of a :doc:`Writer </relationships/artist-work/writer>` relationship, Mogwai are credited using a :doc:`Composer </relationships/artist-work/composer>` relationship.

   .. newline between bullets

   - `Mick Jagger <https://musicbrainz.org/artist/b5ffc3aa-b868-4b88-905f-d73d51dbe51c>`_ and `Keith Richards <https://musicbrainz.org/artist/f0ed72a3-ae8f-4cf7-b51d-2696a2330230>`_ wrote `You Got Me Rocking <https://musicbrainz.org/work/e3df1762-fac5-427d-bb02-b98716a553a8>`_. As their individual roles are unclear - one might have been primarily working on the lyrics, with the other writing the music - the :doc:`Writer </relationships/artist-work/writer>` relationship is used. Once more information becomes available, these can be replaced by :doc:`Composer </relationships/artist-work/composer>` and/or :doc:`Lyricist </relationships/artist-work/lyricist>` relationships.
