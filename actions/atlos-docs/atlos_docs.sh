
#!/bin/bash
# Wrapper para ejecutar atlos_docs_tool.py
set -euo pipefail
set -x

MODE=$1
BASE_DIR=${2:-docs}
OUTPUT=${3:-mkdocs.yml}

python3 /app/atlos_docs_tool.py --mode "$MODE" --base-dir "$BASE_DIR" --output "$OUTPUT"
