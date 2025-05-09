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
        print("Usage: python manage.py [command]")
        print("Available commands: test, analyze, docker, serve, deploy, mkvenv, install")
        return

    cmd = sys.argv[1]

    if cmd == "local_test":
        run("./run_tests_local.sh", "Unit and Integration Tests")
    elif cmd == "test":
        run("pytest tests/", "Unit and Integration Tests")
    elif cmd == "analyze":
        run("python validador_service_v4.py ./Anexos_Ejemplo ./Resultados", "Document Analysis")
    elif cmd == "docker":
        run("docker build -f Dockerfile.service -t validador-service-v4 .", "Build Docker")
        run("docker run --rm -v $(pwd)/Anexos_Ejemplo:/entrada -v $(pwd)/Resultados:/salida validador-service-v4 /entrada /salida", "Run Docker")
    elif cmd == "serve":
        run("cd mkdocs && mkdocs serve", "Serve MkDocs Locally")
    elif cmd == "deploy":
        run("cd mkdocs && mkdocs gh-deploy", "Deploy Documentation")
    elif cmd == "mkvenv":
        run("python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt", "Create Virtual Environment")
    elif cmd == "install":
        run("pip install -r requirements.txt", "Install Dependencies")
    else:
        print(f"❌ Unsupported command: {cmd}")
        print("Available commands: test, analyze, docker, serve, deploy, mkvenv, install")

if __name__ == "__main__":
    main()