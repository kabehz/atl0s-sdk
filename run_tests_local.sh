#!/bin/bash

echo "🔍 Ejecutando pruebas unitarias y de integración en local"
echo "🔍 Creando entorno virtual"
python3 -m venv .venv

echo "🔍 Activando entorno virtual, Verificando si el entorno virtual ya existe"
source .venv/bin/activate 2>/dev/null || echo "⚠️ VENV no activado"

echo "🔍 Instalando dependencias"
pip install -r requirements.txt
# pip install -r requirements-dev.txt
# pip install -r requirements-test.txt
# pip install -r requirements-lint.txt
# pip install -r requirements-docs.txt
# pip install -r requirements-ml.txt
# pip install -r requirements-ml-dev.txt
# pip install -r requirements-ml-test.txt
# pip install -r requirements-ml-lint.txt
# pip install -r requirements-ml-prod.txt


echo "🔍 Ejecutando pruebas unitarias y de integración"
python3 -m unittest discover -s tests -v
# pytest --tb=short -q --disable-warnings --maxfail=1
# pytest --tb=short -q --disable-warnings --maxfail=1 --cov=legal-advisor-validator
# pytest --tb=short -q --disable-warnings --maxfail=1 --cov-report=html:coverage_html_report
# pytest --tb=short -q --disable-warnings --maxfail=1 --cov-report=xml:coverage.xml
# pytest --tb=short -q --disable-warnings --maxfail=1 --cov-report=term-missing --cov-fail-under=80 --cov-config=.coveragerc
echo "✅ Pruebas completadas"


# echo "🔍 Ejecutando pruebas de linting"
# pylint --rcfile=.pylintrc legal-advisor-validator


echo "🧹 Limpiando el entorno"
deactivate
rm -rf .venv
echo "🗑️ Entorno limpio"
echo "🚀 Listo para el siguiente paso"
echo "🔍 Ejecutando pruebas de linting"
pylint --rcfile=.pylintrc legal-advisor-validator





