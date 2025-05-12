import os
import argparse
import yaml
from pymdownx.emoji import twemoji, to_svg

def build_nav(base_dir="docs"):
    nav = []
    for root, _, files in os.walk(base_dir):
        section = os.path.relpath(root, base_dir)
        section_title = section.replace("_", " ").title()
        children = []
        for file in sorted(files):
            if file.lower().endswith(('.md', '.markdown')):
                full_path = os.path.join(root, file)
                if not os.path.exists(full_path):
                    print(f"⚠️ Archivo no encontrado, generando placeholder: {full_path}")
                    os.makedirs(os.path.dirname(full_path), exist_ok=True)
                    with open(full_path, "w", encoding="utf-8") as f:
                        f.write("# WIP ATLANTYDE COMING SOON!\n")
                label = os.path.splitext(file)[0].replace("_", " ").capitalize()
                path = os.path.join(section, file).replace("\\", "/")
                children.append({label: path})
        if section != "." and children:
            nav.append({section_title: children})
        elif children:
            nav.extend(children)
    return nav

def main():
    parser = argparse.ArgumentParser(description="Generate mkdocs.yml dynamically")
    parser.add_argument('--base-dir', type=str, default='docs', help='Base directory of docs')
    parser.add_argument('--output', type=str, default='mkdocs.yml', help='Output mkdocs.yml file path')
    args = parser.parse_args()

    config = {
        "site_name": "ATLANTYDE ACADEMY Foundation",
        "site_url": "https://kabehz.github.io/atl0s/",
        "site_description": "Infraestructura legal semántica para soberanía europea (NLP + DevSecOps).",
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
                "navigation.tabs", "navigation.expand", "navigation.top",
                "toc.integrate", "search.highlight", "search.suggest"
            ],
            "font": {
                "text": "Roboto",
                "code": "Roboto Mono"
            },
            "language": "es"
        },
        "extra_css": [
            "assets/css/animations.css",
            "assets/branding/nav-style.css",
            "assets/css/markdown.css",
            "assets/css/mermaid.css"
        ],
        "extra_javascript": [
            "assets/js/leaderboard.js",
            "assets/js/nav-iteraction.js",
            "assets/branding/scroll-effect.js",
            "assets/js/intersection-observer.js",
            # "assets/js/scrollspy.js",
            # "assets/js/scrollspy-nav.js",
            # "assets/js/scrollspy-animated.js",
            # "assets/js/scrollspy-animated-nav.js",
            "https://cdnjs.cloudflare.com/ajax/libs/intro.js/7.0.1/intro.min.js"
        ],
        "extra": {
            "social": [
                {"icon": "fontawesome/brands/github", "link": "https://github.com/kabehz/atlantyde-kit-adoption"},
                {"icon": "fontawesome/brands/linkedin", "link": "https://linkedin.com/in/jaimesilvagonzalez"}
            ]
        },
        "markdown_extensions": [
            "toc", "tables", "attr_list", "admonition", "codehilite", "footnotes", "def_list",
            "pymdownx.highlight", "pymdownx.superfences", "pymdownx.inlinehilite",
            "pymdownx.tabbed", "pymdownx.details",
            {"pymdownx.emoji": {"emoji_index": twemoji, "emoji_generator": to_svg}}
        ],
        "plugins": [
            "search",
            {"minify": {"minify_html": True}},
            "mermaid2"
        ],
        "nav": build_nav(args.base_dir)
    }

    with open(args.output, "w", encoding="utf-8") as f:
        yaml.dump(config, f, sort_keys=False, allow_unicode=True)

    print(f"✅ Archivo '{args.output}' generado automáticamente desde '{args.base_dir}'.")

if __name__ == "__main__":
    main()
# This script generates a mkdocs.yml file for the documentation site.
# It scans the specified base directory for markdown files and organizes them into a navigation structure.
# The generated mkdocs.yml file includes configuration for the Material theme, extra CSS and JS files, and various plugins.
# The script uses the PyYAML library to create the YAML file and the argparse library to handle command-line arguments.
# The script also includes a function to build the navigation structure based on the directory and file names.
# The navigation structure is hierarchical, with sections and subsections based on the directory structure.
