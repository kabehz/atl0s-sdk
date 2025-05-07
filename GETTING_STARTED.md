# 🚀 GETTING STARTED – Validador Semántico Jurídico

Bienvenido al repositorio completo del Validador Semántico Jurídico. Este proyecto permite analizar documentos legales con IA semántica, clasificar conceptos jurídicos y visualizar relaciones.

---

## 📦 Requisitos mínimos

- Python 3.8+
- Docker 20.10+ (opcional)
- MicroK8s v1.28+ (opcional)
- RAM: 8 GB | CPU: 4 núcleos

---

## ⚙️ Instalación local (modo desarrollo)

```bash
git clone https://github.com/tu_usuario/validador-semantic.git
cd validador-semantic
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 🧪 Ejecutar análisis local

```bash
python validador_service_v4.py ./Anexos_Ejemplo ./Resultados
```

---

## 🧪 Pruebas unitarias

```bash
./run_tests_local.sh
```

---

## 🐳 Docker (modo contenedor)

```bash
docker build -f Dockerfile.service -t validador-service-v4 .
docker run --rm -v $(pwd)/Anexos_Ejemplo:/entrada -v $(pwd)/Resultados:/salida validador-service-v4 /entrada /salida
```

---

## ☸️ MicroK8s (modo clúster)

```bash
microk8s kubectl apply -f validador_job_v4.yaml
```

---

## 🌐 Publicar documentación técnica

```bash
cd mkdocs
pip install -r requirements.txt
mkdocs serve
# o para GitHub Pages:
mkdocs gh-deploy
```

---

## 📂 Estructura recomendada

| Carpeta             | Descripción                                   |
|---------------------|-----------------------------------------------|
| `Anexos_Ejemplo/`   | Documentos legales para test                  |
| `tests/`            | Tests de unidad e integración                 |
| `docs/`             | Documentación técnica Markdown                |
| `mkdocs/`           | Portal completo con MkDocs Material           |
| `.github/workflows/`| CI/CD para test y artefactos automáticos      |

---

## 📌 Contacto

Creado por Jaime Silva – [https://github.com/tu_usuario](https://github.com/tu_usuario)

MIT License – ATLANTYDE Project