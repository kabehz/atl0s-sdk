#!/bin/bash

README="README.md"

echo "🔍 Buscando archivos README adicionales..."
for file in README_*.md; do
  [[ "$file" == "README.md" ]] && continue
  if ! grep -q "$(head -n 1 "$file")" "$README"; then
    echo -e "\n" >> "$README"
    cat "$file" >> "$README"
    echo "✅ Insertado contenido de $file en $README"
  else
    echo "🟡 Ya está presente $file en $README"
  fi
done
