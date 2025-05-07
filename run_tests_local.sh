#!/bin/bash

echo "🔍 Ejecutando pruebas unitarias y de integración en local"
source .venv/bin/activate 2>/dev/null || echo "⚠️ VENV no activado"

python -m unittest discover -s tests -v