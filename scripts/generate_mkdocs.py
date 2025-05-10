import os
from pathlib import Path
import yaml

def generate_mkdocs():
    docs_path = Path("docs")
    mkdocs_path = Path("mkdocs.yml")

    # Leer el archivo mkdocs.yml existente
    with open(mkdocs_path, "r") as f:
        mkdocs_config = yaml.safe_load(f)

    # Generar navegación dinámica
    nav = []
    for root, dirs, files in os.walk(docs_path):
        for file in files:
            if file.endswith(".md"):
                relative_path = Path(root).relative_to(docs_path) / file
                section = relative_path.parts[0]
                entry = {section: str(relative_path)}
                if entry not in nav:
                    nav.append(entry)

    # Actualizar la configuración de navegación
    mkdocs_config["nav"] = nav

    # Guardar el archivo actualizado
    with open(mkdocs_path, "w") as f:
        yaml.dump(mkdocs_config, f, default_flow_style=False, sort_keys=False)
    print("✅ Archivo 'mkdocs.yml' actualizado dinámicamente")

if __name__ == "__main__":
    generate_mkdocs()