#!/bin/bash
echo '🧠 Generando narrativa desde historia-events.csv...'
echo '---' > docs/storyline.md
echo '# Narrativa generada automáticamente' >> docs/storyline.md
cat data/historia-events.csv | awk -F',' '{print "- " $1 " → " $2}' >> docs/storyline.md