.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Style/Relationships/URLs

URLs
====

Status: **Official Style Guideline**

This page outlines general guidelines for adding relationships which link an entity to a URL. Many relationships also have their own guidelines which, should they conflict, supersede the ones on this page.

Which URLs are allowed?
-----------------------

**Multiple URLs for the same relationship type**

In general, any relevant URLs can be added, there is no technical limit to the number which can be added. However, some relationship types can potentially have hundreds of valid links and you should not try to link to every possible site in these cases.

Some examples of how this applies to different relationship types:

    - :doc:`Fan pages </relationships/artist-url/fan_pages>`: pick the ones that are most useful as a resource for MusicBrainz users and avoid sites whose unique content is only a few obscure bits and pieces.
    - :doc:`Online communities </relationships/artist-url/online_communities>`: pick the more active ones, or those preferred and/or supported by someone involved with the entity.
    - :doc:`Mail order </relationships/artist-url/mail_order>` and :doc:`download </relationships/artist-url/download>` relationships: Don't try to link widely available releases to every online store. The mail order and download relationships are most useful when a release is only available from particular stores.
    - :doc:`Wikipedia </relationships/artist-url/wikipedia>`: If possible, link to :doc:`Wikidata </relationships/artist-url/wikidata>` instead, which serves as a bridge for all languages. If no Wikidata item exists, only link to English and languages which are relevant to the artist (usually the artist's native languages).
    - :doc:`Artist images </relationships/artist-url/artist_images>`, :doc:`place images </relationships/artist-url/place_images>` and :doc:`label logos </relationships/artist-url/label_logos>`: Don't link to the same image on multiple hosts.


**Restricted pages**

Pages do not have to be completely open, as long as it is accessible to the general internet population. Password-protected sites are frowned upon, but if the page is really worth linking to, so long as the website allows free registration, the link is allowed.


**When not to link**

Some sites discourage systematic linking. Please do not add links if it would be counter to the wishes of the other site.

When linking to a page where you can download, stream or get music via mail-order, the page must respect copyright law. Do NOT link to pages which contain pirated material. There are two exceptions to this guideline:

    1. Bootleg recordings of concerts.
    2. Derivative works such as mash-ups or unauthorized remixes (a well-known example of this is Danger Mouse's "The Grey Album").


Which URL to use
----------------

Many sites have multiple pages, so there may be several URLs which would work. URLs which are simple and unlikely to change are preferred. Avoid linking to websites' search pages. The URL should still be specific to the entity being linked, so please do not link to top level domains when a site has information about numerous artists, releases, etc.

**Examples**

    - The official homepage for `Nine Inch Nails <https://musicbrainz.org/artist/b7ffd2af-418f-4be2-bdd1-22f8b48613da>`_ is http://nin.com/ (**not** http://nin.com/index.php, as that is more likely to change)
    - The Wikipedia page for `George Harrison <https://musicbrainz.org/artist/42a8f507-8412-4611-854f-926571049fa0>`_ is http://en.wikipedia.org/wiki/George_Harrison (**not** http://www.wikipedia.org/, because Wikipedia contains information about numerous different things)
    - The Amazon URL for `With Teeth <https://musicbrainz.org/release/963b0e2e-d6cb-4482-a600-0ad167e5bff2>`_ is http://www.amazon.com/gp/product/B0008ISM40 (**not** http://www.amazon.com/ because Amazon sells lots of different releases)


**Linking to images**

When linking to images, link directly to image files, not to pages containing pictures.


**Linking to pages where you can get music**

The URL should also be as close as possible to a direct link to just the specific entity which is being linked.


**Standardised URLs**

For many sites, we use a standardised URL format. In most cases, the URL will be automatically formatted correctly.


Which entity to link to
-----------------------

The URL should be linked to the most appropriate entity.

**Examples**

    - http://www.amazon.com/gp/product/B0008ISM40 is linked to `With Teeth <https://musicbrainz.org/release/963b0e2e-d6cb-4482-a600-0ad167e5bff2>`_ and not `Nine Inch Nails <https://musicbrainz.org/artist/b7ffd2af-418f-4be2-bdd1-22f8b48613da>`_. The URL is a purchase page for a specific release and not for the artist in general.
    - http://www.metallica.com/ is not the official homepage of `Lars Ulrich <https://musicbrainz.org/artist/e2190b35-1181-44f6-8587-4c04123a6f30>`_. The site is for the group `Metallica <https://musicbrainz.org/artist/65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab>`_, not the specific person.


Which relationship types to use
-------------------------------

The relationship type used should be the one which most closely matches. If there is a specific relationship type for the site, that relationship type should be used instead of generic types.

**Examples**

    - An article on Wikipedia should be linked using the :doc:`Wikipedia </relationships/artist-url/wikipedia>` relationship type and not the :doc:`biography </relationships/artist-url/biography>` relationship type.
    - A page on Amazon should use the :doc:`Amazon </relationships/artist-url/amazon>` relationship type rather than the :doc:`discography </relationships/artist-url/discography>` relationship type.


When to remove
--------------

In most cases, if a URL was correct but no longer works, it's best to mark the relationship as ended rather than fully removing the URL. This allows us to try and access an archived version of the URL, and even if that doesn't exist it can be useful as a way to know that other page listing the same URL referred to the same artist. Since URL relationships marked as ended are not displayed as links, it's generally safe to keep the URL even if it points to some other content now.

There are still cases where a URL should certainly be removed. If the URL was never correct in the first place (was added to the wrong entity, for example), it obviously shouldn't be kept. Lyrics URLs can only be linked if the site has a license and is approved, so they should be removed once the license no longer applies, even if archived versions exist. And if a URL is known to have been taken over and now contains malware, it's safer to remove it to avoid risk to other editors.


Restricted relationships
------------------------

For some of our relationships, only certain sites are permitted. For these, links to sites which are not on the whitelist must not be added. These relationships are:

    - :doc:`Lyrics </relationships/artist-url/lyrics>` (:doc:`whitelist </relationships/artist-url/lyrics_whitelist>`)
    - :doc:`Other Databases </relationships/artist-url/other_databases>` (:doc:`whitelist </relationships/artist-url/other_databases_whitelist>`)
