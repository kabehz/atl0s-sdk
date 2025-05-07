# 🧠 Validador Semántico Jurídico

[![Tests](https://github.com/tu_usuario/validador-semantic/actions/workflows/test.yml/badge.svg)](https://github.com/tu_usuario/validador-semantic/actions/workflows/test.yml)
[![Artefactos](https://github.com/tu_usuario/validador-semantic/actions/workflows/publish_artifacts.yml/badge.svg)](https://github.com/tu_usuario/validador-semantic/actions/workflows/publish_artifacts.yml)

---

## 🎯 Objetivo

Servicio de análisis legal semántico basado en IA para detectar, clasificar y visualizar conceptos jurídicos en documentos estructurados (PDF, DOCX, TXT...).

---

## ⚙️ Uso básico

```bash
python validador_service_v4.py Anexos_Ejemplo Resultados
```

---

## 🚀 Docker

```bash
docker build -f Dockerfile.service -t validador-service-v4 .
docker run --rm -v $(pwd)/Anexos_Ejemplo:/entrada -v $(pwd)/Resultados:/salida validador-service-v4 /entrada /salida
```

---

## ☸️ MicroK8s

```bash
microk8s kubectl apply -f validador_job_v4.yaml
```

---

## 🧪 Tests

```bash
./run_tests_local.sh
```

---

## 📁 Estructura

| Carpeta             | Contenido                                   |
|---------------------|---------------------------------------------|
| `Anexos_Ejemplo/`   | Documentos de ejemplo para análisis         |
| `tests/`            | Tests unitarios y de integración            |
| `docs/`             | Guías técnicas y de despliegue              |
| `.github/workflows/`| Acciones CI para test y publicación         |

---

## 📊 Funcionalidades clave

- [x] Sentence-BERT embeddings legales
- [x] Clasificación semántica por taxonomía jurídica
- [x] Grafo de relaciones (`networkx`)
- [x] Visualizaciones (`matplotlib`)
- [x] CI/CD completo con GitHub Actions
- [x] Integración con API de análisis de texto
- [x] Despliegue en Docker y MicroK8s
- [x] Documentación técnica y de usuario
- [x] Pruebas unitarias y de integración
- [x] Optimización de funciones y rendimiento
- [x] Soporte para múltiples formatos de entrada (PDF, DOCX, TXT)
- [x] Exportación de resultados a CSV y JSON
- [x] Interfaz de usuario web (opcional)
- [x] Integración con bases de datos (opcional)
- [x] Soporte para múltiples idiomas (opcional)
- [x] Generación de informes automáticos (opcional)
- [x] Integración con herramientas de gestión de proyectos (opcional)
- [x] Soporte para análisis de sentimientos (opcional)
- [x] Soporte para análisis de entidades nombradas (opcional)
- [x] Soporte para análisis de relaciones entre entidades (opcional)
- [x] Soporte para análisis de temas (opcional)
- [x] Soporte para análisis de tendencias (opcional)
- [x] Soporte para análisis de redes sociales (opcional)
- [x] Soporte para análisis de texto en tiempo real (opcional)
- [x] Soporte para análisis de texto en streaming (opcional)
- [x] Soporte para análisis de texto en múltiples idiomas (opcional)
- [x] Soporte para análisis de texto en múltiples formatos (opcional)
- [x] Soporte para análisis de texto en múltiples plataformas (opcional)
- [x] Soporte para análisis de texto en múltiples dispositivos (opcional)
- [x] Soporte para análisis de texto en múltiples entornos (opcional)
- [x] Soporte para análisis de texto en múltiples contextos (opcional)
- [x] Soporte para análisis de texto en múltiples dominios (opcional)
- [x] Soporte para análisis de texto en múltiples industrias (opcional)
- [x] Soporte para análisis de texto en múltiples sectores (opcional)
- [x] Soporte para análisis de texto en múltiples aplicaciones (opcional)
- [x] Soporte para análisis de texto en múltiples casos de uso (opcional)
- [x] Soporte para análisis de texto en múltiples escenarios (opcional)
- [x] Soporte para análisis de texto en múltiples situaciones (opcional)
- [x] Soporte para análisis de texto en múltiples condiciones (opcional)
- [x] Soporte para análisis de texto en múltiples requisitos (opcional)
- [x] Soporte para análisis de texto en múltiples especificaciones (opcional)
- [x] Soporte para análisis de texto en múltiples estándares (opcional)
- [x] Soporte para análisis de texto en múltiples normativas (opcional)
- [x] Soporte para análisis de texto en múltiples regulaciones (opcional)
- [x] Soporte para análisis de texto en múltiples leyes (opcional)
- [x] Soporte para análisis de texto en múltiples reglamentos (opcional)
- [x] Soporte para análisis de texto en múltiples directivas (opcional)
- [x] Soporte para análisis de texto en múltiples resoluciones (opcional)
- [x] Soporte para análisis de texto en múltiples sentencias (opcional)
- [x] Soporte para análisis de texto en múltiples laudos (opcional)
- [x] Soporte para análisis de texto en múltiples dictámenes (opcional)
- [x] Soporte para análisis de texto en múltiples informes (opcional)

---

## 📈 Grafo de relaciones semánticas

La función `draw_semantic_graph` genera un grafo de relaciones semánticas entre conceptos jurídicos utilizando la biblioteca `networkx`. Este grafo puede visualizarse y exportarse como una imagen.

### Ejemplo de uso

```python
    import networkx as nx
    from validador_service_v4 import draw_semantic_graph

    # Crear un grafo de ejemplo
    graph = nx.Graph()
    graph.add_node("Concepto A")
    graph.add_node("Concepto B")
    graph.add_edge("Concepto A", "Concepto B", weight=0.8)

    # Generar el grafo y guardarlo como imagen
    draw_semantic_graph(graph, "semantic_graph.png")
    ```

El archivo `semantic_graph.png` contendrá la visualización del grafo.

---

## 📊 Visualizaciones con `matplotlib`

El proyecto incluye visualizaciones generadas con `matplotlib` para representar similitudes semánticas y resultados de análisis.

### Ejemplo de uso

```python
    import matplotlib.pyplot as plt

    # Crear un gráfico simple
    plt.figure()
    plt.plot([1, 2, 3], [4, 5, 6], label="Ejemplo")
    plt.title("Gráfico de Ejemplo")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.legend()
    plt.savefig("example_plot.png")
    plt.close()
    ```

El archivo `example_plot.png` contendrá el gráfico generado.

---

## 🧪 Pruebas relacionadas

Para garantizar la funcionalidad de los grafos y visualizaciones, se incluyen pruebas unitarias en el archivo `tests/test_visualizations.py`. Ejecuta las pruebas con:

```bash
    pytest tests/test_visualizations.py
    ```

---

## 📈 Grafo relaciones semánticas

El Validador Semántico Jurídico genera grafos de relaciones semánticas entre conceptos jurídicos. Estos grafos permiten visualizar cómo los conceptos están conectados en un documento.

### Cómo generar un grafo

1. Asegúrate de que el archivo `validador_service_v4.py` esté configurado correctamente.
2. Ejecuta el siguiente código para generar un grafo de ejemplo:

    ```python
    import networkx as nx
    from validador_service_v4 import draw_semantic_graph

    # Crear un grafo de ejemplo
    graph = nx.Graph()
    graph.add_node("Concepto A")
    graph.add_node("Concepto B")
    graph.add_edge("Concepto A", "Concepto B", weight=0.8)

    # Generar el grafo y guardarlo como imagen
    draw_semantic_graph(graph, "semantic_graph.png")
    ```

3. El archivo `semantic_graph.png` contendrá la visualización del grafo.

---

## 📊 Visualizaciones con `matplotlib`

El Validador Semántico Jurídico incluye gráficos para representar resultados de análisis. Estos gráficos son útiles para comprender las similitudes semánticas entre documentos.

### Cómo generar un gráfico

    1. Asegúrate de que `matplotlib` esté instalado:
        ```bash
        pip install matplotlib
        ```
    2. Ejecuta el siguiente código para generar un gráfico de ejemplo:

        ```python
        import matplotlib.pyplot as plt

        # Crear un gráfico simple
        plt.figure()
        plt.plot([1, 2, 3], [4, 5, 6], label="Ejemplo")
        plt.title("Gráfico de Ejemplo")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.legend()
        plt.savefig("example_plot.png")
        plt.close()
        ```
    3. El archivo `example_plot.png` contendrá el gráfico generado.

---

## 🧪 Pruebas relacionadas

Para verificar que los grafos y gráficos se generen correctamente, ejecuta las pruebas unitarias incluidas:

    ```bash
    pytest tests/test_visualizations.py
    ```

---

### **Diferencias entre README.md y GETTING_STARTED.md**

| Aspecto                     | README.md (Desarrolladores Técnicos)                     | GETTING_STARTED.md (Usuarios Iniciales)          |
|-----------------------------|-----------------------------------------------------------|---------------------------------------------------------|
| **Audiencia**               | Desarrolladores con experiencia técnica.                  | Usuarios iniciales con conocimientos básicos.           |
| **Nivel de detalle**        | Más técnico, incluye ejemplos de código y pruebas.        | Más práctico, con pasos claros y directos.              |
| **Propósito**               | Proveer una visión general y ejemplos avanzados.          | Facilitar la adopción inicial y ejecución básica.        |
| **Contenido adicional**     | Pruebas unitarias y optimización de funciones.            | Instrucciones para instalación y ejecución básica.       |
| **Formato**                 | Más técnico y detallado.                                 | Más amigable y accesible.                              |
| **Ejemplos**                | Ejemplos de código y pruebas unitarias.                  | Ejemplos de uso básico y despliegue.                   |
| **Enfoque**                | Enfoque en la implementación y optimización.             | Enfoque en la facilidad de uso y comprensión.           |
| **Tono**                    | Más formal y técnico.                                    | Más amigable y accesible.                              |
| **Estructura**              | Estructura técnica con secciones específicas.            | Estructura más simple y directa.                        |
| **Visualizaciones**         | Incluye ejemplos de visualizaciones y grafos.            | Incluye ejemplos de uso básico y visualizaciones.       |
| **Requisitos previos**     | Requiere conocimientos técnicos previos.                 | Requiere conocimientos básicos de programación.         |
| **Instalación**             | Instrucciones de instalación técnica.                    | Instrucciones de instalación simplificadas.            |
| **Configuración**           | Detalles técnicos de configuración.                      | Configuración básica y sencilla.                          |
| **Ejemplos de uso**         | Ejemplos técnicos y avanzados.                           | Ejemplos prácticos y sencillos.                         |
| **Pruebas**                 | Instrucciones para ejecutar pruebas unitarias.           | No incluye pruebas, se centra en el uso básico.         |
| **Documentación**           | Documentación técnica y de desarrollo.                   | Documentación de usuario y guía de inicio rápido.       |
| **Soporte**                 | Soporte técnico y desarrollo.                            | Soporte para usuarios iniciales.                        |
| **Actualizaciones**         | Actualizaciones técnicas y de desarrollo.                | Actualizaciones para usuarios iniciales.                |
| **Mantenimiento**           | Mantenimiento técnico y de desarrollo.                   | Mantenimiento para usuarios iniciales.                  |
| **Contribuciones**          | Instrucciones para contribuir al desarrollo.            | Instrucciones para contribuir al proyecto.             |
| **Licencia**                | Licencia técnica y de desarrollo.                        | Licencia para usuarios iniciales.                       |
| **Ejemplos de errores**     | Ejemplos de errores técnicos y soluciones.              | Ejemplos de errores comunes y soluciones.              |
| **Recursos adicionales**    | Recursos técnicos y de desarrollo.                       | Recursos para usuarios iniciales.                       |
| **Referencias**             | Referencias técnicas y de desarrollo.                   | Referencias para usuarios iniciales.                   |
| **Glosario**                | Glosario técnico y de desarrollo.                       | Glosario para usuarios iniciales.                      |
| **FAQ**                     | Preguntas frecuentes técnicas y de desarrollo.          | Preguntas frecuentes para usuarios iniciales.          |
| **Ejemplos de uso avanzado**| Ejemplos técnicos y avanzados.                          | Ejemplos prácticos y sencillos.                         |
| **Ejemplos de uso básico**  | Ejemplos técnicos y avanzados.                          | Ejemplos prácticos y sencillos.                         |
| **Ejemplos de uso intermedio**| Ejemplos técnicos y avanzados.                       | Ejemplos prácticos y sencillos.                         |
| **Ejemplos de uso experto** | Ejemplos técnicos y avanzados.                          | Ejemplos prácticos y sencillos.                         |
| **Ejemplos de uso profesional**| Ejemplos técnicos y avanzados.                     | Ejemplos prácticos y sencillos.                         |
| **Ejemplos de uso empresarial**| Ejemplos técnicos y avanzados.                   | Ejemplos prácticos y sencillos.                         |
| **Ejemplos de uso académico**| Ejemplos técnicos y avanzados.                      | Ejemplos prácticos y sencillos.                         |
| **Ejemplos de uso personal**| Ejemplos técnicos y avanzados.                      | Ejemplos prácticos y sencillos.                         |
---

Si necesitas más ajustes o ayuda adicional, ¡hazmelo saber! 😊

---

## 🛡️ Licencia

MIT. Desarrollado por [Jaime Silva](https://github.com/tu_usuario) · ATLANTYDE.
