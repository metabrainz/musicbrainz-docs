.. MusicBrainz Documentation Project

Beginners' Guide
================

Welcome to MusicBrainz! This beginners' guide should get you started on both correcting tags in your digital music and contributing data back to MusicBrainz. If this is your first visit to this page, it might be good to read it all before diving into more advanced topics. If you want to dive right in anyway, the :doc:`basic </how-tos/_basic>` and :doc:`specific </how-tos/_specific>` how-tos are a quite good place to do so.

MusicBrainz (often abbreviated to MB) consists of three parts:

1. The web interface and its backend, the :doc:`database </musicbrainz_database/index>`.
2. The documentation (you're reading part of it!).
3. The :doc:`applications and services </products/index>`.

If you're like most users, you will probably start to tag your files with information that was already in the database (perhaps with `Picard <https://picard.musicbrainz.org>`_). But remember that MusicBrainz is user-edited, so if you find that something is missing, you can add it, and if it is wrong, you can fix it! These changes are not always applied instantly, because they pass through our voting system. Our introductions to :doc:`editing </introductions/editing>` and to :doc:`voting </introductions/voting>` will help you understand how that works.

Documentation
-------------

The documentation includes guides and how-tos, but also the definitions for :doc:`MusicBrainz terminology </terminology/index>` and the :doc:`guidelines </guidelines/index>` editors are expected to follow when editing. You don't need to memorise or even read all of the guidelines from the beginning, although there are a few important ones that deal with :doc:`titles </style_guides/titles>`, :doc:`artists </style_guides/artist>` and :doc:`releases </style_guides/release>`.

Web interface
-------------

Before making any changes to the data, you will need to `register <https://musicbrainz.org/register>`_ and then `log in <https://musicbrainz.org/login>`_. You will need to provide a verified email address so that other editors can contact you. Our `privacy policy <https://metabrainz.org/privacy>`_ makes it very clear that we don't share your data or spam you.

If you want to get used to the interface before you start editing real data, you can do so at `our test page <https://test.musicbrainz.org/>`_. Changes made there **won't be applied** to the real data, so nobody will mind you adding some junk while you get used to the editing system on MusicBrainz. Note that this page is also where new features are tested by our developers, so it might be slightly different from the standard interface… and a bit broken at times!

Definitions
-----------

When a user modifies the data in any way, that's :doc:`editing </introductions/editing>`. This is different from the wiki-like editing you might be used to from sites like Wikipedia, because most edits must go through a :doc:`voting </introductions/voting>` process before being applied.

The term :doc:`release </terminology/entities/release>` refers to a specific issuing of an album, single, compilation, etc., and includes a specific set of :doc:`recordings </terminology/entities/recording>` in a particular order. A release often has several different editions such as a digital iTunes edition, an edition with bonus tracks or a market-specific edition with only :ref:`minor differences <style_release_cover_art>` such as the legal text or price code; these should be entered as separate releases.

A :doc:`disc ID </terminology/terms/disc_id>` is a kind of signature for a CD. It contains the precise timing information for the CD and allows it to be recognised automatically. When you use :doc:`MusicBrainz Picard </products/picard>`, you can automatically retrieve the disc ID of your CD to include it in the MusicBrainz database. We have specific documentation on :doc:`how to add disc IDs </how-tos/add_disc_ids>`.

One of the fundamental aims of MusicBrainz is to offer correct and well structured information. To enforce this, we have :doc:`style guidelines </guidelines/index>` which allow us to ensure the data input by all users is accurate.

Adding a release
----------------

Adding a release is probably one of the first things you will want to do. Please note that MusicBrainz aspires to have data that is structured in a meaningful manner and as accurate as possible, so please follow the :doc:`style guidelines </guidelines/index>`!

If you have a CD, you can first see if MusicBrainz has a :doc:`disc ID </terminology/terms/disc_id>` for it and, if not, add a new disc ID (either to an existing release or while adding the release itself). For that, consult the :doc:`how-to for adding disc IDs </how-tos/add_disc_ids>`. If you have other kind of release (like a vinyl, or a digital release), or you just can't add a disc ID for some reason, you will need to search for the release by hand. Usually the best way is to search for the title of the release. If you can't find the release you have, or the only matches in MusicBrainz are reasonably different from yours (different barcode, for example), then that means you must add the CD as a new release to the database.

See our guide on :doc:`how to add a release </how-tos/add_release>`.

When submitting your new release, it helps immensely if you can provide a link to a page containing more information about the release. Please read these :doc:`tips for adding edit notes </how-tos/add_edit_notes>` and try to follow them. A good edit note is not only useful in the moment of adding a release, but can also prove its use years later when some other user tries to find more information about it. Another way of providing more information about a release, which is especially useful if it's obscure and you cannot find any links, is to upload scans or other artwork from it, as explained in :doc:`How to Add Cover Art </how-tos/add_cover_art>`.

While we welcome bootlegs, we discourage adding home-made compilations or mixtapes. These kinds of releases are not widely available and any information about them is typically only useful to the individual who created them. Releases such as these are usually removed from our database. Information about pirate releases is allowed if they are not equivalent to an official release: a direct digital rip of an official CD should not be added, but a pirate release including demos or remixes in addition to the content of the official CD release can be. If you do add pirate releases, please do not add any download / purchase links to them; we want to document them, but not actively promote piracy.

Pending/open edits
------------------

When editing MusicBrainz, be careful about edits that are open. If there is a pending edit (usually highlighted in yellow) you should check if it is already doing what you wanted to do. If so, you don't need to do anything - except voting Yes so it will be applied sooner! If it is different and you don't agree with it, you probably should say so in an :doc:`edit note </terminology/terms/edit_note>`. Make sure you follow the :doc:`Code of Conduct </guidelines/code_of_conduct>` while doing so!

If you realise you've made a mistake while editing, and your edit is still open, **don't enter a remove edit to undo it!** You should :doc:`cancel your previous edit </how-tos/cancel_edit>` and make your changes again. The exception to this is if you make a mistake when adding a release. In this case, it is usually more efficient to leave your edit as is and create a follow up edit correcting your mistake.

Guides
------

We have some basic guides for adding :doc:`artists </how-tos/add_artist>`, :doc:`relationships </how-tos/add_relationship>` and :doc:`releases </how-tos/add_release>`.

And of course, you can read our :doc:`basic </how-tos/_basic>` and :doc:`specific </how-tos/_specific>` how-tos on different matters.

Software
--------

You can `download MusicBrainz Picard <https://picard.musicbrainz.org/downloads>`_, our tagger, to tag your digital files and submit :doc:`disc IDs </terminology/terms/disc_id>` to MusicBrainz. If you have questions, check the `Picard User Guide <https://picard-docs.musicbrainz.org>`_. You can install all kind of `plugins <https://picard.musicbrainz.org/plugins>`_ for it too!

Discussion
----------

Of course, remember that if you can't find an answer to some doubt in the documentation, you can (should!) :doc:`ask about it </miscellaneous/communication>`.
