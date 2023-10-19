.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Annotation

Annotation
==========

Overview
--------

**Annotations** are text fields, functioning like a miniature wiki, that can be added to any existing artists, labels, recordings, releases, release groups and works.

Their purpose is to add information that usually doesn't fit into the strict structural data schema of MusicBrainz (be it due to technical limitations that may be addressed later, or because the information in itself has to be free-text).

The content of an annotation can be edited by any MusicBrainz user. Like the rest of the database, if something is incorrect or incomplete, you can fix it. All changes are recorded and if someone deletes or defaces the annotation, you can easily restore a previous copy.


Uses of annotations
-------------------

You should **never** add copyrighted content copied from other resources, be they online or printed. More generally, you really shouldn't copy/paste any kind of content, unless it's purely factual.

That being said, here are some things you can add to annotations:

   - Additional facts and trivia: place of recording of a track, city of birth of an artist, awards won by a release, or any other data that doesn't fit into the MusicBrainz schema. This is especially useful when the details given in a liner are more precise than what MusicBrainz currently allows to enter: some tips for entering this data can be found in :doc:`Sub Optimal Credits </terminology/terms/sub_optimal_credits>`.

   .. newline between bullets

   - Miscellaneous editing warnings or information: for example if the entity name presents some specific spelling and/or capitalization difficulty, or why it shouldn't be merged into another.

   .. newline between bullets

   - Open issues to resolve: if you think something is wrong but you're not sure or don't want to fix it yourself, you can write a short note to warn others about it. You may use the word "FIXME" before your note. e.g. "FIXME: some of the releases in this label page should probably be moved to label X".

   .. newline between bullets

   - Additional disambiguation: in the cases when two entities can't be fully distinguished with a short comment, a longer explanation can be included in the annotation. It's usually a good idea to add "See annotation" at the end of the disambiguation comment in these cases.


Technical information
---------------------

**Wiki formatting**

You may use the following wiki formatting in your annotations:

   - ``''italics''``
   - ``'''bold'''``
   - ``'''''bold italics'''''``
   - ``----`` (horizontal rule)
   - ``= Title 1 =``
   - ``== Title 2 ==``
   - ``=== Title 3 ===``
   - ``*`` (preceded by four spaces, at the start of a line) for bulleted list
   - Eight spaces (at the start of a line) for code
   - ``url or [url]`` or ``[url|description]`` for links (note the pipe "|")

Note that anything else won't work - especially not interwiki links, and not **html markup**.

As square brackets are used for hyperlinks, you have to use the encoded html equivalents (``&#91;`` for [ and ``&#93;`` for ]) if you don't want them to be converted into hyperlinks. Example: If you want to use [unknown] in the annotation, you'll have to write ``&#91;unknown&#93;``.

**Entity merges and removals**

When an entity is deleted, all versions of the annotation attached to it are lost. When two entities are merged, their annotations are too: if the entity being merged had an annotation, the text will be appended to the end of the destination entity's annotation and their histories will get merged.
