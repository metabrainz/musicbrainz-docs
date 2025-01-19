.. MusicBrainz Documentation Project

ASIN
====

ASIN stands for "Amazon Standard Identification Number," a supposedly more-or-less stable identifier Amazon uses to identify its products. Linking to Amazon was first done via an automatic process called `AmazonMatching <https://wiki.musicbrainz.org/History:Amazon_Matching>`_ which had the objective to match an album ID to the corresponding ASIN. Today this can only be done manually by adding an :doc:`advanced relationship </relationships/relationships>` of the :doc:`Amazon Relationship Type </relationships/release-url/asin>` which serves better accuracy. There is a tutorial for :doc:`how to change cover art </how-tos/add_cover_art>` using this type.

ASINs are basically derived from :doc:`barcodes </terminology/terms/barcode>`. If two different ASINs have the same barcode, it makes it really difficult to ship the right product to the right people, so this situation is usually avoided. However, sometimes an ASIN can cover more than one barcode. This might happen to allow a new pressing of the same CD to be shipped to a customer who actually ordered the old one.

The same barcode will generally have the same ASIN in any of Amazon's international Websites. However, usually different versions of the same CD (i.e., differently barcoded jewel cases) will be sold in different countries. For example, if you buy Garbage's debut album in the US you'll buy ASIN `B000001OAA <http://www.amazon.com/gp/product/B000001OAA>`_, whereas if you buy it in Germany you'll buy ASIN `B00013R89W <http://www.amazon.de/exec/obidos/ASIN/B00013R89W>`_. The track listing is identical, but the barcode on the back will be different. So there may or may not be a 1:1 correspondence between ASINs and :doc:`MusicBrainz </miscellaneous/about>` albums, depending on whether you consider these to be the same album or not.

It's probably more accurate to say that there's a 1:1 correspondence between *releases* and ASINs, but even that's not entirely clear. The same barcoded album may be imported to different countries at different times, or different barcoded albums may be quietly substituted for each other within one "release."

While Amazon often has the same ASIN for a CD sold via several national portals, the equivalent streaming and MP3 editions (via Amazon Music) can bear a different ASIN in the different national portals.

Adding an ASIN in MusicBrainz
-----------------------------

When editing on the *Release Information* tab, in the box labeled External Links type (or paste) the entire Amazon link, e.g. http://www.amazon.com/gp/product/B00005NEKI for release http://musicbrainz.org/release/b1dc9838-adf3-43f2-93f9-802b46e5fe59.