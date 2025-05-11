#!/bin/bash
echo '🔍 Buscando README_* para incluirlos en mkdocs.yml...'
for file in README_*.md; do
  echo "  - 📘 $(basename $file .md): $file" >> mkdocs.yml
done
echo "✅ mkdocs.yml actualizado con READMEs dinámicos."