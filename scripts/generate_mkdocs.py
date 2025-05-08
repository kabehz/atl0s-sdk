import os
from pathlib import Path
import yaml

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
MKDOCS_FILE = BASE_DIR / "mkdocs.yml"

def generate_nav():
    nav = []
    for root, _, files in os.walk(DOCS_DIR):
        files = [f for f in files if f.endswith(".md")]
        if not files:
            continue
        section = Path(root).relative_to(DOCS_DIR)
        section_title = section.name if section != Path('.') else None
        entries = []
        for file in sorted(files):
            name = Path(file).stem.replace("_", " ").capitalize()
            rel_path = Path(root, file).relative_to(BASE_DIR)
            entries.append({name: str(rel_path)})
        if section_title:
            nav.append({section_title.capitalize(): entries})
        else:
            nav.extend(entries)
    return nav

def main():
    config = {
        "site_name": "Legal Validator",
        "theme": {"name": "material"},
        "nav": generate_nav()
    }
    with open(MKDOCS_FILE, "w") as f:
        yaml.dump(config, f, sort_keys=False, allow_unicode=True)

if __name__ == "__main__":
    main()