.. MusicBrainz Documentation Project

.. https://wiki.musicbrainz.org/Entity

Entity Types
============

Normal Entities
---------------

:doc:`Artist </terminology/entities/artist>`
   An artist is generally a musician, group of musicians, a collaboration of multiple musicians or other music professionals who contribute to works described in the :doc:`MusicBrainz Database </musicbrainz_database/index>`. They can also be a non-musical person (like a photographer, an illustrator, or a poet whose writings are set to music), or even a :doc:`fictional character </terminology/terms/fictional_character>`.

   :doc:`Artist credits </terminology/entities/artist_credit>` are a list of artists, variations of artist names and pieces of text to join the artist names.

:doc:`Event </terminology/entities/event>`
   An organised event which people can attend, and is relevant to MusicBrainz. Events generally refer to live performances, like concerts and festivals.

:doc:`Label </terminology/entities/label>`
   Labels are generally imprints on :doc:`releases </terminology/entities/release>`, and to a lesser extent, the record companies behind those imprints.

:doc:`Place </terminology/entities/place>`
   Places are areas smaller than a geographical region (like a building or an outdoor area) used to perform or produce music. It could range from a stadium to a religious building to an indoor arena.

:doc:`Recording </terminology/entities/recording>`
   Recordings are unique audio data. It has a title, :doc:`artist credit </terminology/entities/artist_credit>`, and duration. Recordings can be linked to tracks on releases. Each track must always be associated with a single recording, but a recording can be linked to any number of tracks.

:doc:`Release </terminology/entities/release>`
   Releases are real-world release objects (like a physical album) that you can buy in your music store. When a musical product is issued on a specific date with specific information such as the country, label, barcode and packaging, it is a release.

   A :doc:`medium </terminology/entities/medium>` is a piece of media included in a release. It contains information about the format, position in the release and an optional title as well as a list of tracks. Several media exist, including but not limited to: CD, 12" vinyl, digital media. A medium normally has a tracklist.

   A :doc:`track </terminology/entities/track>` contains a link to a :doc:`recording </terminology/entities/recording>`, title, :doc:`artist credit </terminology/entities/artist_credit>` and the position on the :doc:`medium </terminology/entities/medium>`. A track is different from a recording in that it is unique to a release; a number of different releases can contain the same recording.

:doc:`Release Group </terminology/entities/release_group>`
   Release groups are an abstract "album" entity. Technically it's a group of releases, with a specified type.

:doc:`Series </terminology/entities/series>`
   A series is a sequence of separate release groups, releases, recordings, works or events with a common theme. The theme is usually prominent in the branding of the entities in the series and the individual entities will often have been given a number indicating the position in the series.

:doc:`URL </terminology/entities/url>`
   A URL represents a regular Internet `Uniform Resource Locator <https://en.wikipedia.org/wiki/Uniform_Resource_Locator>`_ and an associated description of that URL.

:doc:`Work </terminology/entities/work>`
   A work is a distinct intellectual or artistic creation, which can be expressed in the form of one or more audio recordings. While a recording represents audio data, a work represents the composition behind the recording.

Entities with editing restrictions
----------------------------------

The following entities can only be added by `privileged users <https://musicbrainz.org/privileged>`_. See details on the specific entity page for more information on how to request getting new ones added.

:doc:`Area </terminology/entities/area>`
   Areas are historical and existing geographic regions. Areas include countries, sub-divisions, counties, municipalities, cities, districts and islands.

:doc:`Genre </terminology/entities/genre>`
   Genres are a way to categorize music based on its style or other common characteristic.

:doc:`Instrument </terminology/entities/instrument>`
   Instruments are devices created or adapted to make musical sounds.
