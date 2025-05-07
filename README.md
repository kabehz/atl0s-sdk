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

---

## 🛡️ Licencia

MIT. Desarrollado por [Jaime Silva](https://github.com/tu_usuario) · ATLANTYDE.