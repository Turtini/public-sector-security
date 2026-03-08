# docs/conf.py

from __future__ import annotations

from datetime import datetime

from turtini_sphinx_theme import get_theme_paths


project = "Public Sector Security"
author = "Turtini LLC"
copyright = f"{datetime.utcnow().year}, Turtini LLC"

extensions = [
    "myst_parser",
]

source_suffix = {".md": "markdown"}
root_doc = "index"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "attrs_inline",
]

_paths = get_theme_paths()

templates_path = [_paths["templates"]]
html_static_path = ["_static", _paths["static"]]

html_logo = "turtini-logo-white.png"
html_favicon = "_static/favicon.ico"

html_css_files = ["turtini.css"]

html_last_updated_fmt = "%B %d, %Y"

html_context = {
    "turtini_year": datetime.utcnow().year,
}

html_baseurl = ""
