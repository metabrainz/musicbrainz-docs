.. MusicBrainz Documentation Project

.. https://wiki.musicbrainz.org/Work

Work
====

In MusicBrainz terminology, a work is a distinct intellectual or artistic creation, which can be expressed in the form of one or more audio recordings. While a work in MusicBrainz is usually musical in nature, it is not necessarily so. For example, a work could be a novel, play, poem or essay, later recorded as an oratory or audiobook.

.. seealso::

   `Musical composition at Wikipedia <http://en.wikipedia.org/wiki/Musical_composition>`_.


Distinctiveness
---------------

A work's distinctiveness is based on the artists who contributed to its final output, and whether a work is derived from another original work. Examples of works that are distinct:

   - a work that is written by an individual songwriter
   - a work that is the result of a collaboration between composer and lyricist
   - an instrumental work where an artist later adds lyrics
   - translation of an original work into a different language
   - a parody of an original work with differing lyrics
   - a medley of multiple original works
   - a mashup of multiple original works


Types of works
--------------

Works are represented predominantly at two levels:

**Discrete works**
   An individual song, musical number or movement. This includes recitatives, arias, choruses, duos, trios, etc. In many cases, discrete works are a part of larger, aggregate works.

**Aggregate works**
   An ordered sequence of one or more songs, numbers or movements, such as: symphony, opera, theatre work, concerto, and concept album. A popular music album is not considered a distinct aggregate work unless it is evident that such an album was written with intent to have a specifically ordered sequence of related songs (i.e. a “concept album”).


Style guidelines
----------------

Please see the :doc:`guidelines for works </style_guides/work>`.


Properties
----------

**Name**
   The canonical title of the work, expressed in the language it was originally written.

**Type**
   The type of work.

**Aliases**
   If a discrete work is known by name(s) or in language(s) other than its canonical name, these are specified in the work's :doc:`aliases </terminology/terms/alias>`.

**ISWC**
   The :doc:`International Standard Musical Work Code </terminology/terms/iswc>` assigned to the work by copyright collecting agencies.

**MBID**
   See the :doc:`page about MBIDs </terminology/terms/mbid>` for more information.

**Disambiguation Comment**
   See the :doc:`page about comments </terminology/terms/disambiguation>` for more information.

**Annotation**
   See the :doc:`page about annotations </terminology/terms/annotation>` for more information.


Relationships
-------------

A work is associated with artists, recordings and other works through advanced relationships.

**Work-to-Artist relationship**
   A work can be associated with one or more composer, arranger, instrumentator, orchestrator, lyricist, librettist, translator and publisher.

**Work-to-Recording relationship**
   A work can be associated with one or more recordings. This provides the indirect association between a work and its performance and production artists.

**Work-to-Work relationships**
   A work can be associated with one or more other works. There are two types of work-work relationships:

**Part-of-work relationship**
   A work can be expressed as a part of another work.

**Derivative work relationship**
   A work can be expressed as being derived from one or more other works. Examples: instrumental work with lyrics added later, translation of a work into a different language, mashup.


Artists
-------

Works do not have an artist of their own, all artists are derived from the work's relationships. A work will show up under the works tab for any artist directly linked to a work (e.g. composers, lyricists). Any works linked to the artist's recordings will also be shown there.


.. _entities_work_external_databases:

External databases
------------------

.. list-table::
   :class: longtable
   :widths: 1 1 1 1
   :header-rows: 1

   * - Provider
     - Service
     - Main areas covered
     - Notes

   * - `CISAC <https://en.wikipedia.org/wiki/Conf%C3%A9d%C3%A9ration_Internationale_des_Soci%C3%A9t%C3%A9s_d%27Auteurs_et_Compositeurs>`_
     - `ISWCNet database <http://iswcnet.cisac.org/>`_
     - Many countries [1]_
     -

   * - `SACEM <https://en.wikipedia.org/wiki/Soci%C3%A9t%C3%A9_des_auteurs,_compositeurs_et_%C3%A9diteurs_de_musique>`_
     - `Search engine <https://repertoire.sacem.fr/>`_
     - France
     -

   * - `GEMA <https://en.wikipedia.org/wiki/Gesellschaft_f%C3%BCr_musikalische_Auff%C3%BChrungs-_und_mechanische_Vervielf%C3%A4ltigungsrechte>`_
     - `Search engine <https://online.gema.de/werke/search.faces>`_
     - Germany
     -

   * - `SIAE <https://en.wikipedia.org/wiki/Italian_Society_of_Authors_and_Publishers>`_
     - `Search engine <https://www.siae.it/archivioOpere/OpereMusicali/musicaSearch.do>`_
     - Italy
     -

   * - `SGAE <http://www.sgae.es/>`_
     - `Search engine <https://enlinea.sgae.es/RepertorioOnline>`_
     - Spain
     -

   * - `JASRAC <http://www.jasrac.or.jp/>`_
     - `Search engine <http://www2.jasrac.or.jp/eJwid/>`_
     - Japan
     -

   * - `KOMCA <http://komca.or.kr/>`_
     - `Search engine <https://www.komca.or.kr/foreign2/eng/S01.jsp>`_
     - South Korea
     -

   * - `SUISA <http://www.suisa.ch/en/>`_
     - `Search engine <https://sso.suisa.ch/wdb/>`_
     - Switzerland
     -

   * - `BMI <http://en.wikipedia.org/wiki/Broadcast_Music,_Inc.>`_
     - `Search engine <https://repertoire.bmi.com/>`_
     - USA
     -

   * - `ASCAP <http://en.wikipedia.org/wiki/American_Society_of_Composers,_Authors_and_Publishers>`_
     - `Search engine <https://www.ascap.com/repertory>`_
     - USA
     -

   * - `SESAC <https://www.sesac.com/>`_
     - `Search engine <https://www.sesac.com/#!/repertory/search>`_
     - USA
     - No ISWCs

   * - `CASH <http://www.cash.org.hk/>`_
     - `Search engine <https://www.cash.org.hk/work_search>`_
     - Hong Kong
     - No ISWCs

   * - `e-License <http://www.elicense.co.jp/>`_
     - `Search engine <https://ssl.elicense.co.jp/piece_search/search>`_
     - Japan
     - No ISWCs?

   * - `MÜST <http://www.must.org.tw/>`_
     - `Search engine <https://www.must.org.tw/tw/chinese_musical/index.aspx>`_
     - Taiwan
     - No ISWCs

   * - `SACM <http://sacm.org.mx/>`_
     - `Search engine <http://www.sacm.org.mx/Informa/Repertorio>`_
     - Mexico
     -

   * - `SOCAN <https://www.socan.ca/>`_
     - `Search engine <https://www.socan.ca/controller?modulePageName=repertoirePage&subPage=pubRepertoireSearch&searchOption=b&language=en&session=skip>`_
     - Canada
     - No ISWCs

   * - `APRA <https://www.apra.com.au/>`_
     - `Search engine <https://www.apra.com.au/cms/worksearch/worksearch.srvlt>`_
     - Australia/New Zealand
     - No ISWCs

   * - `SAZAS <http://www.sazas.org/>`_
     - `Search engine <https://www.sazas.org/Glasba/Baza-avtorjev-in-del/Baza-Zdru%C5%BEenja-SAZAS>`_
     - Slovenia
     - No ISWCs

   * - `SABAM <http://www.sabam.be/>`_
     - `Search engine <https://www.sabam.be/pls/apex/f?p=1050:1>`_
     - Belgium
     -

   * - `ZAIKS <http://www.zaiks.org.pl/>`_
     - `Search engine <https://online.zaiks.org.pl/WorkCatalog/pages/welcome.jsf>`_
     - Poland
     -

   * - `MACP <http://www.macp.com.my/>`_
     - `Search engine <https://macp.com.my/work-search/>`_
     - Malaysia
     - No ISWCs

   * - `RAO <http://www.rao.ru/>`_
     - `Search engine <http://rao.ru/information/reestry/reestr-proizvedenij-rossijskih-pravoobladatelej/>`_
     - Russia
     - No ISWCs

   * - `OSA <http://www.osa.cz/>`_
     - `Search engine <https://search.osa.cz/>`_
     - Czech Republic
     -

   * - `AKM <http://www.akm.at/>`_
     - `Search engine <https://www.akm-aume.at/akm-webapp/pages/werksuche/sucheDefault.jsf?conversationContext=6>`_
     - Austria
     -

   * - `BUMA/STEMRA <http://www.bumastemra.nl/en/>`_
     - `Search engine <http://www.bumastemra.nl/en/about-buma-stemra/title-catalogue/>`_
     - Netherlands
     -

   * - `CCLI <http://www.ccli.com/>`_
     - `Search engine <https://songselect.ccli.com/>`_
     - Many countries [2]_
     - Account required; No ISWCs

   * - `HFA <https://www.harryfox.com/>`_
     - `Search engine <https://secure.harryfox.com/songfile/public/publicsearch.jsp>`_
     - USA?
     - No ISWCs

   * - `AKKA/LAA <http://www.akka-laa.lv/en/>`_
     - `Search engine <https://portals.akka-laa.lv/PublicCreations/SearchCreations>`_
     - Latvia
     - No ISWCs

.. rubric:: Notes

.. [1] Argentina, Australia, Barbados, Belgium, Canada, Chile, Colombia, Costa Rica, Cuba, Denmark, Ecuador, Estonia, Finland, France, Germany, Great Britain, Hungary, Ireland, Jamaica, Mexico, Norway, Panama, Peru, St. Lucia, South Africa, Spain, Sweden, Switzerland, Trinidad and Tobago, USA (repertoire represented by BMI), Uruguay and Venezuela
.. [2] Australia, Belgium, Botswana, Brazil, Canada, Denmark, Faroe Islands, Finland, Germany, Iceland, Ireland, Lesotho, Luxembourg, Malawi, Namibia, Netherlands, New Zealand, Norway, Singapore, South Africa, South Korea, Swaziland, Sweden, Switzerland, United Kingdom, United States and Zimbabwe
