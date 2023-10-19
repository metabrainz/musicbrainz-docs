.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/Label/Type

Label Type
==========

Description
-----------

This field describes what is the main activity of a :doc:`Label </terminology/entities/label>`.

The values may be:

   - **imprint:** should be used where the label is just a logo (usually either created by a company for a specific product line, or where a former company’s logo is still used on releases after the company was closed or purchased, or both)

      - example: `RCA Red Seal <https://musicbrainz.org/label/28ad74dd-19f4-449c-bf9c-266918cefd6a>`_

   - one of the "production" types:

      - **original production:** should be used for labels producing entirely new releases

         - example: `Riverside Records <https://musicbrainz.org/label/19ea67ec-7a8c-4a25-8cb7-f25a785f8cc4>`_

      - **bootleg production:** should be used for known bootlegs labels (as in "not sanctioned by the rights owner(s) of the released work")

         - example: `Charly Records <https://musicbrainz.org/label/a754ad77-2842-4ed4-a6e7-fb6b1fdc7f40>`_

      - **reissue production:** should be used for labels specializing in catalog reissues

         - example: `Rhino <https://musicbrainz.org/label/c4f2cf49-b57c-4cc1-8061-f54400704ac4>`_

   - **distributor:** should be used for companies mainly distributing other labels production, often in a specific region of the world

      - example: *ZYX*, which distributes in Europe most jazz records in the `Concord Music Group <https://musicbrainz.org/label/0dd8c586-acc3-46f8-bd97-db1d3ce089fc>`_ catalog.

   - **holding:** should be used for holdings, conglomerates or other financial entities whose main activity is not to produce records, but to manage a large set of recording labels owned by them

      - example: `Concord Music Group <https://musicbrainz.org/label/0dd8c586-acc3-46f8-bd97-db1d3ce089fc>`_

   - **rights society:** A rights society is an organization which collects royalties on behalf of the artists. This type is designed to be used with the :doc:`rights society relationship type </relationships/label-release/rights_society>` rather than as a normal release label.

      - example: `GEMA <https://musicbrainz.org/label/50ce279e-ba41-4e82-a4b2-85ed2e926f58>`_


Additional Information
----------------------

**Multiple types**

While most cases are pretty straightforward, there may be some where a label apparently belong to two or more different types. To some extent, the problem is similar with the releases type. Whenever that happens, you should decide based on what constitutes the **main** activity type of the label. While searching, you might discover that the label has different subdivisions, each handling a different activity (as an example, think about the recording label *Verve*, and the holding *Verve Music Group*). Ultimately, if there's still an ambiguity, you should use the an :doc:`annotation </terminology/terms/annotation>` to provide with more detailed information.

**Imprint vs. company**

It is extremely common that a logo is shared with its company name. There is no need to create separate 'Imprint' and 'Original Production' labels in this case. If the logo ever needs to be split later for some reason (e.g. because the company was bought out and the imprint is used by a different company), it can be done at that time. In this case, the name of the imprint should be as it appears in the imprint (logo), and the disambiguation comment should mention how the company name appears when not printed as a logo. example: `JADE <https://musicbrainz.org/label/73ed08a3-0a82-4d05-a00d-08a9bd10fad8>`_ (the logo is printed as *JADE*, and the company is printed as "*JADE music*" or "*Editions JADE*"

**Labels types shifting during history**

Some labels have a long and troubled life, and change their main activity (say, from original to reissue, to holding). There's no way at that time to handle or properly represent that. Again, for anything that complex, use an annotation.

If you really can't decide on a type yourself, look at the releases list for that label, count the compilations, count the albums, count the bootlegs, compare, choose.

In all cases, remember the label type is a convenient indication at best, and that things should be kept simple.

**Bootlegs**

The bootleg type should be handled with some care, as legal issues are not usually trivial, and may even be impossible to sort out (think about the *Charles Mingus* "bootlegs" issued by the as-official-as-it-can-be French *INA*). Ultimately, you should not mark a company as bootleg just because one of its release is marked as such.
