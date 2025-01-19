.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Edit_Note

Edit Notes
==========

Edit notes are comments left by :doc:`users </terminology/terms/editor>` on an edit and serve as an important form of communication between users on the site. They can either be entered at the time of making an edit or added to an existing edit.

.. note:: All users must follow the :doc:`Code of Conduct </guidelines/code_of_conduct>` when entering an edit note.

What to Use Them For
--------------------

Common uses for edit notes include:

- Providing supplementary information (e.g., a URL that contains the source information).
- Asking for clarification on an edit (e.g., if no source was provided).
- Discussing the changes being made and/or their appropriateness (e.g., if the change doesn't follow the :doc:`Style Guidelines </style_guides/_detailed_guides>`).
- Enabling more experienced users to help answer questions (e.g., questions on how to perform an edit correctly).

Edit notes can be as long or as short as necessary but should remain clear and concise. For more information, see :doc:`How to Write Edit Notes </how-tos/add_edit_notes>`.

Email Notification
------------------

Edit notes are displayed when viewing the edits they are left on. Additionally, they are emailed to:

- The user who made the edit.
- Other users who have entered a note on the edit.
- Any user who has voted on the edit.

.. note:: Any vote, whether "Yes," "No," or "Abstain," will result in receiving notes (previously restricted to "Yes" or "No" votes).

When to Use Them
----------------

It is good practice to leave a note whenever making a non-trivial edit to explain the changes. Including a URL link to supporting information is particularly helpful. For contentious edits, such as adding a :doc:`standalone recording </terminology/terms/standalone_recording>` or removing data, providing an edit note is crucial to avoid having the edit voted against.

When voting "No" on an edit, it is essential to leave a note explaining why. This helps:

- Inform the editor why their change may be incorrect, allowing them to cancel or correct the edit.
- Warn other voters about potential issues with the edit.
- Allow the editor to discuss their reasoning with you to potentially change your vote.

Edit Note Syntax
----------------

HTML syntax is not supported in edit notes. However, URLs are automatically displayed as clickable links, and basic wiki syntax is available:

+------------------------------+--------------------------------------------+----------------------------------------------------------+
| **Description**              | **Markup**                                 | **Result**                                               |
+==============================+============================================+==========================================================+
| Italic Text                  | ``''italic''``                             | *italic*                                                 |
+------------------------------+--------------------------------------------+----------------------------------------------------------+
| Bold Text                    | ``'''bold'''``                             | **bold**                                                 |
+------------------------------+--------------------------------------------+----------------------------------------------------------+
| Linking to an edit           | ``edit #123456``                           | `edit #123456 <https://musicbrainz.org/edit/123456>`_    |
|                              | ``edit:123456``                            |                                                          |
|                              | ``edit 123456``                            |                                                          |
+------------------------------+--------------------------------------------+----------------------------------------------------------+
| Linking to a `WikiDocs` page | ``doc:Edit_Note``                          | :doc:`Edit Note </terminology/terms/edit_note>`          |
|                              | ``[Edit_Note]``                            |                                                          |
|                              | (note: bracketed form must be Capitalized) |                                                          |
+------------------------------+--------------------------------------------+----------------------------------------------------------+

- URLs are automatically turned into links but may break if they contain special characters. In such cases, users must manually reconstruct the link.
- Long URLs will display shortened text but remain functional.

Modifying or Removing Edit Notes
--------------------------------

You can modify or remove (blank) your edit notes if:

- The edit note is your own.
- The note hasn’t been removed already.
- The note is less than 24 hours old.
- The note hasn’t received replies from others (except ModBot).
- Your edit note privileges haven’t been disabled by an admin.

To modify or remove a note, click the pencil or cross icon next to the edit note heading. You can provide a reason for the change. Changes are intended for corrections (e.g., typos) rather than completely replacing content, so emails will not be sent for modifications. For notifications, leave a new edit note instead.

Admins can modify or remove any edit notes at any time. If sensitive information (e.g., passwords) is mistakenly included and you cannot edit it, `contact us <https://musicbrainz.org/contact>`_. For spam or offensive remarks in someone else’s note, :doc:`report the user </how-tos/report_user>` and include a link to the edit(s).