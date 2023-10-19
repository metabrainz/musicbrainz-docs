.. MusicBrainz Documentation Project

.. https://wiki.musicbrainz.org/CD_Stub

CD Stub
=======

A CD stub is an anonymously submitted track list that contains a :doc:`disc ID </terminology/terms/disc_id>`, barcode, comment field, and basic metadata like a release title and track names.

All CD stubs are segregated from the main database and are editable by anyone (whether they are logged in or not), however, they don't benefit from core MusicBrainz features such as edit history, permanent unique identifiers (:doc:`MBIDs </terminology/terms/mbid>`), :doc:`relationships </terminology/entities/relationship>`, release information (date, country, label, etc.), and much more.

CD stubs were implemented as a means for people to easily contribute data to MusicBrainz when they are unable, or unwilling, to create an account and add a release. They also enable us to store "untrusted" metadata like the CD Baby music catalog, and to actively serve all this content without cluttering the main database.

Process
-------

The CD stub process is quite simple.

When a disc lookup is performed in :doc:`MusicBrainz Picard </products/picard>` (or any other tagger that supports MusicBrainz CD stubs) by someone that doesn't have a MusicBrainz account, and there is no match for the :doc:`disc ID </terminology/terms/disc_id>`, the user is prompted to either enter the CD as a CD stub, or to create a MusicBrainz account and add it to the main database directly. Either way, the user will be able to retrieve the data and tag their files with it right away. CD stubs are not intended to replace the regular add release process, if a user has a MusicBrainz account the expectation is that they :doc:`add a release </how-tos/add_release>` to the database.

CD stubs can also be posted using the :doc:`web service </products/web_service>`, dismissing the need for users to interact with their browser.

Once the CD stub has been entered, the data can be retrieved by Picard using the :doc:`web service </products/web_service>` for 14 days. After the 14 days, the next user to come along and request the data will be forwarded to the web site where they will review the CD stub and have the option of improving the data before retrieving it and tagging their files with it. After that user reviews the CD stub, its 14 day cycle starts over again.

**Note:** The 14 day cycle doesn't apply to users browsing the data on the website, that can be done at any time with no restriction. The cycle only applies to users requesting the data from the web service.

The goal here is to encourage people to regularly look at the data and for it to improve as people use it. At the same time, the server keeps track of how many requests any CD Stub receives and how many times it's reviewed. This flow of data gives MusicBrainz a real life view of what data is important and enables MusicBrainz editors to migrate some of the more popular CD stubs to the main database. This has proved to be a success as many CD stubs are migrated into the main database each week.
