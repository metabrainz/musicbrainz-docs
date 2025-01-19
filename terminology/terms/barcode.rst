.. MusicBrainz Documentation Project

Barcode
=======

Definition
----------

`Barcodes <https://en.wikipedia.org/wiki/Barcode>`_ are numbers used as stock control mechanisms by retailers: as such they are highly standardised and well recognised, and form an invaluable identifier for communication between companies.

On physical releases, they usually appear in the form of a machine-readable series of black and white bars, hence the name "barcode".

On digital releases, they appear in numerical form and might be embedded in metadata of downloaded files, returned by an `API <https://en.wikipedia.org/wiki/API>`_, hidden in the HTML source of a digital service provider or are part of a `URL <https://en.wikipedia.org/wiki/URL>`_.

There are many different types of barcode, but the ones usually found on music releases are two:

* `Universal Product Code <https://en.wikipedia.org/wiki/Universal_Product_Code>`_ (UPC), which is the original barcode used in North America. They are 12 digits long, but any number of zeros at the start can be left off, so the actual printed barcode can be shorter than this.
* `European Article Number <https://en.wikipedia.org/wiki/European_Article_Number>`_ (EAN) also known as Japanese Article Number (JAN), which is widely used in the rest of the world. The 13 digit type (EAN-13) is the most common, although there are others such as EAN-8. A UPC can be turned into an EAN-13 by adding a leading zero.

Since 2005 both EAN and UPC are subsumed under the umbrella GTIN format which can be padded with leading zeroes up to 14 digits.

Guidelines
----------

See :ref:`the guideline for barcodes <style_release_barcode>`.

Other identifiers
-----------------

* :doc:`Catalog number </terminology/terms/catalog_number>`
* :doc:`ASIN </terminology/terms/asin>`
* :doc:`Label Code </terminology/terms/label_code>` for labels
* :doc:`ISRC </terminology/terms/isrc>` for recordings
* :doc:`ISWC </terminology/terms/iswc>` for works

Resources
---------

* `List of country codes <https://en.wikipedia.org/wiki/List_of_GS1_country_codes>`_ to find where an EAN comes from.
* `GEPIR <https://en.wikipedia.org/wiki/GEPIR>`_ - distributed database of GS1 members, useful for looking up which company a barcode belongs to.
