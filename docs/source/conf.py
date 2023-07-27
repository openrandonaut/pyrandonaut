# Configuration file for the Sphinx documentation builder.

import pyrandonaut
from sphinx.locale import _

# -- Project information

project = "pyrandonaut"
copyright = "2023. OpenRandonaut"
author = "OpenRandonaut <openrandonaut@riseup.net>"
language = 'en'

version = pyrandonaut.__version__
# The full version, including alpha/beta/rc tags.
release = pyrandonaut.__version__

# -- General configuration

html_show_sourcelink = False
master_doc = "index"
suppress_warnings = ["image.nonlocal_uri"]
pygments_style = "default"

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "rtd-dev": ("https://dev.readthedocs.io/en/stable/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]


# -- Options for HTML output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

html_logo = "_static/logo.png"

html_theme_options = {
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "vcs_pageview_mode": "",
    "navigation_depth": -1,
}

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = False

# -- Options for EPUB output
epub_show_urls = "footnote"

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


# Extensions to theme docs
def setup(app):
    from sphinx.domains.python import PyField
    from sphinx.util.docfields import Field

    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
        doc_field_types=[
            PyField(
                "type",
                label=_("Type"),
                has_arg=False,
                names=("type",),
                bodyrolename="class",
            ),
            Field(
                "default",
                label=_("Default"),
                has_arg=False,
                names=("default",),
            ),
        ],
    )
