# -*- coding: utf-8 -*-
#
# conan documentation build configuration file, created by
# sphinx-quickstart on Wed Apr 27 13:10:21 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
from shutil import copyfile
import json

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

sys.path.insert(0, os.path.abspath('./_themes'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'conan',
    'sphinxcontrib.spelling',
    'sphinx_sitemap',
    'notfound.extension',
]

# The short X.Y version.
version = "1.25"
# The full version, including alpha/beta/rc tags.
release = u'1.25.2'

dir_path = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(os.path.join(dir_path, "versions.json")):
    data = {"master": version}
else:
    with open("versions.json") as f:
        json_data = f.read()
        data = json.loads(json_data)
versions_dict = data

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

html_context = {
    "versions": versions_dict,
    "current_version": version,
    "display_github": True, # Integrate GitHub
    "github_user": "conan-io", # Username
    "github_repo": "docs", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/" # Path in the checkout to the docs root
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'conan'
copyright = u'2016-2019, JFrog'
author = u'The Conan team'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '**/site-packages']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------
import conan

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'sphinx_rtd_theme'
html_theme = "conan"
html_theme_path = conan.get_html_theme_path()


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
  "base_url": "https://docs.conan.io/en/latest/",
}

# for sphinx-sitemap
html_baseurl = html_theme_options['base_url']

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/conan-logo.png"

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/conan-favicon.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'conandoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'conan.tex', u'Conan Documentation',
     author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "_static/conan-logo.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'conan', u'Conan Documentation',
     author, 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'conan', u'Conan Documentation',
     author, 'conan', 'Documentation of Conan C/C++ Package Manager',
     'Technology'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
#epub_basename = project

# The HTML theme for the epub output. Since the default themes are not
# optimized for small screen space, using the same theme for HTML and epub
# output is usually not wise. This defaults to 'epub', a theme designed to save
# visual space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files that should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the Pillow.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True

# A list of regular expressions that match URIs that should not be checked when doing a linkcheck build.
linkcheck_ignore = [r'http://localhost:\d+', r'https://github.com/conan-io/conan/pull/\d+', r'https://github.com/conan-io/docs/pull/\d+']
linkcheck_workers = 15
linkcheck_timeout = 90
linkcheck_retries = 2

# Not Found
notfound_pagename = 'Page Not Found'


# copy legacy redirects
def copy_legacy_redirects(app, docname): # Sphinx expects two arguments
    # FILL in this dicts the necessary redirects
    redirect_files = {
        "creating_packages/package_dev_flow.html": "../developing_packages/package_dev_flow.html",
        "conan1.0.html": "faq/conan1.0.html",
        "mastering/python_requires.html": "../extending/python_requires.html",
        "mastering/version_ranges.html": "../versioning/version_ranges.html",
        "mastering/revisions.html": "../versioning/revisions.html",

        "integrations/cmake.html": "build_system/cmake.html",
        "integrations/makefile.html": "build_system/makefile.html",
        "integrations/ninja.html": "build_system/ninja.html",
        "integrations/pkg_config_pc_files.html": "build_system/pkg_config_pc_files.html",
        "integrations/boost_build.html": "build_system/boost_build.html",
        "integrations/b2.html": "build_system/b2.html",
        "integrations/qmake.html": "build_system/qmake.html",
        "integrations/premake.html": "build_system/premake.html",
        "integrations/make.html": "build_system/make.html",
        "integrations/qbs.html": "build_system/qbs.html",
        "integrations/meson.html": "build_system/meson.html",
        "integrations/scons.html": "build_system/scons.html",
        "integrations/gcc.html": "build_system/gcc.html",

        "integrations/docker.html": "cross_platform/docker.html",
        "integrations/qnx_neutrino.html": "cross_platform/qnx_neutrino.html",
        "integrations/emscripten.html": "cross_platform/emscripten.html",

        "integrations/visual_studio.html": "ide/visual_studio.html",
        "integrations/xcode.html": "ide/xcode.html",
        "integrations/android_studio.html": "ide/android_studio.html",
        "integrations/clion.html": "ide/clion.html",
        "integrations/youcompleteme.html": "ide/youcompleteme.html",

        "integrations/git.html": "vcs/git.html",

        "integrations/jenkins.html": "ci/jenkins.html",
        "integrations/travisci.html": "ci/travisci.html",
        "integrations/appveyor.html": "ci/appveyor.html",
        "integrations/gitlab.html": "ci/gitlab.html",
        "integrations/circleci.html": "ci/circleci.html",
        "integrations/azure_devops.html": "ci/azure_devops.html",

        "integrations/other.html": "custom.html",
        "integrations/pylint.html": "linting.html",

    }

    redirect_template = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="1; url=%s" />
</head>
</html>
"""

    if app.builder.name == 'html':
        for html_src_path, dst_path in redirect_files.items():
            target_path = app.outdir + '/' + html_src_path
            html = redirect_template % dst_path
            if not os.path.exists(os.path.dirname(target_path)):
                os.makedirs(os.path.dirname(target_path))
            with open(target_path, "w") as f:
                f.write(html)

def setup(app):
    app.connect('build-finished', copy_legacy_redirects)
