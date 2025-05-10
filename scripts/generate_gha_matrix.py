### **1. Contexto del Repositorio**
#La estructura del repositorio sigue un patrón consistente:
#- Código fuente: `src/<tecnologia>/<script|component|app|library>/code`
#- Tests: `tests/<tecnologia>/<script|component|app|library>/code-test`

#Este patrón permite identificar automáticamente las tecnologías y componentes disponibles, lo que facilita la generación de matrices dinámicas para los workflows.
#- Sin embargo, actualmente los workflows de GitHub Actions están configurados de manera estática, lo que limita la escalabilidad y la automatización del proceso de CI/CD.
#- Cada vez que se añade una nueva tecnología o componente, es necesario actualizar manualmente los workflows, lo que puede llevar a errores y desincronización.
#- Además, la falta de validación de la correspondencia entre los componentes y sus pruebas puede resultar en una cobertura de pruebas incompleta.
#- Esto se traduce en un proceso de integración continua menos eficiente y más propenso a errores.
#- La solución propuesta es implementar un script que genere dinámicamente la matriz de tecnologías y componentes, asegurando que cada componente tenga su correspondiente directorio de pruebas.
#- Esto no solo mejorará la eficiencia del pipeline, sino que también garantizará una mayor cobertura de pruebas y una mejor alineación con las prácticas de GitOps.
#- La implementación de esta mejora permitirá al equipo de desarrollo centrarse en la creación de nuevas funcionalidades y mejoras, en lugar de perder tiempo en la gestión manual de los workflows.
#- Además, al automatizar la generación de la matriz, se reducirá el riesgo de errores humanos y se mejorará la consistencia en la ejecución de las pruebas.
#- En resumen, la mejora propuesta no solo optimiza el proceso de CI/CD, sino que también alinea el repositorio con las mejores prácticas de desarrollo ágil y DevOps.

### **2. Estrategia de Mejora**
#### **a. Generación Dinámica de Matrices**
#- Utilizar un script en Bash o Python para recorrer las carpetas `src/<tecnologia>` y generar dinámicamente una lista de tecnologías y componentes.
#- Pasar esta lista como una matriz a los workflows de GitHub Actions.

#### **b. Validación de Correspondencia**
#- Asegurarse de que cada componente en `src/<tecnologia>` tenga un directorio correspondiente en `tests/<tecnologia>`.
#- Si no existe un directorio de pruebas, generar un error o advertencia en el workflow.

#### **c. Escalabilidad**
#- La matriz debe ser capaz de manejar nuevas tecnologías y componentes sin necesidad de modificar manualmente los workflows.
#- Esto asegura que el pipeline sea **GitOps-friendly**, ya que cualquier cambio en la estructura del repositorio se reflejará automáticamente en los workflows.

### **3. Implementación de la Mejora**

#### **a. Script para Generar la Matriz**
# Un script en Python puede recorrer las carpetas y generar la matriz:
# Con esta mejora, el repositorio está preparado para escalar de manera eficiente, soportando múltiples tecnologías y componentes con un pipeline completamente automatizado y dinámico. 😊
import os
import json
from pathlib import Path

def generate_matrix():
    base_src = Path("src")
    base_tests = Path("tests")
    matrix = []

    for technology in base_src.iterdir():
        if technology.is_dir():
            for component in technology.iterdir():
                if component.is_dir():
                    # Verificar si existe el directorio de pruebas correspondiente
                    test_path = base_tests / technology.name / component.name
                    if test_path.exists():
                        matrix.append({
                            "technology": technology.name,
                            "component": component.name
                        })
                    else:
                        print(f"⚠️ Advertencia: No se encontraron pruebas para {technology.name}/{component.name}")

    return {"include": matrix}

if __name__ == "__main__":
    matrix = generate_matrix()
    with open("gha_matrix.json", "w") as f:
        json.dump(matrix, f, indent=4)
    print("✅ Matriz generada en 'gha_matrix.json'")

# - Este script recorre las carpetas `src` y `tests`, generando una matriz que se puede utilizar en los workflows de GitHub Actions.
# - La matriz generada se puede utilizar en los workflows de GitHub Actions para ejecutar pruebas automáticamente para cada componente y tecnología.
# - Este script genera una matriz en formato JSON que puede ser utilizada directamente en los workflows de GitHub Actions.
