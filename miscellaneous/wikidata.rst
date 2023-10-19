.. MusicBrainz Documentation Project

.. https://wiki.musicbrainz.org/Wikidata

Wikidata
========

Jump to navigationJump to search
From the mouth of the horse: "**Wikidata** is a free knowledge base that can be read and edited by humans and machines alike. It is for data what Wikimedia Commons is for media files: it centralizes access to and management of structured data, such as interwiki references and statistical information. Wikidata contains data in every language supported by the MediaWiki software." `[1] <https://www.wikidata.org/>`_

Wikidata interacts with MusicBrainz in various ways. This page is meant to note these various ways for MusicBrainz editors.


MusicBrainz
-----------

Interactions that affect MusicBrainz:

**Relationships**
   The most straight-forward are the Wikidata URL relationships. A few bots scour MusicBrainz and add Wikidata links to entities, but it can also be done manually.

      - `All open Wikidata relationship edits <http://musicbrainz.org/search/edits?auto_edit_filter=&order=desc&negation=0&combinator=and&conditions.0.field=link_type&conditions.0.operator=%3D&conditions.0.args=358&conditions.0.args=352&conditions.0.args=733&conditions.0.args=354&conditions.0.args=594&conditions.0.args=353&conditions.0.args=749&conditions.0.args=351&conditions.1.field=status&conditions.1.operator=%3D&conditions.1.args=1&field=Please+choose+a+condition>`_.
      - `All Wikidata relationship edits <http://musicbrainz.org/search/edits?auto_edit_filter=&order=desc&negation=0&combinator=and&conditions.0.field=link_type&conditions.0.operator=%3D&conditions.0.args=358&conditions.0.args=352&conditions.0.args=733&conditions.0.args=354&conditions.0.args=594&conditions.0.args=353&conditions.0.args=749&conditions.0.args=351&field=Please+choose+a+condition>`_.

**Areas**
   Areas were originally imported from Wikidata by `area_bot <https://musicbrainz.org/user/area_bot>`_, although that script is not currently running (if you want to request a missing area, please create a ticket in `JIRA <http://tickets.musicbrainz.org/browse/AREQ>`_).


Wikimedia
---------

There are several properties in `Wikidata <https://wikidata.org/>`_ for MBIDs, all of which can be used to link an item on Wikidata to MusicBrainz:

   - `Area MBID <https://www.wikidata.org/wiki/Property:P982>`_
   - `Artist MBID <https://www.wikidata.org/wiki/Property:P434>`_
   - `Event MBID <https://www.wikidata.org/wiki/Property:P6423>`_
   - `Genre MBID <https://www.wikidata.org/wiki/Property:P8052>`_
   - `Instrument MBID <https://www.wikidata.org/wiki/Property:P1330>`_
   - `Label MBID <https://www.wikidata.org/wiki/Property:P966>`_
   - `Place MBID <https://www.wikidata.org/wiki/Property:P1004>`_
   - `Recording MBID <https://www.wikidata.org/wiki/Property:P4404>`_
   - `Release MBID <https://www.wikidata.org/wiki/Property:P5813>`_
   - `Release Group MBID <https://www.wikidata.org/wiki/Property:P436>`_
   - `Series MBID <https://www.wikidata.org/wiki/Property:P1407>`_
   - `Work MBID <https://www.wikidata.org/wiki/Property:P435>`_

The template `Authority Control <https://en.wikipedia.org/wiki/Template:Authority_control>`_ on the English Wikipedia will automatically include a link to MusicBrainz.
