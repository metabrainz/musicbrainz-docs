.. MusicBrainz Documentation Project

Code of Conduct for Bots
========================

Bot editor type
---------------

Every bot owner must contact the MusicBrainz team when creating a bot editor, so that its user type can be set to Bot. This will let voters know that the edits are entered by a bot. **Do not** run any edits with your bot until the Bot type is set.

Edit limits
-----------

**Open edits**
   There is a recommended limit of 2,000 open edits and a hard limit of 2,500 open edits per bot at the same time. Any bot which goes over the hard limit will be blocked.

**Daily edits**
   Bots shouldn't make more than 1,000 edits (be it normal edits or autoedits) per day - that allows users that want to check them all to do so.

**Exceptions**
   Exceptions to the above limits can be granted in the :doc:`Development Chat </miscellaneous/metabrainz_meeting>`.

Voting
------

Bots themselves are not allowed to vote on any edits.

Voting yes on bot edits is discouraged unless the voter knows for sure that they are correct, since it helps them to go through with fewer eyes on them. If a bot edit gets rejected, non-bot users can always re-enter the edit if they think it is correct. Reverting the edit is much more difficult, especially for removals and merges. This also applies to the bot owner: no matter how much you trust your code, manually verify everything before voting yes.

Bot owners should read and respond to edit notes on their bot edits in reasonable time. If you're not going to be able to do so, **don't run your bot!** Just wait until you have more time. You bot will quickly lose the support of the community if you ignore editor votes and comments on your edits.

Bot code
--------

We require that the code for every bot is `open-sourced <https://opensource.org/licenses>`_ and a link to the source must be provided from that bot's user page. Other bot owners, and the community in general, are encouraged to check, review and (if necessary) propose patches for them.

Additional requirements
-----------------------

In addition to a link to the bot's source code, the bot's user page must at minimum list who maintains the bot.

The bot should also log in to MusicBrainz every time it is run, regardless of whether it actually ends up making any edits or not, so that the MusicBrainz team can better keep track of which bots are actually active.
