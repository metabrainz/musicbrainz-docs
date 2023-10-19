.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Release/Date

Release Date
============

The release date is the date in which a release was made available through some sort of distribution mechanism. For example, this may be via a retail store, being published as a free download on a website or distributed to industry insiders (in the case of promotional releases) amongst other mechanisms.

What a release date is not
--------------------------

   - A *copyright* date: A release date is NOT the same as a copyright date off a disc liner or vinyl cover. It can be a useful indication for releases from obscure sources; however in the general case it is not correct. Often a copyright date can precede the year of release, if the actual release was in January. Often re-releases/re-issues will carry the copyright date of the original release rather than the year they were re-issued.

   - A *performance* date: In the case of live performance bootlegs, the ReleaseDate is a different concept to the performance date. The concert may have occurred on 2007-08-03, but it may have taken some time for the bootleg to be produced, tracks split and packaged for CD (or other :doc:`ReleaseFormat </terminology/terms/release_format>`) release. See :doc:`Live Bootleg Style </style_guides/types_of_releases/live_bootlegs>` for an attempt to structure the capture of this information with the current :doc:`MusicBrainz database </musicbrainz_database/index>` structure.

   - An *import* date: Amazon (and other retailers) often have listings for releases marked as "IMPORT". Dates for these releases should never be used as release dates; they most often represent when the retailer imported the release from its original release country and added to their database for sale. This is an incorrect release date to use; instead the release date for the home country of release should be sought, either from a different Amazon domain, or a different (local) retailer site.

Differences between countries
-----------------------------

The release date of the same release in different countries may differ by several days or several weeks. For example, up to 2015 CD releases from mainstream distributors were typically released on different days of the week in different countries, e.g. (non-exhaustive, and not a general rule).

.. table::
   :widths: auto

   ================================================ ======================================
   Location                                         Release Day
   ================================================ ======================================
   UK/Ireland Downloads (some labels)	             Sunday
   most European countries, Australia & New Zealand Monday
   US                                               Tuesday
   Japan                                            Wednesday
   Germany                                          Friday (was Monday before summer 2005)
   ================================================ ======================================

Displaying the day of week is not currently supported within MusicBrainz; however a `userscript <https://en.wikipedia.org/wiki/Userscript>`_ is available that will `display this for you in your browser <https://userscripts-mirror.org/scripts/show/8481>`_.


Sources for release dates
-------------------------

Since a copyright date is not a reliable source (only an indicative source), the release date will usually need to be sourced online. Possible sources include:

   - online retail stores
   - label sites
   - official artist discographies
   - `other online music databases <https://musicbrainz.org/doc/Other_Databases>`_

All sources have varying degrees of reliability, differing by type of music, format of release and age of release. To be sure you may often need to cross-reference between several stores or sources. Note that many sources will not distinguish between countries reliably so one should be careful that the ReleaseDate one chooses matches the :doc:`Release Country </terminology/terms/release_country>` set.

**Store-specific Hints**

   - **Amazon.com** has many :doc:`ASINs </terminology/terms/asin>` with 1990-10-25 as the release date. This is a bogus date representing when Amazon first went into operation, so if present don't enter it in MusicBrainz (the system will warn you). The older dates are also often incorrect, as they are more "when it was added on Amazon" than "when it was released".

   - **Amazon** usually has two dates on its releases, the *Original Release Date* and another *Audio CD* or *LP* date on the line above. Almost always, the top date is more likely to be correct. The bottom date usually represents the original release, which may be on a different media, have different numbers of tracks, be non-remastered etc. It can also sometimes mean the *originally announced* release date; so if the actual release gets delayed by several weeks these dates may be several weeks apart. In both cases, the top date should almost always be used; subject to a general judgement on the reliability of the Amazon information (and confirmation with another source if possible).

   - **Discogs** has extremely varied reliability of its release dates; especially where it notes down to a specific day of the month. Sometimes release countries are wrong. Please try and be especially careful to cross-check a day-specific date that is sourced from Discogs.

   - **Wikipedia** often does not say which country a release date is for; often only the home country of release. Please ensure that the date applies to the country your release is from using a second source.

   - **iTunes** often displays a release date from when the first version of an album/single was first made available to the iTunes Store as a whole, often not the same date as when other versions were released to a specific territory. Do not rely on the date shown and check other download stores from your country to verify the correct digital release date.

   - **Juno Records** often displays on the product page a date that is a week later than the actual release date (this is, however, not always the case). The store also tends to display a different date in the search results to that on the product page. It is recommended to verify dates with another store.

   - **Beatport** is fairly reliable.

   - **Bandcamp** dates are set by the artist, and sometimes refer to the first physical releases, not digital media reeditions etc. You can see when the files where actually made public by looking at the RSS feed dates.

   - **Metal-Archives** is fairly reliable on years, but month and days can be added by other users without proof and even give points for editing, creating a situation where obscure releases have very precise release dates for no reason. You should also always check out the "Additional notes" tab when there is one.

.. seealso::

   For more information regarding release dates you can review the articles on `Japanese release dates <https://reference.discogs.com/wiki/japanese-release-dates>`_ and `Global Release Day <https://wikipedia.org/wiki/Global_Release_Day>`_.
