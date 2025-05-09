import os
import json
from pathlib import Path
import subprocess

# def get_changed_files():
#     """Obtiene la lista de archivos modificados en el último commit."""
#     try:
#         # Intenta obtener los cambios entre HEAD y HEAD~1
#         result = subprocess.run(
#             ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#             text=True,
#             check=True,
#         )
#         return result.stdout.splitlines()
#     except subprocess.CalledProcessError as e:
#         # Si falla, intenta obtener los cambios desde el inicio del repositorio
#         print(f"Advertencia: {e.stderr}. Usando HEAD en su lugar.")
#         result = subprocess.run(
#             ["git", "diff", "--name-only", "HEAD"],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#             text=True,
#             check=True,
#         )
#         return result.stdout.splitlines()

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
        print(f"Archivos modificados detectados: {result.stdout}")
        return result.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Advertencia: {e.stderr}. Usando HEAD en su lugar.")
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        print(f"Archivos modificados detectados: {result.stdout}")
        return result.stdout.splitlines()

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

    # Validar el formato del JSON antes de exportarlo
    changes_str = json.dumps(changes)
    print(f"Exportando cambios detectados: {changes_str}")
    