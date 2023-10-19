.. MusicBrainz Documentation Project

.. https://wiki.musicbrainz.org/Label/FAQ

Labels
======

How do you "relate" a label and a release?
------------------------------------------

When adding or editing a :doc:`release </terminology/entities/release>`, you can additionally specify one or more pairs of :doc:`label </terminology/entities/label>` and :doc:`catalog number </terminology/terms/catalog_number>`, and a :doc:`barcode </terminology/terms/barcode>`. This is a core relation between labels and releases.


How to handle autoreleases?
---------------------------

In some cases, artists "autoproduce" and "autorelease" their own records. As long as an imprint is possible to positively identify, it should be used as a label entry. If there's no such thing, or if the creation of such a label entry is disputable, you should use the :ref:`Special Purpose Label <style_unknown_and_untitled_special_purpose_label>` **[no label]**.


How to handle White Labels? (and other unlabeled releases)
----------------------------------------------------------

Like for autoreleases, you should use the :ref:`Special Purpose Label <style_unknown_and_untitled_special_purpose_label>` **[no label]**.


Can an imprint and the company that controls it have the same name?
-------------------------------------------------------------------

Yes, definitely. Actually, a company "A" may sell its own imprint "A" to another company "B" and continue to exist as company "A", while the imprint is being operated by company "B"… This can result in really confusing situations… Usually though, editors in MusicBrainz will deal with imprints exclusively (which *is* the information available on sleeves).

In the old days, there was actually no clear distinction between an imprint and the company that controlled it. Nowadays though, things got much more complex. Whether or not something requires two distinct entries in the database is up to the editor, and should be decided on a case by case basis (though we think that in most cases, just one entry is enough).


Are "collections" valid imprints?
---------------------------------

This is a difficult question that can't be solved generally, but only on a case by case basis. Hence, the use of a label entry for collections names must be made with extra-care. Definitely, one must not use collection names printed on the front cover as a label name, but only if the collection name is used in place of the label name (usually on the back cover, next to a catalog number), and is really used by the producing label as is. For example, the "Verve Jazz Masters" releases are from label "Verve", dot, and "Jazz Masters" should be part of the release name. On the other hand, "Original Jazz Classics" is an imprint, owned by label "Fantasy".
