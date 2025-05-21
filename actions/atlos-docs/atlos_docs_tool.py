
#!/usr/bin/env python3
import argparse, os, yaml
from pymdownx.emoji import twemoji, to_svg

def insert_badges(readme='README.md', badges_file='README_badges_mkdocs.md'):
    print("📥 Insertando badges...")
    if not os.path.exists(readme) or not os.path.exists(badges_file):
        print("❌ Archivos necesarios no encontrados.")
        return
    with open(readme, "r+", encoding="utf-8") as f:
        content = f.read()
        if "## 🧠 Badges de Progreso en Documentación" in content:
            print("🟡 Badges ya presentes.")
        else:
            f.write("\n")
            with open(badges_file, "r", encoding="utf-8") as b:
                f.write(b.read())
            print("✅ Badges insertados.")

def generate_structured_nav(base_dir="docs"):
    print("📁 Generando navegación estructurada...")
    nav = []
    for root, _, files in os.walk(base_dir):
        for f in sorted(files):
            if f.endswith(".md"):
                path = os.path.join(root, f).replace("\\", "/")
                nav.append({f.replace(".md", "").capitalize(): path})
    return nav

def generate_semantic_nav(base_dir="docs"):
    print("📁 Generando navegación semántica...")
    nav = []
    for root, _, files in os.walk(base_dir):
        section = os.path.relpath(root, base_dir)
        section_title = section.replace("_", " ").title()
        children = []
        for file in sorted(files):
            if file.lower().endswith((".md", ".markdown")):
                full_path = os.path.join(root, file)
                if not os.path.exists(full_path):
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
    parser = argparse.ArgumentParser(description="ATL0S Docs Tool")
    parser.add_argument('--mode', choices=['append-badges', 'structured', 'semantic'], required=True)
    parser.add_argument('--base-dir', type=str, default='docs')
    parser.add_argument('--output', type=str, default='mkdocs.yml')
    args = parser.parse_args()

    if args.mode == 'append-badges':
        insert_badges()
    else:
        nav = generate_structured_nav(args.base_dir) if args.mode == 'structured' else generate_semantic_nav(args.base_dir)
        config = {"nav": nav}
        if args.mode == 'semantic':
            config.update({
                "site_name": "ATLANTYDE ACADEMY Foundation",
                "site_url": "https://kabehz.github.io/atl0s/",
                "site_description": "Infraestructura legal semántica para soberanía europea (NLP + DevSecOps).",
                "site_author": "Kabehz",
                "theme": {
                    "name": "material",
                    "logo": "assets/branding/header-main.png",
                    "favicon": "assets/branding/favicon.ico",
                    "palette": {"scheme": "default", "primary": "blue", "accent": "pink"},
                    "features": ["navigation.tabs", "navigation.expand", "navigation.top", "toc.integrate", "search.highlight", "search.suggest"],
                    "font": {"text": "Roboto", "code": "Roboto Mono"},
                    "language": "es"
                },
                "extra_css": ["assets/css/markdown.css", "assets/css/mermaid.css"],
                "extra_javascript": ["https://cdnjs.cloudflare.com/ajax/libs/intro.js/7.0.1/intro.min.js"],
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
                "plugins": ["search", {"minify": {"minify_html": True}}, "mermaid2"]
            })
        with open(args.output, "w", encoding="utf-8") as f:
            yaml.dump(config, f, sort_keys=False, allow_unicode=True)
        print(f"✅ Archivo '{args.output}' generado en modo {args.mode}.")

if __name__ == "__main__":
    main()
