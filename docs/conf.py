# -- Project information -----------------------------------------------------
project = "Public Sector Security"
copyright = "Turtini"
author = "Turtini"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"

# (Optional) Match the left-nav behavior you’re used to
html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "includehidden": True,
}

# (Optional) If you have a logo like your main docs
# html_logo = "_static/turtini-logo.svg"
# html_favicon = "_static/favicon.ico"

html_static_path = ["_static"]
