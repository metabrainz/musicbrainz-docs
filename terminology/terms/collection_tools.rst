.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Collections/Tools

Collection Tools
================

To manage your collection with :doc:`MusicBrainz </miscellaneous/about>`, we hope to have a number of tools available in the future which can scan your music directory and submit your collection to MusicBrainz. This page will provide a list of tools which support this.

List of tools
-------------

`Beets <http://beets.radbox.org/>`_, an open-source command-line music manager, has a `MusicBrainz collection plugin <http://beets.readthedocs.org/page/plugins/mbcollection.html>`_ that lets you add albums to your collection.

Development
-----------

For developers (and adventurous users) there is example code.

   - http://svn.musicbrainz.org/miscellaneous/trunk/collection/. - You can use this tool to submit your collection, written in python by `kuno <https://wiki.musicbrainz.org/User:Kuno>`_.

   - http://muz.goatse.co.uk/musicbrainz/collections - This is a Perl script that allows for a user point it to a directory (containing any number of sub folders) that contains MP3s. It will then submit to the :doc:`XML Web Service </products/web_service>` based on files found. This was made by Muz. Any issues are best raised with Muzzz on the :doc:`IRC Channel </miscellaneous/irc>`.

   - `MusicBrainz::Collection <http://search.cpan.org/dist/MusicBrainz-Collection/>`_ - Another Perl script for uploading collection information. Supports MP3, MP4, FLAC, Ogg Vorbis, WMA, WAV, AIFF, Musepack, and Monkey's Audio.

   - `python-musicbrainz-ngs <https://github.com/alastair/python-musicbrainz-ngs>`_ - Contains Python bindings for the collection API.
