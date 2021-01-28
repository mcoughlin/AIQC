"""
# Dependencies. 
brew install pandoc
pip install nbsphinx, sphinx_copybutton, sphinx_rtd_theme, ipython

# Make after changes.
$ cd aiqc/docs
$ make html

# Then you can open 'aiqc/docs/_build/html' files in a browser.
# pip install sphinx-autobuild # Watch files instead of `make html`

# The notebooks and images all get duplicated. So after lots of changes, 
delete the `/_build` and rerun `make html`.
"""

# -- Project information -----------------------------------------------------
project = 'AIQC'
copyright = '2020, Team AIQC'
author = 'Team AIQC'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import sphinx_rtd_theme

# https://nbsphinx.readthedocs.io/en/0.8.0/
# These are pip packages. See `docs/requirements.txt` 
# Which is called by `.readthedocs.yml`
extensions = [
	'nbsphinx'
	, 'sphinx_copybutton'
	, 'sphinx_rtd_theme'
]

# https://nbsphinx.readthedocs.io/en/0.7.0/usage.html#suppress_warnings
suppress_warnings = [
    'nbsphinx',
]

html_theme = "sphinx_rtd_theme"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
# nbsphinx automatically excludes '.ipynb_checkpoints'


# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_css_files
# Create a CSS file at path: `.../docs/_static/css/custom.css`.
html_css_files = ['css/custom.css']
html_logo ='images/aiqc_logo_wide_white_docs.png'
html_favicon = 'images/favicon.ico'
html_show_sphinx = False
html_show_copyright = False
html_theme_options = {
	'logo_only': True,
	'display_version': False
}

hight_language = 'python3'

suppress_warnings = [
    'nbsphinx',
]

# For notebook hyperlinks, I seem to have to use a `[](.html)` syntax to get it to work.
# https://nbsphinx.readthedocs.io/en/0.8.1/markdown-cells.html#Links-to-Other-Notebooks

# `make html` is supposed to replicate to `.../docs/_build/html/_static/css/custom.css` 
# but I've been having to manually overwrite the _build css file at that location.

#html_sidebars = { '**': ['globaltoc.html'] }
# ^ whenever I add/ remove a page, I seem to have to run `make html` with this uncommented or commented in order to get the toc to stick.
