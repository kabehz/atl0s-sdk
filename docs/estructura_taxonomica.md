# 🧭 Taxonomía de Carpetas – Legal Validator v0.2.0

Esta guía describe **el propósito, retos y visión** de cada carpeta del proyecto. Pensado como mapa cognitivo y motivador para atraer a desarrolladores LATAM con desafíos concretos.

---

## `.github/workflows/` – CI/CD Multitecnología

📌 Contiene todos los flujos de automatización:
- `ci-multitecnologia.yml`: Pruebas en Python, Bash, Terraform, Ansible
- `update_mkdocs.yml`: Autoindexación semántica de documentación
- `release-template.yml`: Publicación automatizada de versiones

🎯 *Reto*: Crea nuevos workflows para validación semántica con LLMs o reglas OPA.

---

## `docs/` – Documentación VIVA

📚 Aquí vive el conocimiento del proyecto, versionado y desplegado con MkDocs.
- `index.md`: Navegación por perfil técnico
- `ci_cd_architecture.md`: Diagrama mermaid CI/CD
- `deploy_doc_guide.md`: Guía de despliegue en GitHub Pages

🎯 *Reto*: Añadir guías temáticas por tipo de taxonomía legal o técnica.

---

## `src/` – Núcleo de Inteligencia

💻 Contiene código fuente distribuido por tecnología:
- `pip/legal-validator/`: Analítica semántica legal
- `bash/scripts/`: Automatización CLI
- `iac/terraform` & `ansible/`: Infraestructura reproducible

🎯 *Reto*: Implementar despliegue semántico autoescalable con GitOps.

---

## `tests/` – Evidencia y Confianza

🧪 Validación modular, cobertura de funciones:
- `python/`: Unit e integración
- `bash/`: Validación CLI
- `iac/`: Terraform y Ansible lint/test

🎯 *Reto*: Crear pruebas semánticas fuzzing y validadores de contratos.

---

## `scripts/` – Automatización Extensible

⚙️ Scripts que facilitan construcción, testeo y despliegue.
- `generate_mkdocs.py`: Generación dinámica de índice

🎯 *Reto*: Incluir transformaciones NLP y extracción de metadatos legales.

---

> 🌱 Este repositorio es un entorno vivo de aprendizaje, colaboración y trazabilidad. Cada carpeta es una **misión abierta** para innovar.

🧠 **Participa creando, versionando y documentando como un verdadero arquitecto de conocimiento.**