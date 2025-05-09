import os
import json
from pathlib import Path
import subprocess

def get_changed_files():
    """Obtiene la lista de archivos modificados en el último commit."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        return result.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error al obtener archivos modificados: {e.stderr}")
        return []

def detect_changes():
    """Detecta cambios en las carpetas src y tests."""
    changed_files = get_changed_files()
    changes = {"src": [], "tests": []}

    for file in changed_files:
        if file.startswith("src/"):
            changes["src"].append(file)
        elif file.startswith("tests/"):
            changes["tests"].append(file)

    return changes

if __name__ == "__main__":
    changes = detect_changes()
    with open("changes_detected.json", "w") as f:
        json.dump(changes, f, indent=4)
    print("✅ Cambios detectados guardados en 'changes_detected.json'")
