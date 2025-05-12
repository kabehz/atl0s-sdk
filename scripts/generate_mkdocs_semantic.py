import os
import yaml
from pymdownx.emoji import twemoji, to_svg

def build_nav(base_dir="docs"):
    nav = []
    for root, _, files in os.walk(base_dir):
        section = os.path.relpath(root, base_dir)
        section_title = section.replace("_", " ").title()
        children = []
        for file in sorted(files):
            if file.endswith(".md"):
                label = os.path.splitext(file)[0].replace("_", " ").capitalize()
                path = os.path.join(section, file).replace('\\', '/')
                children.append({label: path})
        if section != "." and children:
            nav.append({section_title: children})
        elif children:
            nav.extend(children)
    return nav

config = {
    "site_name": "ATLANTYDE ACADEMY Foundation",
    "site_url": "https://kabehz.github.io/atl0s/",
    "site_description": "Sociedad Cooperativa en Legaltech, EU Digital Compliance,Formación y Transformación Digital sirviendo infraestructura para la validación legal semántica y soberanía normativa europea basada en NLP + DevSecOps.",
    "site_author": "Kabehz",
    "theme": {
        "name": "material",
        "logo": "assets/branding/header-main.png",
        "favicon": "assets/branding/favicon.ico",
        "palette": {
            "scheme": "default",
            "primary": "blue",
            "accent": "pink"
        },
        "features": [
            "navigation.tabs",
            "navigation.expand",
            "navigation.top",
            "navigation.sections",
            "navigation.tracking",
            "navigation.instant",
            "toc.integrate",
            "search.highlight",
            "search.share",
            "search.suggest"
        ],
        "font": {
            "text": "Roboto",
            "code": "Roboto Mono"
        },
        "language": "es",
        "icon": {
            "repo": "fontawesome/brands/github",
            "edit": "fontawesome/solid/edit",
            "collapse": "fontawesome/solid/caret-down",
            "expand": "fontawesome/solid/caret-up",
            "nav": {
                "collapse": "fontawesome/solid/caret-down",
                "expand": "fontawesome/solid/caret-up"
            }
        }
    },
    "extra_css": [
        "assets/css/animations.css",
        "assets/branding/nav-style.css",
        "https://cdnjs.cloudflare.com/ajax/libs/intro.js/7.0.1/introjs.min.css",
        "assets/css/markdown.css",
        "assets/css/mermaid.css"
    ],
    "extra_javascript": [
        "assets/js/intersection-observer.js",
        "assets/branding/scroll-effect.js",
        "https://cdnjs.cloudflare.com/ajax/libs/scrollreveal/4.0.9/scrollreveal.min.js",
        "https://cdnjs.cloudflare.com/ajax/libs/intro.js/7.0.1/intro.min.js"
    ],
    "extra": {
        "social": [
            {
                "icon": "fontawesome/brands/github",
                "link": "https://github.com/kabehz/atlantyde-kit-adoption"
            },
            {
                "icon": "fontawesome/brands/linkedin",
                "link": "https://linkedin.com/in/jaimesilvagonzalez"
            }
        ]
    },
    "markdown_extensions": [
        "toc",
        "tables",
        "attr_list",
        "admonition",
        "codehilite",
        "footnotes",
        "def_list",
        "pymdownx.highlight",
        "pymdownx.superfences",
        "pymdownx.inlinehilite",
        "pymdownx.tabbed",
        "pymdownx.details",
        {
            "pymdownx.emoji": {
                "emoji_index": twemoji,
                "emoji_generator": to_svg
            }
        }
    ],
    "plugins": [
        {
            "search": {
                "index": True
            }
        },
        {
            "minify": {
                "minify_html": True,
                "minify_css": True,
                "minify_js": True
            }
        },
        {
            "mermaid2": {
              "theme": "default",
              "themeVariables": {
                "primaryColor": "#4A90E2",
                "edgeLabelBackground": "#ffffff",
                "tertiaryColor": "#ffffff",
                "noteBkgColor": "#ffffff",
                "noteTextColor": "#000000"
              }
            }
        },
        "material/get-deps"
    ],
    "nav": build_nav()
}

with open("mkdocs.yml", "w") as f:
    yaml.dump(config, f, sort_keys=False)

print("✅ mkdocs.yml regenerado con prácticas óptimas y sociales integradas.")
