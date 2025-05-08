# 🧾 Changelog – Legal Validator v0.2.0

## 🚀 Versión: 0.2.0
📅 Fecha de publicación: 2025-05-08  
🔖 Estado: Release candidate

---

## 🧱 Estructura y Modularización

- 🔀 Reorganización total del proyecto en `src/`, `tests/`, `docs/`, `assets/`, `scripts/`
- 📂 Soporte para múltiples tecnologías: Python, Bash, Terraform, Ansible
- 📜 Inclusión de contratos inteligentes en `docs/smart_contracts/`

---

## ⚙️ Integración CI/CD Multitecnología

- ✅ Workflows GitHub Actions para:
  - Testing Python con `pytest`
  - Validación de scripts `bash`
  - Validación IaC (`terraform validate`, `ansible-playbook`)
  - Auto-despliegue MkDocs con `gh-pages`
  - Autoindexación `mkdocs.yml` desde contribuciones `.md`

---

## 🧠 UX y Documentación

- 🎨 Tema `mkdocs-material` personalizado con branding ATLANTYDE
- 🌗 Soporte para modo claro/oscuro, navegación por pestañas y búsqueda integrada
- 📘 Guía de despliegue y onboarding neurodidáctico (`README_dev.md`, `CONTRIBUTING.md`)
- 🔄 Navegación temática por perfil técnico (DevOps, Backend, Web3, Legal, Docs)

---

## 🧪 Testeo y Validación

- ✔️ Consolidación de tests funcionales:
  - `extract_text`, `semantic_analysis`, `hash_file`
- 🔍 Limpieza de rutas duplicadas, `PYTHONPATH`, cobertura semántica básica

---

## 📦 Instalación sugerida

```bash
git clone https://github.com/kabehz/legal-validator.git
cd legal-validator
python -m venv .venv && source .venv/bin/activate
pip install -e src/pip/legal-validator
make test
```

---

## 🧬 Próximos pasos (v0.3.0 roadmap)

- 🤖 Integración de LLMs para análisis semántico contextual
- 🧾 Generación automática de contratos en PDF firmables
- 🔐 Reglas OPA para verificación legal basada en políticas
- 🌍 Multilenguaje y compatibilidad con LLM europeos

---

Gracias por contribuir al ecosistema Legal Validator 🌐