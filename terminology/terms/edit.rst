.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Edit

Edits
=====

An edit (previously called *moderation*) is a change entered by an :doc:`editor </terminology/terms/editor>` into the :doc:`MusicBrainz Database </musicbrainz_database/index>`.

Auto-edits
----------

An auto-edit (previously called *automod(eration)*) is an edit that bypasses the normal :doc:`voting process </introductions/voting>`, being automatically approved and instantly applied. These edits display "automatically applied" rather than a vote count.

Generally, auto-edits include:

- Edits that add data to the database (e.g., adding an artist or track times).
- Minor changes to existing data (e.g., correcting capitalization).

However, not all edits follow these rules, and determining whether an edit will be auto-applied can be complex. Editors can ensure their edits go through voting by ticking the "Make all edits votable" checkbox when submitting changes.

:ref:`Auto-editors <terms_editor_auto_editor>` are trusted users with "auto-editor" privileges, allowing them to submit a broader range of changes as auto-edits.

Edit Statuses
-------------

Edits may fall into the following statuses:

Open
^^^^
An open edit can be voted on by other editors or canceled by the editor who submitted it.

Typically, new edits remain open for one week. Depending on the vote tally, edits may be applied sooner (or later). Refer to the :ref:`voting introduction <introductions_voting_applying_edits>` for more details.

Applied
^^^^^^^
The most common status. It indicates the edit was accepted and its changes have been applied.

Failed Vote
^^^^^^^^^^^
An edit with more "no" votes than "yes" votes, resulting in rejection.

No Votes Received
^^^^^^^^^^^^^^^^^^
This historical status applied when the :ref:`data quality <entities_release_data_quality>` was set to high, but the edit received no votes.

Failed Dependency, Failed Prerequisite, and Internal Error
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
These statuses indicate edits that could not be applied due to specific issues:

- **Failed Dependency**: Occurs when the entity being edited no longer exists (e.g., it was merged, deleted, or the related edit was canceled).
- **Failed Prerequisite**: Happens when the data has already been changed by another edit (e.g., a competing edit was applied first or someone else made an auto-edit).
- **Internal Error**: Rare and signifies an issue not covered above, usually a bug that should be reported via the :doc:`bug tracker </miscellaneous/bug_tracker>`.

Cancelled
^^^^^^^^^
A canceled edit is one voluntarily withdrawn by the editor who submitted it.
