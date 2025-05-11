#!/bin/bash

README="README.md"
BADGES_FILE="README_badges_mkdocs.md"

if grep -q "## 🧠 Badges de Progreso en Documentación" "$README"; then
    echo "🟡 Badges ya presentes en README.md"
else
    echo -e "\n" >> "$README"
    cat "$BADGES_FILE" >> "$README"
    echo "✅ Badges insertados en README.md"
fi
