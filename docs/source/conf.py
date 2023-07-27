# Configuration file for the Sphinx documentation builder.

import pyrandonaut

# -- Project information

project = 'pyrandonaut'
copyright = u'2023. An <a href="https://github.com/openrandonaut">OpenRandonaut</a> Project'
author = 'OpenRandonaut <openrandonaut@riseup.net>'

version = pyrandonaut.__version__
# The full version, including alpha/beta/rc tags.
release = pyrandonaut.__version__

# -- General configuration

html_show_sourcelink = False    

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']



# -- Options for HTML output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

html_logo = "_static/logo.png"

html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    'navigation_depth': -1,
}

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = False

# -- Options for EPUB output
epub_show_urls = 'footnote'

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# -- Options for autodoc ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration

# Automatically extract typehints when specified and place them in
# descriptions of the relevant function/method.
autodoc_typehints = "description"

# Don't show class signature with the class' name.
autodoc_class_signature = "separated"