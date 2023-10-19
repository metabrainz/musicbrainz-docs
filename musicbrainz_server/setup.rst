.. MusicBrainz Documentation Project

Install & Setup
===============

Setup from Docker Compose
-------------------------

This method is recommended as it makes install, setup, and maintenance much easier for you, to the cost of a small overhead compared to the size of the database.

It can be used to:

- Replicate the MusicBrainz website/web service/database,
- Test your own app that queries MusicBrainz web service,
- Develop MusicBrainz Server itself.

See `MusicBrainz Docker <https://github.com/metabrainz/musicbrainz-docker>`_ and its `release notes <https://github.com/metabrainz/musicbrainz-docker/releases>`_.

Setup from source code
----------------------

This can potentially be a very laborious and time consuming method of getting a functioning MusicBrainz server. Use it only if you cannot use MusicBrainz Docker for some reason (disk space, development, etc.)

Get a copy of musicbrainz-server from git:

.. code::

   git clone --recursive https://github.com/metabrainz/musicbrainz-server.git musicbrainz-server
   cd musicbrainz-server

And follow the instructions in the `INSTALL <https://github.com/metabrainz/musicbrainz-server/blob/master/INSTALL.md>`_ file.

Support
-------

The setup process may look daunting, but please don't let this discourage you; the INSTALL is thorough and contains a lot of information, and we are willing to provide assistance. If you have questions about installing, join us in the `#metabrainz IRC channel <http://webchat.freenode.net/?channels=metabrainz>`_ or post a question on the `community forum <https://community.metabrainz.org/tags/musicbrainz-server>`_ and we will attempt to help you out.

We recommend that you dive in and give it a try - who knows how far you'll get and what you might learn along the way!

Requirements
------------

In order to set up a running MusicBrainz server with the full database you will need:

- A linux box, preferably Ubuntu.
- 60GB+ of free disk space, (if you are a developer and only want the server code and database structure 2GB+ should do, count 6GB+ if you want sample data).
- Git knowledge which will enable you to check out the source code.
- PostgreSQL, Perl, Node.js, and some other dependencies (See `all software prerequisites <https://github.com/metabrainz/musicbrainz-server/blob/master/INSTALL.md#prerequisites>`_)

As a developer the following knowledge/skills are beneficial:

- Perl and a number of perl modules, PostgreSQL, React/JSX.
- How to compile and install packages from source on a Linux box.
- How to patch existing packages, although we can help you out if you have questions about that.

.. note::

   The server has never been ported to Windows, and we suspect that it would be a fair amount of work to make that happen.

External Links
--------------

- MusicBrainz Server
   - List of `MusicBrainz Server updates <https://blog.metabrainz.org/category/musicbrainz+server/?tag=changelog>`_ on the MetaBrainz blog
   - List of `supplemental instructions <http://blog.musicbrainz.org/category/musicbrainz+server/?tag=instructions>`_ on the MetaBrainz blog

- MusicBrainz Docker
   - List of `MusicBrainz Virtual Machine releases <https://blog.metabrainz.org/category/musicbrainz+virtual-machine/>`_ on the MetaBrainz blog
   - List of `MusicBrainz Docker releases <https://github.com/metabrainz/musicbrainz-server/releases>`_ on GitHub
