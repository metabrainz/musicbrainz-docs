.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Style/Classical/Works

Works
=====

Definition of a classical work
------------------------------

Any original classical works can be added to MusicBrainz (for arrangements, see the "Arrangement works" section below). Lost or fragmentary works can be entered, but this should be indicated in the work annotation.


**Work boundaries**

Works should be entered into MusicBrainz using the boundaries decided by the composer, as printed in the score.

   **Note:** Do not split a musical entity into smaller pieces based on track splits, tempo markings, lyrics or other information. E.g. the fourth movement of Beethoven's ninth symphony contains many musically different sections, and is often spread out over several tracks, but it is still only a single work.


**Collections**

Sometimes works are published in "collections". This is common for songs and shorter instrumental pieces, but can also happen with larger works like piano sonatas. These works can be interesting to have as "containers", but should not be treated as a main work with parts (for instance regarding Recording titles).

   **Note:** In general you should only add a collection if the composer was involved. Do not enter things like "All piano sonatas by Beethoven" as works in MusicBrainz.


**Stage music**

   **Note:** The overture is usually not part of the first act. The structure will be: Overture is a part of Main work, and then Act is a part of Main Work.


**Ballet**

Note that in ballet music, as opposed to opera (see below), a "scene" is a distinct work. Also note that scenes can be combined with numbers in different ways; some works have numbered scenes (e.g. "Scene 2"), while others have numbers titled "scene" (e.g. "No. 2. Scene").


**Opera**

The recommended structure for opera is: Number is a part of Act is a part of Opera (naturally Number and Act are optional).

In unnumbered operas (Wagner, for instance), sometimes an act is the smallest entity you can enter. See "excerpts" below for how to deal with popular arias and choruses.

   **Note:** In opera, "scenes" are instructions about who appears on stage (e.g. "Don Giovanni. Zerlina"), and/or what should take place (e.g. "Kurwenal enters boisterously through the curtains"). A scene is not an independent work in an opera. Furthermore, scenes can change completely independent of the music, sometimes several times during a single number. In general you should not create "scene works" as a container for numbers.


Different versions
------------------

If a work has specific versions, make sure that there is also a generic "catch-all" version available. Editors will not always be able to identify which specific version is performed. Until we have a better way of marking these "catch-all" works, it is recommended that you write something like "catch-all work" in the disambiguation field. For example, `Mahler's 10th symphony <https://musicbrainz.org/work/eff9bd21-8ba3-4a16-832b-d241c280ed8a>`_ has several different reconstructions and completions, so it also has a `"catch-all for unknown versions" work <https://musicbrainz.org/work/ce9ab8fa-3d7b-409a-bd1b-22f49fd0688a>`_.

   **Note:** Do not edit an existing work to become a specific version, add a new work instead.


**Revisions**

Different revisions of a work by one single composer. The most common case is when an earlier work is edited for a performance some years later.


**Arrangement works**

For written (and published) arrangements of another work. Here "arranging" is defined as changing the harmonies in the music, and/or rewriting the work for a different type of ensemble, for example from piano and soloist to orchestra. Transposing is not arranging.

Do not create a new work for improvised arrangements, "head-arrangements", private / unpublished arrangements or when the arranger is unknown. For an arrangement to be valid as a unique work in MusicBrainz, it must be possible for other performers to record new versions. There must be at least two different recordings available. The recordings must be of different performances by two different (groups of) performers. You must be able to source that the both performances use the exact same arrangement. If in doubt, do not create a new work.

For every other case, use the recording - artist arranger relationship.

   **Note:** Works can always be performed with different instrumentation than indicated in the score, and solo parts can be supplied for different instruments or voice ranges. This does not merit a new work.

   **Note:** Usually the arranger will not be given composer credit for the arrangement work, but exceptions do exist. Follow the general praxis.


**Translated lyrics**

A translation of a work should always imply a new work, since both the lyrics language information and the translator relationship would not apply to the original work. These translation works should be linked to the original with the "translated version" relationship. Keep the composer and lyricist/librettist of the original work.

If a work has been translated into the same language multiple times, a new work should be created for each translation. If you can't find which translation a recording is using, consider adding a new work, with a disambiguation like "unknown English translation".


**Completion and restoration**

When a work is completed or restored by a different composer than the original, usually both composers get composition credits. Use the composer relationship with the attribute "additional" for the composer who completed the work, and the reconstructed by relationship for reconstruction/restoration.


Linking recordings to works
---------------------------

It is possible that you have found the correct works to link to your recordings, but it is not an exact match. This is usually solved with the performance AR. If the recording contains more than one work, link to all performed works. If the recording contains just a part of a work, use the "partial" attribute.

There are however some cases that can be treated differently:

**Complete multi-part works**

If a multi-part work is presented as a single recording, you can link the recording to the "container" work, instead of linking to every sub-part.

**Menuet I - Menuet II etc.**

Strictly speaking these works are a single musical entity, but if the "second part" is often recorded as a standalone piece, it can have its own work.

   **Note:** Do not routinely create split works. This is most common for instrumental solo works.

**Excerpts**

If a sub-part of a larger work is performed regularly as a standalone piece, you can add it as a work. It is recommended that you write "Excerpt from [Work]" in the disambiguation field.

   **Note:** Do not add more than one work per excerpt. For instance, there should be only one "Ode to Joy" from Beethoven's ninth symphony, even if the amount of bars from the symphony that are actually performed differs between individual recordings. Likewise an opera aria is only one excerpt work, any recitatives are regarded as included in that work.
