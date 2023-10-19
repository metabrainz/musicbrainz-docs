.. MusicBrainz Documentation Project

Live Data Feed
==============

The Live Data Feed enables a server running a PostgreSQL database in conjunction with the :doc:`MusicBrainz Server </musicbrainz_server/index>` software to automatically stay in sync with the main server. This is accomplished by downloading :doc:`replication </musicbrainz_database/replication>` packets (served from `metabrainz.org <https://metabrainz.org>`_) at hourly intervals and applying them to the local database. This enables a local mirror server to never be more than about an hour off sync with the main server.

Please note that we do not offer hosting services. If you wish to set up a MusicBrainz mirror you must do so on your own servers.

Licensing
---------

The replication packets are licensed under the Creative Commons `Attribution-NonCommercial-ShareAlike 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0>`_ license.

Non-commercial / personal users may sign up and `obtain a free access token for Live Data Feed <https://metabrainz.org/signup/noncommercial>`_.

Commercial use
--------------

If you are interested in commercial use of our data, how we define commercial use or sign up for commercial use, please see the `MetaBrainz Foundation <https://metabrainz.org/supporters/account-type>`_ site.

..  note::

    **Please note that MetaBrainz does not charge for access to the data. However, we ask that commercial users support our efforts financially.** Anyone can :doc:`download data snapshots </musicbrainz_database/download>` that are at most a few days old (which is better than our closest competitors) or use our :doc:`web service </products/web_service>` to have instant up to date access to the data. Clearly it takes money to continue our operations, so we ask for support for our non-profit foundation so that we may continue to develop new features. For more information, see the `MetaBrainz Foundation <https://metabrainz.org/supporters/account-type>`_ site.
