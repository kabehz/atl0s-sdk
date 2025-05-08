#!/bin/bash

# Colores y efectos
BLUE="\033[1;34m"
GREEN="\033[1;32m"
NC="\033[0m"

echo -e "${BLUE}📘 Legal Validator Docs Launcher${NC}"

function usage() {
  echo "Usage:"
  echo "  ./doc.sh serve     # Servir documentación localmente"
  echo "  ./doc.sh deploy    # Publicar en GitHub Pages"
  echo "  ./doc.sh build     # Compilar documentación sin servir"
}

case "$1" in
  serve)
    echo -e "${GREEN}🚀 Sirviendo documentación en http://localhost:8000...${NC}"
    mkdocs serve
    ;;
  deploy)
    echo -e "${GREEN}🚀 Desplegando documentación a GitHub Pages...${NC}"
    mkdocs gh-deploy --force
    ;;
  build)
    echo -e "${GREEN}🏗️ Compilando documentación...${NC}"
    mkdocs build
    ;;
  *)
    usage
    ;;
esac