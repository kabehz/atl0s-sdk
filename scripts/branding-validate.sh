#!/bin/bash

# ┌─────────────────────────────────────────────┐
# │ ATLANTYDE :: Script Branding Visual Checker │
# └─────────────────────────────────────────────┘

echo "🔍 Iniciando validación visual ATLANTYDE..."

# 1. Verificar estructura de archivos
echo "📁 Verificando estructura de assets..."

REQUIRED_FILES=(
  "docs/assets/branding/header-main.png"
  "docs/assets/branding/footer-mission.png"
  "docs/assets/branding/nav-bg.svg"
  "docs/assets/branding/scroll-bg.png"
  "docs/assets/branding/europe-star.png"
  "docs/assets/branding/europe-tagline.png"
  "docs/assets/branding/coming-soon.png"
)

missing=false

for file in "${REQUIRED_FILES[@]}"; do
  if [ ! -f "$file" ]; then
    echo "❌ Faltante: $file"
    missing=true
  else
    echo "✅ Encontrado: $file"
  fi
done

if [ "$missing" = true ]; then
  echo "⚠️ Archivos faltantes. Por favor, verifica antes de continuar."
  exit 1
fi

# 2. Validar configuración en mkdocs.yml
echo "📄 Verificando configuración en mkdocs.yml..."

REQUIRED_LINES=(
  "extra_css:"
  "  - assets/branding/css/nav-style.css"
  "extra_javascript:"
  "  - assets/branding/js/scroll-effect.js"
  "logo: assets/branding/header-main.png"
  "favicon: assets/branding/favicon.ico"
)

for line in "${REQUIRED_LINES[@]}"; do
  grep -q "$line" mkdocs.yml || echo "⚠️ Revisa mkdocs.yml: falta línea -> $line"
done

# 3. Lighthouse o Pa11y (requiere Node.js instalado)
echo "🧪 Ejecutando test de accesibilidad con Pa11y..."
if command -v pa11y &> /dev/null; then
  npx pa11y http://localhost:8000 --reporter html > branding-accessibility-report.html
  echo "📄 Reporte generado: branding-accessibility-report.html"
else
  echo "⚠️ Pa11y no instalado. Ejecuta: npm install -g pa11y"
fi

# 4. Validación responsive: mensaje orientativo
echo "🧪 Validación responsive (manual)"
echo "👉 Abrir el site en local y verificar en:"
echo "   - Mobile (360x640)"
echo "   - Tablet (768x1024)"
echo "   - Desktop (1920x1080)"

echo "✅ Validación finalizada. ¡Listo para preparar el PR!"
