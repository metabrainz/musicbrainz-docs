.. MusicBrainz Documentation Project

.. https://musicbrainz.org/doc/AcoustID

AcoustID
========

`AcoustID <https://acoustid.org/>`_ is an `acoustic fingerprint <https://wikipedia.org/wiki/acoustic_fingerprint>`_ system built entirely on open-source technology.

In MusicBrainz
--------------

Each recording page in the MusicBrainz web interface has a Fingerprint tab, listing the AcoustIDs associated with the recording. Every AcoustID listed has a “link” or “unlink” link action associated with it. If you are certain that an AcoustID does not belong to a recording, you can use “unlink” to disable the association between the MusicBrainz recording and the AcoustID. This will prevent Picard from suggesting that recording when it scans an audio file and finds that AcoustID. If you find that someone else has disabled the AcoustID incorrectly, you may use “link” to reactivate this association.

To see more information about the AcoustID, including durations of submitted fingerprints, visualizations of the fingerprint, and a list of associated MusicBrainz :doc:`recordings </terminology/entities/recording>`, click on the AcoustID.

.. note::

   Using the link/unlink actions requires you to enter your MusicBrainz credentials into a different website. If you are not comfortable doing this, please do not use these actions.


In Picard
---------

If your files do not have :doc:`MBIDs </terminology/terms/mbid>` in their tags, you can use :doc:`Picard </products/picard>` to submit AcoustID fingerprints while you tag them.

**Configuring Picard**
   Go to ":menuselection:`Options --> Options… --> Fingerprinting`", select *Use AcoustID* under the *Audio Fingerprinting* section.

   If you want to be able to submit fingerprints, enter your API key. If you don't already have one, click :guilabel:`Get API key…`, or you can get it from `acoustid.org <https://acoustid.org/api-key>`_.

**Using AcoustIDs in Picard: Scanning and submitting AcoustIDs**
   Select an unmatched file (or cluster) and press the :guilabel:`Scan` button. Picard will calculate the fingerprint of the file and look it up on the AcoustID server, trying to find an ID corresponding to the file's fingerprint. If the fingerprint yields a match, and it is already linked to a MusicBrainz ID, the track will be matched. You don't need to submit it! If it does not get a MB or AcoustID match, the fingerprint stays associated with the file in memory, but the file stays in the left-hand pane. Now you must manually match the track using another mechanism (e.g. Cluster/Lookup or manual search on the website).

   .. image:: /images/picard_submit_accoustid.png
      :width: 100%

   Once the file is matched to MusicBrainz, you can press the :guilabel:`Submit AcoustIDs` button to send the information to AcoustID, thus helping future users.

   .. seealso::

      For additional information about using MusicBrainz Picard, please see the `Picard User Guide <https://picard-docs.musicbrainz.org>`_.


The AcoustID Fingerprinter
--------------------------

If your files already have MBIDs stored in their tags, just use the AcoustID Fingerprinter (you can download it from the `AcoustID website <https://acoustid.org/fingerprinter>`_).

Open the Fingerprinter and input your API key in the key field. If you don't have an API key, press :guilabel:`Get API key` to get one. Select the folders that contain the files you want to fingerprint and press :guilabel:`Fingerprint`: your files will be fingerprinted and the info submitted to AcoustID. You're done!
