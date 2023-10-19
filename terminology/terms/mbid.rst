.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/MusicBrainz_Identifier

MusicBrainz Identifier
======================

One of MusicBrainz' aims is to be the universal lingua franca for music by providing a reliable and unambiguous form of music identification; this music identification is performed through the use of MusicBrainz Identifiers (MBIDs).

In a nutshell, an MBID is a 36-character `Universally Unique Identifier <https://en.wikipedia.org/wiki/Universally_Unique_Identifier>`_ that is permanently assigned to each entity in the database, i.e. :doc:`artists </terminology/entities/artist>`, :doc:`release groups </terminology/entities/release_group>`, :doc:`releases </terminology/entities/release>`, :doc:`recordings </terminology/entities/recording>`, :doc:`works </terminology/entities/work>`, :doc:`labels </terminology/entities/label>`, :doc:`areas </terminology/entities/area>`, :doc:`places </terminology/entities/place>` and :doc:`URLs </terminology/entities/url>`. MBIDs are also assigned to :doc:`Tracks </terminology/entities/track>`, though tracks do not share many other properties of entities. For example, the artist `Queen <https://musicbrainz.org/artist/0383dadf-2a4e-4d10-a46a-e9e041da8eb3>`_ has an artist MBID of ``0383dadf-2a4e-4d10-a46a-e9e041da8eb3``, and their song `Bohemian Rhapsody <https://musicbrainz.org/recording/b1a9c0e9-d987-4042-ae91-78d6a3267d69>`_ has a recording MBID of ``b1a9c0e9-d987-4042-ae91-78d6a3267d69``.

An entity can have more than one MBID. When an entity is merged into another, its MBIDs redirect to the other entity.


Using MBIDs for disambiguation
------------------------------

MBIDs are used to disambiguate between entities that share the same name in the :doc:`MusicBrainz Database </musicbrainz_database/index>`.

For example, there are two popular artists with the name "John Williams":

   - `John Williams <https://musicbrainz.org/artist/53b106e7-0cc6-42cc-ac95-ed8d30a3a98e>`_, the soundtrack composer and conductor, has an artist MBID of ``53b106e7-0cc6-42cc-ac95-ed8d30a3a98e``
   - `John Williams <https://musicbrainz.org/artist/8b8a38a9-a290-4560-84f6-3d4466e8d791>`_, the classical guitar player, has an artist MBID of ``8b8a38a9-a290-4560-84f6-3d4466e8d791``

And there are two different singles titled "99 Red Balloons":

   - `99 Red Balloons <https://musicbrainz.org/release/189002e7-3285-4e2e-92a3-7f6c30d407a2>`_, the original by `Nena <https://musicbrainz.org/artist/c954d136-c7fd-4fd9-8bb0-fb0491fc6a02>`_, has a release MBID of ``189002e7-3285-4e2e-92a3-7f6c30d407a2``
   - `99 Red Balloons <https://musicbrainz.org/release/c9f91cdc-984e-4303-9a51-4ac0dfa2348f>`_, the cover by `Goldfinger <https://musicbrainz.org/artist/87fc1871-b74e-4bf5-a00d-8a89c288008b>`_, has a release MBID of ``c9f91cdc-984e-4303-9a51-4ac0dfa2348f``


Using MBIDs in applications
---------------------------

MBIDs play an important role when managing a digital music collection and there are several applications that are :doc:`MusicBrainz enabled </products/enabled_applications>`.

**Taggers**

Multiple MBIDs may be written to a file by a MusicBrainz enabled :ref:`tagger application <enabled_applications_taggers>`. They are commonly used to identify:

   - the recording itself
   - the release
   - the label
   - the track artist
   - the release artist

For more information, see the `tag documentation <https://picard-docs.musicbrainz.org/variables/variables.html>` and the `tag mappings <https://picard-docs.musicbrainz.org/appendices/tag_mapping.html>` of the MusicBrainz Picard tagger.


**Music players**

Music player applications can take advantage of a file that has been tagged with MBIDs to do things such as:

   - query the :doc:`MusicBrainz Database </musicbrainz_database/index>` for further information about the file or related entities
   - reliably search for related files based on a unique string, instead of by potentially ambiguous strings such as :doc:`artist name </terminology/entities/artist>` or :doc:`release title </terminology/entities/release>`


**Flickr**

See :doc:`Flickr Machine Tag </terminology/terms/flickr_machine_tag>` for information about adding MBIDs to photos on Flickr.


**Uniform Resource Identifier**

URIs can be constructed by prefixing the MBID with the address of the MusicBrainz server and the entity type, for example `Queen <https://musicbrainz.org/artist/0383dadf-2a4e-4d10-a46a-e9e041da8eb3>`_'s URI becomes http://musicbrainz.org/artist/0383dadf-2a4e-4d10-a46a-e9e041da8eb3, and `Bohemian Rhapsody <https://musicbrainz.org/recording/ebf79ba5-085e-48d2-9eb8-2d992fbf0f6d>`_'s URI becomes http://musicbrainz.org/recording/ebf79ba5-085e-48d2-9eb8-2d992fbf0f6d.

.. seealso::

   There are several other identifiers that MusicBrainz uses:

      - :doc:`Disc ID </terminology/terms/disc_id>`: An ID calculated from the TOC of a CD.
      - :doc:`AcoustID </terminology/terms/acoustid>`: the open-source `acoustic fingerprint <https://en.wikipedia.org/wiki/acoustic_fingerprint>`_ system used by MusicBrainz since 2013.
      - :doc:`Barcode </terminology/terms/barcode>`: Machine-readable numbers used as stock control mechanisms by retailers.
      - :doc:`ISRC </terminology/terms/isrc>`: The International Standard Recording Code, an identification system for audio and music video recordings.
      - :doc:`ISWC </terminology/terms/iswc>`: The International Standard Musical Work Code, an identification system for musical works.
      - :doc:`IPI </terminology/terms/ipi>`: a number identifying persons connected to ISWC registered works (authors, composers, etc.).
