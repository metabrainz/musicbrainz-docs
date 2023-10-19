.. MusicBrainz Documentation Project

.. https://wiki.musicbrainz.org/Event/Setlist

Event Setlist
=============

Event setlists generally consist of a list of song/work titles. Additionally, they can contain artists (for example, at the start of each set in a multiple-artist concert) and additional information (like "Encore" or "Interlude").

Syntax
------

Each (non-empty) line in the setlist must start with a symbol followed by a space. Those are **@ for artists**, **\* for works/songs**, and **# for additional info** (such as "Encore").

It's possible to link to artists and works in MusicBrainz by including their :doc:`MusicBrainz ID </terminology/terms/mbid>`. To do that, use **[MBID|name to be displayed]** instead of just listing the name.

It's possible to escape the square brackets when not used for the above link, as follows:

   - left square bracket ([): ``&lsqb;`` or ``&lbrack;`` or ``&#91;`` or ``&#x5b;``;
   - right square bracket (]): ``&rsqb;`` or ``&rbrack;`` or ``&#93;`` or ``&#x5d;``;
   - ampersand (&): ``&amp;`` or ``&AMP;`` or ``&#38;`` or ``&#x26;``.

Examples
--------

**Popular music setlist**

.. code-block::

   @ [9f8ee15f-8fe8-4b4e-8a8a-8e905211b642|Leogun]
   * [8dddc197-9ef4-4b5a-9908-9310230c1237|What’s It Gonna Take?]
   * [f8e538bb-f146-421a-964f-663cc8cdae38|Let’s Be Friends]
   * [070713fc-6a63-4cf3-98dd-d5720cda6c8b|End of the World]
   * [b8600fa1-e12c-49cf-aa88-4d6d648c78ca|Medicine]
   * [4f18ba97-cbfb-4fb5-814d-cae1ed8620b4|Piggy in the Middle]
   * [7ee70167-f50a-4d88-899b-bd25a1f8c99d|By the Reins]
   @ [e1f1e33e-2e4c-4d43-b91b-7064068d3283|KISS]
   * [5b5a12c2-46e1-479c-9308-e78a7f908006|Psycho Circus]
   * [92651d41-fea1-34fb-a1d1-c772ea1b00a4|Shout It Out Loud]
   * [96d1408f-4780-3ff4-b234-c6c0d633f89e|Let Me Go, Rock ’n Roll]
   * [b05809ff-d6a9-3b17-9d8d-c15697d77462|I Love It Loud]
   * [905c8f48-ce28-4369-85d8-75202285757f|Hell or Hallelujah]
   * [bbd90dfe-265a-3e72-9ce0-99cc4fa0cdf4|War Machine] (Gene breathes fire)
   * [5dbb6fa5-9332-3890-9021-4241f4f3f4d5|Heaven’s on Fire]
   * [a35d9cc6-4732-3181-920b-0f1a0d876d56|Calling Dr. Love]
   * [c9873562-2181-4693-a8e5-358b62d225db|Say Yeah]
   * [cfc0ad98-7b8c-31ff-a804-d47c8e8b1f12|Shock Me] / [9f9e6ff8-38f4-4f24-9009-24383dadc070|Outta This World]
   # guitar and drum solos
   # bass solo (Gene spits blood and flies)
   * [75a72144-fbcf-3c3f-aabd-e85dec885cad|God of Thunder]
   * [e93851ad-502b-3549-b187-2ed8bac9c19f|Lick It Up] / [f00616af-fff7-3fe8-ab97-5dda1d34eded|Won’t Get Fooled Again]
   * [d14dc99a-a45e-394d-8fb7-06dc91670b58|Love Gun] (Paul flies over the crowd)
   * [52cb581c-5972-3d49-9cdb-bb2b472f99b9|Black Diamond]
   * [512c4801-5184-3061-934d-e3542921aa66|Detroit Rock City]
   * [0c309dd6-867a-3998-babe-57ffca970d54|I Was Made for Lovin’ You]
   * [de4c0fa3-a578-38e6-99fd-3448f7cbd640|Rock and Roll All Nite]

**Classical music setlist**

.. code-block::

   @ [4bba846d-6748-4741-8ad6-6f02a29bd0de|Edgar Arro]
   * [887f0014-1625-4a3c-baa6-7c8bf23913bf|Eesti rahvaviis nr. 10]

   @ [22af9fd9-c026-4bcd-9f6d-f7f6e851b366|Heino Eller]
   * [7d13bb1d-1ff3-48e6-96a7-699447ca0a07|Kodumaine viis]

   @ [5ed7f4fc-9cab-40f1-ab1f-d7fa1e4bba5a|Artur Kapp]
   * [4b26c8e6-4df5-4673-8050-c61436f03003|Viimne piht]

   @ [3195acf6-7432-4607-adbd-972b4c0747e2|Ester Mägi]
   * [663e8428-6f8b-4db8-94d3-1ffd2c6b6919|Kadents ja teema]

   @ Edgar Arro
   * [1a660948-480b-4246-9afd-3cd2ce28aa89|Eesti rahvaviis nr. 5]

   @ Heino Eller
   * [884f7f47-09c7-4ae9-9502-7662b2d77e46|Lüüriline valss]

   @ Edgar Arro
   * [1fba7c61-e660-4dfa-a228-b6b247fa489e|Eesti rahvaviis nr. 1]

   @ Ester Mägi
   * [81ee397c-a21a-4930-8ea3-54f74e557536|Presto]

   @ [ae0b2424-d4c5-4c54-82ac-fe3be5453270|Arvo Pärt]
   * [354c7179-3903-3723-88ff-323ed5e9c374|Fratres]

   @ Ester Mägi
   * [cf61e5bd-89bc-404c-b2f7-8383d549566f|Kuus eesti rahvaviisi]
