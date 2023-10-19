.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Guess_Case

Guess Case
==========

Guess case changes the capitalization of titles to be closer to our language guidelines. While in most situations it is not perfect and the result will still need some human corrections, it can still save a lot of time.

Modes
-----

These are the currently available Guess Case modes:

**English**
   This method tries to make titles follow the :doc:`English language guidelines </style_guides/language_guides/english>`.

**Sentence**
   This method capitalizes the first word of a sentence, but all the following words of the sentence are kept lowercase. This is close to the guidelines for a lot of non-English languages, but you should still look out for proper nouns and any other differences indicated in the :doc:`appropriate language guideline </style_guides/language_guides/_language_guides>`.

**French**
   This method is very similar to the Sentence one, but a space is inserted before semicolons, colons, exclamation marks and question marks (;:!?) and text inside guillemets is padded with spaces too (« text »). Keep in mind this method is not smart enough to figure out when the first noun in a sentence should be capitalized according to the :doc:`French language guidelines </style_guides/language_guides/french>`.

**Turkish**
   This method tries to make titles follow the :doc:`Turkish language guidelines </style_guides/language_guides/turkish>`. It is fairly similar to the English one, but it has a different set of (Turkish) words that it will lowercase, and it knows how to capitalize letters ı and i.


Options
-------

**Keep all-uppercase words uppercased (on by default)**
   With this option on, a title like “Absolute ABBA” is left as-is. Without this option on, a title like “A VERY LOUD TITLE” will be converted to “A Very Loud Title”, “A very loud title” or whatnot, depending on the mode chosen. Select it if some words are intentionally all-uppercase in the title; unselect it if you have an all-uppercase tracklist that you'd want to turn into normal case.

**Uppercase Roman numerals**
   This option will turn any Roman numerals in the titles into their more standard uppercase version. Keep in mind that if you aren't specifically trying to uppercase any Roman numerals in the titles, it might be sensible to keep this off: there's a fair amount of common music-related words that are also Roman numerals, such as "mix" (1009) or "mic" (1099), or the key E in several languages ("mi", 1001).
