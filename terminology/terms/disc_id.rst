.. MusicBrainz Documentation Project

Disc ID
=======

A Disc ID is the code number that MusicBrainz uses to link a physical CD to a :doc:`release </terminology/entities/release>` listing.

It is a string of letters, such as: `XzPS7vW.HPHsYemQh0HBUGr8vuU- <http://musicbrainz.org/cdtoc/XzPS7vW.HPHsYemQh0HBUGr8vuU->`_.

Detailed Display
----------------

Disc IDs for a release can be seen on the Disc IDs tab. Clicking on a Disc ID will display detailed information about it.

Disc ID Clashes
---------------

A release may have multiple Disc IDs, and a single Disc ID may be linked to multiple releases. This occurs because :doc:`disc ID calculation </development/disc_id_calculation>` involves a hash of the frame offsets of the CD tracks.

- Different pressings of a CD often have slightly different frame offsets, resulting in different Disc IDs.
- Conversely, two different CDs may have exactly the same set of frame offsets and therefore share the same Disc ID. For example: `lwHl8fGzJyLXQR33ug60E8jhf4k- <http://musicbrainz.org/cdtoc/lwHl8fGzJyLXQR33ug60E8jhf4k->`_.

.. seealso::

   :doc:`How to Add Disc IDs </how-tos/add_disc_ids>`
      Tutorial on adding Disc IDs to a release.
   :doc:`Disc ID Calculation </development/disc_id_calculation>`
      Explanation of how Disc IDs are calculated.