#!/bin/bash

if [ -z "$1" ]; then
  echo "❌ Error: Debes proporcionar la subcarpeta como argumento (por ejemplo, src/legal-validator/)."
  exit 1
fi

SUBCARPETA=src/pip/$1

echo "🔍 Ejecutando pruebas para la subcarpeta: $SUBCARPETA"

if [ ! -d ".venv" ]; then
  echo "🔍 Creando entorno virtual"
  python3 -m venv .venv
fi

echo "🔍 Activando entorno virtual"
source .venv/bin/activate || { echo "⚠️ No se pudo activar el entorno virtual"; exit 1; }

echo "🔍 Instalando dependencias"
pip install -r requirements.txt

export PYTHONPATH=$(pwd)/src

echo "🔍 Ejecutando pruebas"
pytest $SUBCARPETA/tests/ --tb=short -q --disable-warnings --maxfail=5

echo "✅ Pruebas completadas"

deactivate
rm -rf .venv
echo "🗑️ Entorno limpio"