.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Sub_Optimal_Credits

Sub-Optimal Credits
===================

While the MusicBrainz schema can correctly store a huge amount of data, at some moment you'll probably find something that just can't be entered with as much detail as the available information sources (be it liner notes, a website or other) provide. In these cases, you should add a "Sub Optimal Credits" section to the annotation for the entity.

Add the information to the smallest entity that qualifies: if you have information in a booklet that applies just to a recording, add it in the recording's annotation, not the one for the full release it appears in. If at all possible, add a relationship which is as accurate as MusicBrainz allows, and indicate what that relationship exactly represents in the "Sub Optimal Credits" section. If it is not possible, leave it uncredited (but remember to indicate this fact).

You should try to structure the Sub Optimal Credits section in the least confusing way you can. You can see `examples of annotations that include it <https://musicbrainz.org/search?query=%22SubOptimalCredits%22+OR+%22Sub+Optimal+Credits%22&type=annotation&limit=25&advanced=1>`_, like:

.. code::

   === [SubOptimalCredits] ===

If the information you are missing is a particular instrument, :doc:`follow the instructions </how-tos/add_instrument>` to request that it be added. Other relationships, vocal types and the like can be proposed by :doc:`adding a ticket </how-tos/add_change_request_ticket>`.
