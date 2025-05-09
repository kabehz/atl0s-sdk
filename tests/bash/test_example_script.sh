#!/bin/bash
# Test para verificar que el script se ejecuta correctamente
bash src/bash/example_script.sh | grep "Hello, World!" && echo "Test Passed" || echo "Test Failed"