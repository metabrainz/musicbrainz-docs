.. MusicBrainz Documentation Project

Voting
======

Voting is the twin process of :doc:`editing </introductions/editing>`, and while often neglected it is equally important for the correct functioning of MusicBrainz. User review and :doc:`style guidelines </style_guides/_detailed_guides>` are what makes the MusicBrainz data be relatively free of wrong information.

Voting
------

If you registered as a MusicBrainz user more than two weeks ago and at least 10 of your :doc:`edits </terminology/terms/edit>` have been accepted, you can participate in the voting process. A good start would be to :doc:`subscribe </terminology/terms/subscription>` to a few artists and labels you're familiar with. By doing this you will receive a mail every day any other user enters any edits involving your subscriptions, and you'll also be able to access said edits via the Edits for Subscribed Entities link in the My Data menu on the site.

The act of voting is pretty simple: just choose Yes or No and enter your vote (you can also abstain if you're not sure). You should follow the :doc:`Code of Conduct </guidelines/code_of_conduct>` and, of course, you should not vote on a whim. Before voting on an edit, read all its :doc:`edit notes </terminology/terms/edit_note>`: they'll usually let you know why the user is trying to make an edit. If the edit note is unclear (or there isn't one) feel free to (politely!) ask the editor for more information with your own edit note. You should also be familiar with the appropriate :doc:`style guidelines </style_guides/_detailed_guides>` and, if possible, with the entity being edited. If you're voting No, please **always** leave an edit note explaining why: this allows the editor to explain his reasons or, if the edit is just wrong, gives him/her pointers on what to do instead.

Voting is not always an one-off process. By default you will get an email when someone adds an edit note to an edit you've voted Yes or No on (or left an edit note on); these notes might sometimes convince you to change your vote. Or, if you stop being sure about your vote, just change it to Abstain.

.. _introductions_voting_applying_edits:

Applying edits
--------------

The immense majority of edits stay open for 7 days unless they are approved by an :ref:`auto-editor <terms_editor_auto_editor>`, in which case they are automatically applied, or get three unanimous votes before that, in which case they'll be either applied (3 Yes) or rejected (3 No) shortly. At the end of the 7 day period, if they're still open, a check is made. If there are at least as many No votes as Yes votes, the edit is rejected. If there are no No votes, or fewer No votes than Yes votes, the edit is applied.

Amendment edits
^^^^^^^^^^^^^^^

To allow rectifying one's own mistakes after adding new entities, most edits by the entity adder that would normally require voting can be automatically applied if no more than 24 hours have passed since the initial addition.

"Destructive" edits
^^^^^^^^^^^^^^^^^^^

Some edits (most removals and merges) are considered "destructive" (meaning they're either impossible or very hard to revert). Because of this, they do not apply immediately even if they get 3 uncontested Yes votes. A "destructive" edit will always remain open for at least 48 hours, even if it received 3 Yes votes before that. A "destructive" edit with at least 3 uncontested Yes votes will apply after the 48 hour period; a "destructive" edit that gets its third uncontested Yes vote after being open for more than 48 hours will apply automatically.

Delay after a No vote
^^^^^^^^^^^^^^^^^^^^^

In most cases, the editor making an edit will want to react to a No vote on it. To ensure the original editor has time to react, the first No vote on an edit will extend the time until expiration to 72 hours if it was less than 72 hours when the vote was entered. Similarly, instead of automatically being rejected when having 3 uncontested No votes, the edit will stay open until 72 hours have passed from the first No vote, giving time to the editor to either argue their case or :doc:`cancel the edit </how-tos/cancel_edit>`.

.. note:: The voting period of an edit can be extended multiple times as long as the count of No votes goes from 0 to 1 (i.e. it becomes contested again)

This flowchart illustrates how edits become (or don't become) applied:

.. image:: /images/Vote-flowchart-simple.png
