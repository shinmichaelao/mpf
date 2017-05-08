#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sphinx-doc config file

import sys
import os
import shutil
import time

from copy import copy

import sphinx_rtd_theme
import git
from sphinx.ext.autosummary import Autosummary
from sphinx.ext.autosummary import get_documenter
from docutils.parsers.rst import directives
from sphinx.util.inspect import safe_getattr

sys.path.insert(0, os.path.abspath(os.pardir))

from mpf.core.utility_functions import Util
import mpf._version
from mpf.core.config_processor import ConfigProcessor

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinxcontrib.napoleon',
    'sphinx.ext.autosummary',
]

templates_path = ['_templates']

source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# The short X.Y version.
version = mpf._version.__short_version__
# The full version, including alpha/beta/rc tags.
release = mpf._version.__version__

# General information about the project.
project = 'Mission Pinball Framework v{} API'.format(version)
copyright = '2013-%s, The Mission Pinball Framework Team' % time.strftime('%Y')
author = 'The Mission Pinball Framework Team'

# dev warning box will be shown in HTML builds for the following GitHub branch
# names:
branches_for_dev_warning = ['dev']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

todo_include_todos = True

numpydoc_show_inherited_class_members = False

autodoc_default_flags = [
         # Make sure that any autodoc declarations show the right members
         "members",
         # "inherited-members",
         # "private-members",
         "show-inheritance",
]


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
html_title = 'Mission Pinball Framework API v{}'.format(version)

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'MPF API v{}'.format(version)

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or
# 32x32
# pixels large.
html_favicon = '_static/images/icons/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr', 'zh'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'MPFAPIdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',

    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'MPFAPI.tex', 'MPF API Documentation',
     'The Mission Pinball Framework Team', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'mpfapi', 'MPF API Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False

# -- Show warnings for dev branches in HTML docs --------------------------

# If this is running on ReadTheDocs.org, the context dict will be overwritten
# by theirs which will contain the propoer branch name (since the git command
# doesn't work there.

context = dict()

try:
    context['github_version'] = git.Repo('..').active_branch.name
except:
    context['github_version'] = None


def setup(app):
    app.add_stylesheet('mpf.css')
    RstBuilder().build_rst_files()

    # We need to do this in the setup() function since ReadTheDocs will append
    # the context dict to the end of conf.py which means we don't have the
    # populated value at the global context yet, so we need to do it here.

    if globals()['context']['github_version'] in branches_for_dev_warning:

        globals()['rst_prolog'] = '''
        
        .. only:: html
        
           .. warning::
           
              **This is the API reference for an unreleased version of MPF!**
        
              This is the API for MPF |version|, which is the "dev" (next)
              release of MPF that is a work-in-progress. Use the "Read the Docs"
              link in the lower left corner to view the API docs for the
              version of MPF you're using.
        
        '''


class RstBuilder(object):

    def __init__(self):

        self.dest_folder = 'mpf'

        self.mpfconfig = ConfigProcessor.load_config_file(os.path.join(
            os.pardir, 'mpf', 'mpfconfig.yaml'), 'machine')

        self.doc_sections = dict()
        self.index_entries = dict()
        self.templates = dict()

        self.populate_doc_sections()
        self.get_templates()

    def populate_doc_sections(self):

        self.doc_sections['machine'] = self.mpfconfig['mpf']['core_modules']

        self.doc_sections['config_players'] = dict()

        for name, module_ in self.mpfconfig['mpf']['config_players'].items():
            self.doc_sections['config_players'
                              ]['{}_player'.format(name)] = module_

        self.doc_sections['platforms'] = self.mpfconfig['mpf']['platforms']

        for plugin in Util.string_to_list(self.mpfconfig['mpf']['plugins']):
            name = plugin.split('.')[-2]
            self.doc_sections['machine'][name] = plugin

        self.doc_sections['devices'] = dict()

        for device in self.mpfconfig['mpf']['device_modules']:
            device_cls = Util.string_to_class(device)
            name = device_cls.collection
            self.doc_sections['devices'][name] = device

        self.doc_sections['modes'] = dict()

        for name in [x for x in
                     os.walk(os.path.join(os.pardir, 'mpf', 'modes'))][0][1]:

            if name.startswith('__'):
                continue

            class_name = ''.join([x.capitalize() for x in name.split('_')])

            self.doc_sections['modes'][name] = (
                'mpf.modes.{0}.code.{0}.{1}'.format(name, class_name))

        # populate the index entries

        for name in self.doc_sections.keys():
            self.index_entries[name] = list()

    def get_templates(self):
        for name in self.doc_sections.keys():
            with open(os.path.join(
                    templates_path[0], '{}.rst'.format(name)), 'r') as f:
                self.templates[name] = f.read()

    def build_rst_files(self):
        print('Building RST files from templates')

        try:
            shutil.rmtree(self.dest_folder)
        except FileNotFoundError:
            pass

        os.makedirs(self.dest_folder)

        for section, items in self.doc_sections.items():
            for name, module_ in items.items():
                self.create_rst_file(section, name, module_)

        self.write_index()

    def create_rst_file(self, section, name, module_):
        this_rst = copy(self.templates[section])

        file_name = this_rst.split('\n')[0].format(name=name)

        file_name = file_name.replace('[', '.')

        for char in "''*]":
            file_name = file_name.replace(char, '')

        if file_name[-1] == '.':
            file_name = file_name[:-1]

        with open(os.path.join(self.dest_folder, '{}.rst'.format(file_name)),
                  'w') as f:
            f.write(this_rst.format(
                name=name,
                module_underline='=' * (len(this_rst.split('\n')[0]) +
                                        len(name) - 6),
                full_path_to_class=module_,
                article='an' if name[0] in ('a', 'e', 'i', 'o', 'u') else 'a',
                cap_name=name.capitalize()))

        self.index_entries[section].append((name, file_name))

    def create_rst_file_list(self, file_list):
        file_list.sort()

        final_string = str()

        for name, file in file_list:
            final_string += '   {0} <{1}/{2}>\n'.format(name, self.dest_folder,
                                                        file)

        return final_string

    def write_index(self):

        with open(os.path.join(templates_path[0], 'index.rst'), 'r') as f:
                template = f.read()

        string_indices = dict()
        for section, files in self.index_entries.items():
            string_indices[section] = self.create_rst_file_list(files)

        template = template.format(**string_indices)

        with open('index.rst', 'w') as f:
            f.write(template)
