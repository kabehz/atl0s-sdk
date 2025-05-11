#!/bin/bash

INPUT="data/historia-events.csv"
TEMPLATE="templates/historia-template.md"
OUTPUT="docs/nuestra-historia.md"

[ ! -f "$INPUT" ] && echo "❌ Faltante: $INPUT" && exit 1
[ ! -f "$TEMPLATE" ] && echo "❌ Faltante: $TEMPLATE" && exit 1

EVENTOS=$(awk -F',' 'NR>1 {
  enlace = ($6 != "" && $7 != "") ? sprintf("\n🎬 [%s](%s)", toupper(substr($7, 1, 1)) substr($7, 2), $6) : ""
  printf "### %s – %s (%s)\n\n%s.%s\n\n", $1, $2, $3, $4, enlace
}' "$INPUT")

sed "s/{{EVENTOS}}/$EVENTOS/" "$TEMPLATE" > "$OUTPUT"
echo "✅ Generado: $OUTPUT"
