.. MusicBrainz Documentation Project

.. https://musicbrainz.org/relationship/e6159066-6013-4d09-a2f8-bc473f21e89e

Label Rename
============

Description
-----------

This describes a situation where a label has changed its name, either for purely aesthetic reasons or following a buyout/sellout/spin-off. Extra care should be taken with cases where complicated merge/split/restructure financial operations are done. For example, it's not a good idea to rename the label `Verve <https://musicbrainz.org/label/99a24d71-54c1-4d3f-88cc-00fbcc4fce83>`_ into `The Verve Music Group <https://musicbrainz.org/label/4fb00dfd-7674-44c0-bf67-79daf8c61767>`_, as Verve continued its existence thereafter as an imprint.

| **ID**: 202
| **Cardinality of {entity0}**: Few relationships (0)
| **Cardinality of {entity1}**: Few relationships (0)
| **Orderable direction**: None (0)
| **UUID**: e6159066-6013-4d09-a2f8-bc473f21e89e


Link phrases
------------

   - **Forward link phrase**: renamed into
   - **Reverse link phrase**: renamed from
   - **Long link phrase**: was renamed into


Attributes
----------

The following attributes can be used with this relationship type:

   - start date
   - end date


Guidelines
----------

The start and end dates should contain the date the rename occurred. The same date should be used in both fields, as a label is not "renamed" over a period of time.

Try to remember that MusicBrainz is not a corporate database, so keep it simple. Avoid abusing this relationship by trying to follow companies' existences too closely. A company slightly altering its name, without significant change to its imprint(s) or ownership details, is not enough to justify adding new labels to the database (to then be used as targets for this relationship).

Keep in mind that the minor benefit of that extra bit of detail is far outweighed by the complexity involved in ensuring that editors assign the correct version of the company as the label for releases.


Example
-------

`Satellite Records <https://musicbrainz.org/label/666a6186-b34b-437e-b200-4dbf3690ed11>`_ *(50s/60s US, renamed to Stax)* was renamed into `Stax <https://musicbrainz.org/label/3d60c9cf-c020-49e8-a803-2189c146b880>`_ in 1961
