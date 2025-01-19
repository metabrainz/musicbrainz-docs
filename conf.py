"""Configuration file for the Sphinx documentation builder.
"""

# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import datetime
import glob
import os
import sys


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('_extensions'))

# import sphinx_rtd_theme
# import picard_theme

this_year = datetime.datetime.now().year
copyright_year = str(this_year) if this_year == 2023 else f'2023-{this_year}'

# -- Project information -----------------------------------------------------

project = 'MusicBrainz'

# # The full version, including alpha/beta/rc tags (must start with a 'v' and not contain any spaces)
# version = 'v2.9.2'
# Default to the published date for now until a versioning format has been decided.
version = datetime.datetime.now().strftime("%Y-%m-%d")

author = 'MusicBrainz Team'
copyright = 'This documentation is licensed under CC0 1.0.'     # pylint: disable=redefined-builtin

# -- Language information ----------------------------------------------------

default_language = 'en'
# supported_languages = [
#     ('en', 'English'),
#     ('fr', 'Français'),
#     # ('de', 'Deutsch'),
#     # ('es', 'Español'),
# ]

# -- Base file name for PDF and EPUB files -----------------------------------

base_filename = 'musicbrainz'


# -- Notice for Back of Title Page in LaTex Output ---------------------------

my_notice = r'''\vspace*{\fill}
MusicBrainz User Guide is licensed under CC0 1.0. To view a copy of
this license, visit https://creativecommons.org/publicdomain/zero/1.0
\vspace{0.1\textheight}'''


# -- General configuration ---------------------------------------------------

# The master toctree document.
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "recommonmark",
    "notfound.extension",
    # "taggerscript",
    "sphinxcontrib.youtube",
    # "sphinx_rtd_theme",
    # "picard_theme",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    '_images',
    '_ignored',
    '_locale',
    'Thumbs.db',
    '.DS_Store',
    'README.md',
    'html',
    'docs',
    '.git',
    '.github',
    'images',
    'testing',
    'README.md',
    'TODO.md',
]


# -- Options for Internationalization ----------------------------------------

language = default_language
locale_dirs = ['_locale']
gettext_compact = False
# gettext_compact = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
# html_theme = "picard_theme"
# html_theme = "basic"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html_js_files = ['/version_links.js']

# # Major.minor portion of the version number used for naming the download files
# major_minor = re.match(r'^(v[0-9]+\.[0-9]+)', version).group(1)

# html_context = {
#     'extra_css_files': [
#         '_static/css/extra.css',
#     ],
#     'default_language': default_language,
#     'supported_languages': supported_languages,
#     'major_minor': major_minor,
#     'release': version,
# }

html_context = {
    'extra_css_files': [
        '_static/css/mb-specific.css',
    ],
}

html_favicon = '_static/musicbrainz-icon.png'

html_copy_source = False


# -- Options for LaTeX / PDF output ------------------------------------------

release = version   # For display on cover of PDF document

latex_documents = [
    ('pdf', f'{base_filename}.tex', project, '', 'manual', False),
    # ('pdf', '{0}.tex'.format(base_filename), project, 'Edited by Bob Swift', 'manual', False),
    # ('pdf', '{0}.tex'.format(base_filename), project, '', 'howto', False),
]

# latex_toplevel_sectioning = 'part'
# latex_toplevel_sectioning = 'section'     # Use with 'howto' document style
# latex_toplevel_sectioning = 'chapter'

# latex_show_urls = 'inline'
# latex_show_urls = 'footnote'
latex_show_urls = 'no'

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    # 'preamble': '\\hyphenation{Music-Brainz}',
    'preamble': r'''\hyphenation{Music-Brainz}
\usepackage{fontspec}
\setmainfont{DejaVu Sans}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
\newcommand\sphinxbackoftitlepage{''' + my_notice + r'''}
''',
    'extraclassoptions': 'openany',
    # 'maketitle': r'\newcommand\sphinxbackoftitlepage{<Extra material>}\sphinxmaketitle',
    # 'maketitle': r'\newcommand\sphinxbackoftitlepage{<Extra material>}\sphinxmaketitle',
}

latex_domain_indices = True


# -- Options for epub output ------------------------------------------

epub_basename = base_filename
epub_theme = 'epub'

# Metadata included in the epub file.
# epub_title = f'{project} User Guide ({major_minor})'
epub_title = f'{project} User Guide ({version})'
epub_description = 'A User Guide for MusicBrainz.'
epub_author = 'MusicBrainz Team'
epub_contributor = 'Members of the MusicBrainz Community'
epub_publisher = 'MetaBrainz Foundation'
epub_uid = 'MusicBrainzUserGuide'

epub_tocdepth = 3
epub_tocscope = 'includehidden'

epub_cover = ('_static/musicbrainz_logo_256.png', 'epub-cover.html')
epub_guide = (('cover', 'epub-cover.xhtml', 'Cover Page'),)

# epub_show_urls = 'inline'
# epub_show_urls = 'footnote'
epub_show_urls = 'no'

epub_use_index = True

epub_post_files = [
    ('genindex.xhtml', 'INDEX'),
]


def _exclude_files_helper():
    excludes = [
        '404.xhtml',
        'index.xhtml',
        'not_found.xhtml',
        'pdf.xhtml',
        'examples/examples.xhtml',
    ]

    for filepath in glob.glob('tutorials/v_*'):
        if filepath.endswith('.rst'):
            excludes.append(filepath[:-3] + 'xhtml')

    return excludes


epub_exclude_files = _exclude_files_helper()
