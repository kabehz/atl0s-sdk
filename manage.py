#!/usr/bin/env python3

import os
import sys
import subprocess

def run(cmd, desc=None):
    print(f"\n🚀 {desc or 'Ejecutando'}: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Error ejecutando: {cmd}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Uso: python manage.py [comando]")
        print("Comandos disponibles: test, analyze, docker, serve, deploy, mkvenv, install")
        return

    cmd = sys.argv[1]

    if cmd == "test":
        run("./run_tests_local.sh", "Tests unitarios e integración")
    elif cmd == "analyze":
        run("python validador_service_v4.py ./Anexos_Ejemplo ./Resultados", "Análisis de documentos")
    elif cmd == "docker":
        run("docker build -f Dockerfile.service -t validador-service-v4 .", "Build Docker")
        run("docker run --rm -v $(pwd)/Anexos_Ejemplo:/entrada -v $(pwd)/Resultados:/salida validador-service-v4 /entrada /salida", "Run Docker")
    elif cmd == "serve":
        run("cd mkdocs && mkdocs serve", "MkDocs Local")
    elif cmd == "deploy":
        run("cd mkdocs && mkdocs gh-deploy", "Publicar en GitHub Pages")
    elif cmd == "mkvenv":
        run("python -m venv .venv && source .venv/bin/activate", "Crear entorno virtual")
    elif cmd == "install":
        run("pip install -r requirements.txt", "Instalar dependencias base")
    else:
        print("Comando no reconocido.")

if __name__ == "__main__":
    main()