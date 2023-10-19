.. MusicBrainz Documentation Project

.. https://wiki.musicbrainz.org/Label

Label
=====

Labels are one of the most complicated and controversial parts of the music industry. The main reason for that being that the term itself is not clearly defined and refers to at least two overlapping concepts: imprints, and the companies that control them. Fortunately, in many cases the imprint and the company controlling it have the same name.


What is a label?
----------------

**Imprint**

Labels in MusicBrainz refer mainly to imprints.

An imprint is (strictly, and nothing more than) a brand (and trademark) associated with the marketing of sound recordings (an imprint is not a company). An imprint may be marketed as a project, unit or division of the company that manages it. Imprints are the information you certainly want to add in the database and is the information available on sleeves in the form of a label logo (a.k.a. imprint). Imprints are labels, as one usually understand it. Specifically, you should favor using names as they are represented on the imprint, rather than using a company name (usually found in "copyright"/"produced" mentions).

**Record company**

To a lesser extent, a label entity may be created in the database to represent a record company.

A record company typically manages imprints, and coordinates the *production* / *manufacturing* / *promotion* / *relations with artist* / *PR* / *distribution* of sound recordings. Record companies may directly handle one or more of these aspects, or may sign contractual agreements with other companies to do the job. In some specific cases, you may want to create a label in the database to represent such a company name rather than an imprint: usually, such a move is required when labels went through complex merge/split operations and you need :doc:`relationships </terminology/entities/relationship>` to structure the imprints list and represent their history in a meaningful way. It can also make sense to add such a company in order to use the manufacturing and distribution relationships. Please note, though, that there is no need to "de-duplicate" companies from imprints when their name are very close.

**Music group**

Lastly, we also store music groups.

A music group is a financial holding company, whose purpose is solely to control and manage other companies directly involved in the production of sound recordings. For record companies, the use of Music groups is reserved for specific cases that you will likely not encounter unless you're doing some research intensive background work on structuring the labels list.

**Others**

At this time, we **don't** keep track of companies involved in the other aspects of the music industry (PR, management, etc.), and we **don't** get into too much financial details, or try to represent exactly the socio-economic organization of companies. There are three reasons for that:

   - this information is usually not available from sleeves
   - this information is irrelevant to the MusicBrainz goal of being the ultimate source of *music* information
   - such a project would be extremely complicated and our current data model is not fit for it

There are several entities that are **not** correct labels for which we still keep an entry so we can stop people from adding :doc:`releases </terminology/entities/release>` to them. You can find a list of these non-labels below.


Examples
--------

   - Original Production: `EMI Records <https://musicbrainz.org/label/022fe361-596c-43a0-8e22-bad712bb9548>`_
   - Holding: `EMI Group <https://musicbrainz.org/label/a8f3eb19-05db-4895-b1d2-7ec911022a5e>`_


Style guidelines
----------------

We have no specific guidelines for labels.


Label properties
----------------

**Name**

The official name of the label.

The label name should be represented as found on media sleeves, including use of characters from non latin charsets, stylized characters, etc.

If a label is renamed a new label should be created and a :doc:`label rename relationship </relationships/label-label/label_rename>` created between the two.

If there exists multiple slightly different names for the label (eg: *The Verve Music Group*, *Verve Music Group*, *VMG*), you should use the most commonly used name, or the one used on the label's official site.

Labels are not always named uniquely, and different labels may share the same label name. To help differentiate between identically named labels, you should use a :doc:`disambiguation comment </terminology/terms/disambiguation>` and possibly an :doc:`annotation </terminology/terms/annotation>` as well.

**Disambiguation**

See the :doc:`page about disambiguation comments </terminology/terms/disambiguation>` for more information.

**Type**

The :doc:`type </terminology/terms/label_type>` describes the main activity of the label.

**Area**

The :doc:`area of origin </terminology/terms/label_country>` for the label.

**Label code**

The :doc:`label code </terminology/terms/label_code>` is the "LC" code of the label.

**IPI code**

An Interested Party Information code is an identifying number assigned by the CISAC database for musical rights management. See :doc:`IPI </terminology/terms/ipi>` for more information, including how to find these codes.

**ISNI code**

The International Standard Name Identifier for the label. See :doc:`ISNI </terminology/terms/isni>` for more information.

**Date period**

The exact meaning of the begin and end dates depends on the type of label. Note that it's usually hard to know if an imprint has folded or is just on hold, so generally the end date should only be entered if there's a clear indication of its demise.

   **Begin date**

      - For officially registered trademarks or companies (holdings, distributors), it's the date at which it was registered.
      - For imprints, collection names (when used as labels) and subdivisions (or subsidiaries) for which there is no available creation date, it's the release date of the first release ever issued under that label name.
      - For bootleg companies (more generally for obscure/dubious companies), it's also tolerable to use the release date of the first release, unless more accurate data is available.

   **End date**

      - For companies (holdings, distributors), it's the date at which the company ceased to exist (be it bankrupted or dismantled).
      - For imprints, collection names (when used as labels) and subdivisions (or subsidiaries) for which there is no available dismantling date, it's the release date of the last release ever issued under that label name.
      - For bootlegs companies (or otherwise obscure/dubious companies), it's also tolerable to use the release date of the last release, unless one has more accurate information.

**Aliases**

Aliases are used to store alternate names or misspellings. For more information and examples, see the :doc:`page about aliases </terminology/terms/alias>`.

**Annotation**

See the :doc:`page about annotations </terminology/terms/annotation>` for more information.

**MBID**

See the :doc:`page about MBIDs </terminology/terms/mbid>` for more information.


Non-Labels
----------

Here is a list of labels which weren't deleted so that people can :doc:`subscribe </terminology/terms/subscription>` to them:

**Generic**

   - `[unknown] <https://musicbrainz.org/label/46caaa9e-3e26-49b5-827c-64ccc73c1b07>`_ - This is an official :ref:`special purpose label <style_unknown_and_untitled_special_purpose_label>`

**Online stores (etc)**

   - `Amazon.com <https://musicbrainz.org/label/11076740-0966-4c19-ac63-98e3d580be4c>`_
   - `Bandcamp <https://musicbrainz.org/label/76fef728-2653-4b6a-ade6-df76ab74cc97>`_
   - `CD Baby <https://musicbrainz.org/label/bd193a84-7a34-4e93-8c9a-5e81b0f226cf>`_
   - `Emubands <https://musicbrainz.org/label/039a023a-e769-4a68-a825-d21505498afe>`_
   - `Internet Archive <https://musicbrainz.org/label/44eb567e-3e38-4936-ba6c-751e2627e649>`_
   - `iTunes Store <https://musicbrainz.org/label/93ec02b7-152c-44c6-b120-d7cd483aae43>`_

**Rights societies**

See the `search results <https://musicbrainz.org/search?query=type%3A%22rights+society%22&type=label&limit=25&method=advanced>`_ for the list.


Additional information
----------------------

   - :doc:`How to identify labels </how-tos/identify_labels>`
   - :ref:`Special purpose labels <style_unknown_and_untitled_special_purpose_label>`
   - :doc:`Label FAQ </faq/label>`
   - :doc:`Label subscriptions </terminology/terms/subscription>`
   - :doc:`Extra resources </miscellaneous/label_resources>`
