from turtini_sphinx_theme import get_theme_paths

# ---- Core Sphinx settings ----
extensions = [
    "myst_parser",
]

# IMPORTANT: make the landing page live at docs/index.md
root_doc = "index"
master_doc = "index"

# Let Sphinx read Markdown
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# ---- Theme wiring (your existing approach) ----
_paths = get_theme_paths()
templates_path = [_paths["templates"]]
html_static_path = [_paths["static"]]
html_css_files = ["turtini.css"]

# Avoid build artifacts
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
