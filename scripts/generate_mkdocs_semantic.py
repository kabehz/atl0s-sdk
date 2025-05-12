import os, yaml

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
    "site_name": "ATLANTYDE Docs",
    "theme": {
        "name": "material",
        "logo": "assets/branding/header-main.png",
        "favicon": "assets/branding/favicon.ico"
    },
    "extra_css": [
        "assets/css/animations.css",
        "assets/branding/nav-style.css"
    ],
    "extra_javascript": [
        "assets/js/intersection-observer.js",
        "assets/branding/scroll-effect.js"
    ],
    "markdown_extensions": [
        "toc",
        "tables",
        "attr_list",
        "admonition",
        {
            "pymdownx.emoji": {
                "emoji_index": "!!python/name:material.extensions.emoji.twemoji",
                "emoji_generator": "!!python/name:material.extensions.emoji.to_svg"
            }
        }
    ],
    "plugins": [
        "search",
        "minify",
        {
            "git-revision-date-localized": {
                "fallback_to_build_date": False
            }
        },
        "material/get-deps"
    ],
    "nav": build_nav()
}

with open("mkdocs.yml", "w") as f:
    yaml.dump(config, f, sort_keys=False)

print("✅ mkdocs.yml generado dinámicamente por semántica de directorios.")