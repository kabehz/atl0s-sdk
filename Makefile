# Makefile - ATLANTYDE DevOps Local

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

.DEFAULT_GOAL := help

help:
	@echo "🧠 Comandos disponibles:"
	@echo "  make install   → Instala entorno y dependencias"
	@echo "  make serve     → Lanza documentación local"
	@echo "  make test      → Ejecuta tests"
	@echo "  make build     → Compila documentación"
	@echo "  make nav       → Autogenera navegación semántica"
	@echo "  make all       → nav + build + test"

install:
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-dev.txt

nav:
	$(PYTHON) scripts/generate_mkdocs_semantic.py

serve: nav
	$(VENV)/bin/mkdocs serve

build: nav
	$(VENV)/bin/mkdocs build --strict

test:
	$(VENV)/bin/pytest

all: nav build test