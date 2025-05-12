# 🧠 Validador Semántico Jurídico

[![Tests](https://github.com/tu_usuario/validador-semantic/actions/workflows/test.yml/badge.svg)](https://github.com/tu_usuario/validador-semantic/actions/workflows/test.yml)
[![Artefactos](https://github.com/tu_usuario/validador-semantic/actions/workflows/publish_artifacts.yml/badge.svg)](https://github.com/tu_usuario/validador-semantic/actions/workflows/publish_artifacts.yml)

---

## 🎯 Objetivo

El **Validador Semántico Jurídico** es un servicio basado en inteligencia artificial diseñado para analizar, clasificar y visualizar conceptos jurídicos en documentos estructurados (PDF, DOCX, TXT, etc.). Este proyecto combina técnicas avanzadas de procesamiento de lenguaje natural (NLP) y aprendizaje automático para ofrecer análisis semánticos precisos y visualizaciones intuitivas.

---

## 🚀 Funcionalidades clave

### Funcionalidades actuales

- [x] **Embeddings legales**: Basados en Sentence-BERT.
- [x] **Clasificación semántica**: Por taxonomía jurídica.
- [x] **Grafo de relaciones**: Generado con `networkx`.
- [x] **Visualizaciones**: Gráficos y dashboards con `matplotlib`.
- [x] **CI/CD**: Integración completa con GitHub Actions.
- [x] **Soporte para múltiples formatos**: PDF, DOCX, TXT.
- [x] **Exportación de resultados**: A CSV y JSON.
- [x] **Despliegue**: Compatible con Docker y MicroK8s.

### Funcionalidades futuras/opcionales

- [ ] Interfaz de usuario web.
- [ ] Integración con bases de datos.
- [ ] Soporte para múltiples idiomas.
- [ ] Generación de informes automáticos.
- [ ] Mejora de la precisión de los embeddings.
- [ ] Integración con APIs externas.
- [ ] Análisis de sentimientos en textos jurídicos.
- [ ] Mejora de la visualización de grafos.
- [ ] Implementación de un sistema de recomendaciones.
- [ ] Soporte para análisis en tiempo real.
- [ ] Integración con herramientas de gestión de proyectos.
- [ ] Mejora de la documentación y ejemplos de uso.
- [ ] Implementación de un sistema de alertas y notificaciones.
- [ ] Mejora de la eficiencia del procesamiento de documentos.
- [ ] Implementación de un sistema de control de versiones para los documentos analizados.
- [ ] Mejora de la usabilidad y experiencia del usuario.
- [ ] Implementación de un sistema de autenticación y autorización.
- [ ] Mejora de la seguridad y protección de datos.
- [ ] Implementación de un sistema de backup y recuperación de datos.
- [ ] Mejora de la escalabilidad y rendimiento del sistema.
- [ ] Implementación de un sistema de monitoreo y análisis de rendimiento.
- [ ] Mejora de la integración con otras herramientas y sistemas.
- [ ] Implementación de un sistema de gestión de usuarios y roles.
- [ ] Mejora de la integración con herramientas de análisis de datos.
- [ ] Implementación de un sistema de gestión de tareas y proyectos.
- [ ] Mejora de la integración con herramientas de colaboración y comunicación.
- [ ] Implementación de un sistema de gestión de documentos y archivos.
- [ ] Mejora de la integración con herramientas de gestión de contenido.
- [ ] Implementación de un sistema de gestión de conocimiento y aprendizaje.
- [ ] Mejora de la integración con herramientas de gestión de relaciones con clientes (CRM).
- [ ] Implementación de un sistema de gestión de relaciones con proveedores (SRM).
- [ ] Mejora de la integración con herramientas de gestión de recursos humanos (HRM).
- [ ] Implementación de un sistema de gestión de relaciones con socios (PRM).
- [ ] Mejora de la integración con herramientas de gestión de proyectos ágiles.
- [ ] Implementación de un sistema de gestión de relaciones con inversores (IRM).
- [ ] Mejora de la integración con herramientas de gestión de relaciones con empleados (ERM).
- [ ] Implementación de un sistema de gestión de relaciones con comunidades (CRM).
- [ ] Implementación de un sistema de gestión de relaciones con medios de comunicación (PRM).

---

## ⚙️ Uso básico

### Procesar un archivo

```bash
python validador_service_v4.py Anexos_Ejemplo Resultados
```

### Procesar diferentes formatos

```bash
# Procesar un archivo PDF
python validador_service_v4.py Anexos_Ejemplo/documento.pdf Resultados

# Procesar un archivo DOCX
python validador_service_v4.py Anexos_Ejemplo/documento.docx Resultados

# Procesar un archivo TXT
python validador_service_v4.py Anexos_Ejemplo/documento.txt Resultados
```

### Manejo de errores

Si ocurre un error, revisa los logs generados en la carpeta `Resultados/logs/`.

---

## 📦 Docker

### Construir la imagen

```bash
docker build -f Dockerfile.service -t validador-service-v4 .
```

### Ejecutar el contenedor

```bash
docker run --rm \
  -v $(pwd)/Anexos_Ejemplo:/entrada \
  -v $(pwd)/Resultados:/salida \
  validador-service-v4 /entrada /salida
```

### Configurar variables de entorno

```bash
docker run --rm \
  -e LOG_LEVEL=DEBUG \
  -v $(pwd)/Anexos_Ejemplo:/entrada \
  -v $(pwd)/Resultados:/salida \
  validador-service-v4 /entrada /salida
```

---

## ☸️ MicroK8s

### Aplicar el job

```bash
microk8s kubectl apply -f validador_job_v4.yaml
```

### Verificar el estado del job

```bash
microk8s kubectl get jobs
```

### Acceder a los logs del pod

```bash
microk8s kubectl logs -l job-name=validador-job-v4
```

---

## 📝 Función `extract_text`

La función `extract_text` permite extraer texto de archivos en diferentes formatos (PDF, DOCX, imágenes, etc.).

### Ejemplo de uso

```python
from validador_service_v4 import extract_text
from pathlib import Path

file_path = Path("Anexos_Ejemplo/documento.pdf")
text = extract_text(file_path)
print(text)

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

### Ejemplo uso

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

## 🧪 Pruebas

### Ejecutar todas las pruebas

```bash
pytest tests/
```

### Ejecutar pruebas específicas

```bash
pytest tests/test_visualizations.py
```

---

## 📁 Estructura del proyecto

| Carpeta             | Contenido                                   |
|---------------------|---------------------------------------------|
| `Anexos_Ejemplo/`   | Documentos de ejemplo para análisis         |
| `tests/`            | Tests unitarios y de integración            |
| `docs/`             | Guías técnicas y de despliegue              |
| `.github/workflows/`| Acciones CI para test y publicación         |

---

## 🛠️ Contribuir

¡Gracias por tu interés en contribuir! Sigue estos pasos para colaborar:

1. Haz un fork del repositorio.
2. Crea una rama para tus cambios:

   ```bash
   git checkout -b mi-nueva-funcionalidad
   ```

3. Realiza tus cambios y asegúrate de que las pruebas pasen:

   ```bash
   pytest tests/
   ```

4. Haz un commit y sube tus cambios:

   ```bash
   git commit -m "Añadida nueva funcionalidad X"
   git push origin mi-nueva-funcionalidad
   ```

5. Abre un pull request en GitHub.

---

## 🛡️ Licencia

Este proyecto está bajo la Licencia **EUPL** (European Union Public License). Puedes consultar los términos completos en el archivo `LICENSE`.
Desarrollado por [Jaime Silva](https://github.com/kabehz) · ATLANTYDE.

---

### **Mejoras Implementadas**

1. **Documentación**: Se mejoró la claridad y la estructura de la documentación.
2. **Estructura clara**: Se reorganizó el contenido para facilitar la navegación.
3. **Ejemplos prácticos**: Se añadieron ejemplos detallados para diferentes formatos y configuraciones.
4. **Visuales**: Se incluyeron ejemplos de uso para grafos y visualizaciones.
5. **Contribución**: Se añadió una sección clara para guiar a nuevos colaboradores.
6. **Neuromarketing**: Uso de emojis y secciones bien delimitadas para mejorar la experiencia del usuario.
7. **Optimización de comandos**: Se simplificaron los comandos de uso y despliegue.
8. **Errores comunes**: Se incluyó una sección para manejar errores y revisar logs.
9. **Docker y MicroK8s**: Se mejoraron las instrucciones para el uso de Docker y MicroK8s.
10. **Pruebas**: Se incluyó una sección clara para ejecutar pruebas y verificar el funcionamiento del proyecto.
11. **Artefactos**: Se añadió un badge para la publicación de artefactos en GitHub Actions.
12. **CI/CD**: Se mejoró la integración continua y el despliegue continuo con GitHub Actions.
13. **Optimización de código**: Se realizaron mejoras en el código para aumentar la eficiencia y legibilidad.
14. **Manejo de errores**: Se mejoró el manejo de errores y la generación de logs.

---

## 🚪 ¿Y ahora qué?

¡Enhorabuena por firmar tu compromiso ético!

Tu siguiente paso es **crear tu perfil digital oficial como miembro de la ATLANTYDE Community**.

➡️ Ve al siguiente Lab: [`LAB-M00 – Perfil Digital`](../LAB-M00-PerfilDigital/README.md)

Este paso es obligatorio para formar parte activa de nuestra comunidad y aparecer en los tableros de progreso, reconocimientos e historia viva del proyecto.