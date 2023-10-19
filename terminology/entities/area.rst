.. MusicBrainz Documentation Project

.. https://wiki.musicbrainz.org/Area

Area
====

Areas are geographic regions or settlements. Areas are usually kept in sync with their :doc:`Wikidata </miscellaneous/wikidata>` entries. To request that an area be added to Musicbrainz submit a bug request under the AREQ category. See the `list of current AREQ issues <https://tickets.metabrainz.org/projects/AREQ/issues/AREQ-1840?filter=allopenissues%7Clist>`_ for more information.


Properties
----------

**Name**

The name of the area.

**Type**

The type of area. Possible values are:

   **Country**
      Country is used for areas included (or previously included) in `ISO 3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1>`_, e.g. `United States <https://musicbrainz.org/area/489ce91b-6658-3307-9877-795b68554c98>`_.

   **Subdivision**
      Subdivision is used for the main administrative divisions of a country, e.g. `California <https://musicbrainz.org/area/ae0110b6-13d4-4998-9116-5b926287aa23>`_, `Ontario <https://musicbrainz.org/area/2747553f-b44d-44c4-a7c3-b67412b6f10b>`_, `Okinawa <https://musicbrainz.org/area/ff6ef0b9-0b41-4697-bd55-8619ad4a196c>`_. These are considered when displaying the parent areas for a given area.

   **County**
      County is used for smaller administrative divisions of a country which are not the main administrative divisions but are also not municipalities, e.g. counties in the USA. These are not considered when displaying the parent areas for a given area.

   **Municipality**
      Municipality is used for small administrative divisions which, for urban municipalities, often contain a single city and a few surrounding villages. Rural municipalities typically group several villages together.

   **City**
      City is used for settlements of any size, including towns and villages.

   **District**
      District is used for a division of a large city, e.g. `Queens <https://musicbrainz.org/area/431a085b-9f4c-4fbb-82de-2ca7ce735da8>`_.

   **Island**
      Island is used for islands and atolls which don't form subdivisions of their own, e.g. `Skye <https://musicbrainz.org/area/d572815d-3a09-4091-9b32-7784020f1438>`_. These are not considered when displaying the parent areas for a given area.

**Begin and end dates**

The dates indicate when a certain area was founded and/or ceased to exist. For example, the `Soviet Union <https://musicbrainz.org/area/32f90933-b4b4-3248-b98c-e573d5329f57>`_ has a begin date of 1922 and an end date of 1991.

**ISO 3166 codes**

The `ISO 3166 codes <https://en.wikipedia.org/wiki/ISO_3166>`_ are the codes assigned by ISO to countries and subdivisions.

**Aliases**

The :doc:`aliases </terminology/terms/alias>` are used to store alternate names or misspellings.

**MBID**

See the :doc:`page about MBIDs </terminology/terms/mbid>` for more information.

**Annotation**

See the :doc:`page about annotations </terminology/terms/annotation>` for more information.
