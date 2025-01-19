.. MusicBrainz Documentation Project

ISRC
====

The **International Standard Recording Code**, abbreviated to **ISRC**, is a system of codes that identify audio and music video recordings. It is standardized by the `IFPI <https://www.ifpi.org/>`_ in ISO 3901:2001 and used by IFPI members to assign a unique identifier to every distinct sound recording they release.

An ISRC identifies :doc:`sound recordings </terminology/entities/recording>`, not the song itself. Instead, :doc:`songs </terminology/entities/work>` are identified by :doc:`International Standard Musical Work Code (ISWC) </terminology/terms/iswc>` codes. So, different recordings, edits, remixes and remasters of the same song will be assigned their own ISRC. But the same recording should have the same ISRC in all countries/territories.

ISRCs have replaced ISANs (International Standard AudioVisual Numbers) to identify music, audio recordings and music videos because they are more specific. They can also have :doc:`IPIs </terminology/terms/ipi>` attached to it, whereas the ISAN was not designed to be used with :doc:`IPIs </terminology/terms/ipi>`.

Structure
---------

The ISRC is a 12-byte alphanumeric string (only uppercase Latin letters and Arabic numerals, ``[A-Z0-9]``) of the form ``CCOOOYYSSSSS``:

* **CC** is a 2-character *country* code of only letters, as defined in `ISO 3166-1 <https://www.iso.org/obp/ui/#search/code/>`_
* **OOO** is a 3-character *owner* code of letters and/or digits
* **YY** is a 2-character *year* code of only digits
* **SSSSS** is a 5-character *serial number* of only digits

The country code shows the owner's country of residence. Owner codes are assigned by the IFPI to its members. The year defines the year in which the ISRC was allocated to the recording (although in Japan they usually antedate and set the recording year — `other antedated ISRC <https://musicbrainz.org/tag/antedated%20isrc>`_). The serial number or designation code is assigned by the owner and separates recordings with the same country, year and owner codes.

While hyphens are not part of ISRCs, they are sometimes included so that they can be read more clearly. An example would be ``CC-OOO-YY-SSSSS``.

Determining ISRCs of recordings
-------------------------------

On compact discs, ISRC codes can be stored in subchannel Q. Applications like Ahead's Nero and Exact Audio Copy (EAC), using :doc:`libdiscid </products/libdiscid>`, can read these codes. Sometimes, ISRCs are printed on the cover or in the booklet of a release. Some collection societies like `SCPP <https://www.scpp.fr/>`_ and `CISAC <https://www.cisac.org/>`_ will also show ISRCs in their online catalogues, but there is no legal or industry requirement to do that. Some online music stores like `mora.jp <https://mora.jp/>`_ also distribute music (usually as FLAC files) with ISRC written as metadata.

Resources
---------

Some users have written tools to automatically submit ISRCs from a CD or digital service provider using the :doc:`MusicBrainz API </development/api>`:

* Web: `kepstin’s MagicISRC <https://magicisrc.kepstin.ca/>`_ (`GitHub <https://github.com/kepstin/magicisrc>`_) for one {multi-disc} release (author: `kepstin <http://musicbrainz.org/user/kepstin>`_)
    * `mb. MASS ISRC <https://github.com/jesus2099/konami-command/blob/master/mb_MASS-ISRC.user.js>`_ Paste a bunch of ISRC instead of one by one in kepstin's magicisrc (author: `jesus2099 <https://musicbrainz.org/user/jesus2099>`_)
* Web: `Spotify ISRC submit <https://d.ontun.es/>`_ (author: `tatsumo <https://musicbrainz.org/user/tatsumo>`_; `MB forums thread <https://community.metabrainz.org/t/20910>`_)
* Linux, Windows, macOS (Python): `isrcsubmit <http://jonnyjd.github.io/musicbrainz-isrcsubmit/>`_ (author: `JonnyJD <https://wiki.musicbrainz.org/User:JonnyJD>`_)
  (supported back-ends: mediatools, cd_info, cdrdao, discisrc, drutils, cdda2wav, icedax; duplicate detection and review; `MB forums thread (archived) <https://web.archive.org/web/20150324140342/http://forums.musicbrainz.org/viewtopic.php?id=3444>`_)
* Linux (Perl): `submit_isrcs <http://gist.github.com/njh/9159699>`_ (author: Nicholas Humfrey, back-end: icedax)
* Linux (Ruby): `isrcs2mb <https://web.archive.org/web/20141206180357/http://users.musicbrainz.org/~outsidecontext/tools/isrcs2mb.rb>`_ by (author: `OutsideContext <https://wiki.musicbrainz.org/User:OutsideContext>`_, back-end: icedax)
* Windows: `isrcsubmit <https://web.archive.org/web/20120127060214/https://oxygene.sk/lukas/isrcsubmit-0.2.zip>`_ (author: Lukas Lalinsky, doesn't work for multi-disc releases, see `OTHER-157 <http://tickets.musicbrainz.org/browse/OTHER-157>`_)
* Windows: `Command line tool (mediatools.exe) <https://web.archive.org/web/20141206180403/http://www.flanagan-family.com/mediatools.zip>`_ for extracting ISRC and CD-Text data from CDs (author: `simonf <https://web.archive.org/web/20150211042333/http://forums.musicbrainz.org/profile.php?id=3851>`_)

.. note:: Not all CD/DVD drives can successfully read the ISRCs from the CD.

External resources
------------------

* `SoundExchange ISRC Search <https://isrc.soundexchange.com/>`_ - database of nearly 20 million ISRC codes
* `IFPI ISRC Search <https://isrcsearch.ifpi.org/>`_ - IFPI's ISRC search ("powered by SoundExchange"…)
* `Search engine <https://www.scpp.fr/en/Pages/consultation-phonogrammes.aspx>`_ for French phonograms provided by `SCPP (Société civile des producteurs phonographiques) <https://fr.wikipedia.org/wiki/Soci%C3%A9t%C3%A9_civile_des_producteurs_phonographiques>`_.
* `ISRC申报平台 <http://www.isrc.com.cn/article_cate/id-147>`_ China's ISRC database
* `國際標準錄音錄影資料代碼查詢系統 <http://isrc.ncl.edu.tw/>`_ Taiwan's ISRC database
* `PPL Repertoire Search <https://repsearch.ppluk.com/>`_ for British recordings.
* `音楽の森 <https://www.minc.gr.jp/db/>`_ (*ongakunomori=music forest*) Japan's ISRC database (requires registration, restricted to Japanese citizens)
* `ISRCHunt <https://isrchunt.com/>`_ checks if ISRC's from a Spotify Playlist exist in MB, supplies an A-tisket link

Further information
-------------------

* `The IFPI's official ISRC web site <https://isrc.ifpi.org/>`_
* `Wikipedia page about ISRC <https://en.wikipedia.org/wiki/International_Standard_Recording_Code>`_
* :doc:`GRid </terminology/terms/grid>`, another IFPI standard for identifying releases of music in electronic networks
* :doc:`ISWC </terminology/terms/iswc>`, an ISO standard for identifying musical works
* ISMN, an ISO standard for identifying printed music publications