# Contributing to the MusicBrainz Documentation

This repository contains the curated parts of the documentation, including the Style Guide, database structure, and database and web server installation instructions.  This information is reviewed and approved by the MusicBrainz project team prior to being accepted for inclusion on the MusicBrainz Documentation portion of the ReadTheDocs site.

Non-curated documentation, such as user-provided hints, tips and guides, is found on the [MusicBrainz wiki](https://wiki.musicbrainz.org/Main_Page) and can be entered and updated by the users directly without prior review and approval by the MusicBrainz project team.

If you want to contribute corrections or new material to this curated documentation, there are a couple of different ways to submit your contributions, which are described in the "Submitting" sections below.

The source documentation has been developed in the English language. Translation into other languages is being managed through a [Weblate server](https://translations.metabrainz.org/). This provides a number of benefits including translation tools and automated checking and processing. Any help in providing or reviewing translations is greatly appreciated. That helps to make the information available to a greater number of MusicBrainz users. Please [contact us](mailto:support@metabrainz.org?subject=MusicBrainz%20Documentation%20Help) if you are interested in helping to work on translating the documentation to other languages, or would like to contribute in some other manner.

Thank-you for considering contributing to this documentation project.

### Submitting via pull requests

If you are comfortable developing ReStructuredText format files, and are familiar with [Pull Requests](https://github.com/metabrainz/picard-docs/pulls) on GitHub, you can submit the requested changes to the documentation source files in that form. This is the preferred method, because it provides a clear way for the changes to be reviewed and discussed.

If you are submitting your changes via a pull request, please make the request against the **master** branch for review and implementation.  All documentation is included in the form of restructured text files (\*.rst) found in the appropriate source directory such as "guidelines", "faq", "how-tos" and "style_guides".  These directories also contain some subdirectories to help organize the information into logical groups.  The `index.rst` file contains the top level document index for the HTML output. [Sphinx](https://www.sphinx-doc.org/) is used to produce the final output documents.

Please check your submission for things like spelling and punctuation, and please remove any trailing whitespace from the lines.

The `setup.py` file provides utilities for performing some basic checks of the project files, and to build the website files on your system for local testing.  We encourage you to run the checks and view your changes on the local html files to ensure they are correct and as-expected prior to submitting the pull request.

### Submitting via issue tickets

If you are not so comfortable developing ReStructuredText format files or preparing GitHub pull requests, you can create a ticket regarding the [MusicBrainz Server](https://tickets.metabrainz.org/issues/?jql=project+%3D+MBS+AND+component+%3D+Documentation+AND+resolution+%3D+Unresolved) or the [Style Guide](https://tickets.metabrainz.org/issues/?jql=project+%3D+STYLE+AND+resolution+%3D+Unresolved) requesting the change (if the issue does not already exist) and attach your suggestions to it, either as an attached text file or within the discussion comments on the Issue. This way, someone can convert your suggestions into the appropriate (\*.rst) file changes and submit a pull request with the changes on your behalf.
