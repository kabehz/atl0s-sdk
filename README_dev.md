# 👨‍💻 Developer Guide – Legal Validator

Bienvenido/a a la guía técnica para desarrolladores del proyecto **Legal Validator**, una plataforma modular diseñada para escalar tecnologías legales con NLP, automatización, y contratos inteligentes.

---

## 🧠 Arquitectura Modular

```
src/
├── python/        -> Código de análisis semántico legal (NLP)
├── bash/          -> Scripts de automatización (deploy, linting, test)
├── iac/           -> Infraestructura como código (Terraform, Ansible)

tests/
├── python/        -> Unit/integration tests usando pytest
├── bash/          -> Validación de scripts y pipelines
├── iac/           -> Validación sintáctica de Terraform y Ansible

docs/
├── smart_contracts/ -> Contratos inteligentes en formato Markdown
```

---

## ⚙️ Entorno de Desarrollo

### Requisitos Previos

- Python 3.10+
- `pip`, `virtualenv`
- Docker (para pruebas de despliegue)
- Terraform y Ansible (para módulos IaC)
- MkDocs (para documentar)

### Instalación Rápida

```bash
# Clona el proyecto
git clone https://github.com/<tu_usuario>/legal-validator.git
cd legal-validator

# Entorno virtual
python -m venv .venv
source .venv/bin/activate

# Instalar el módulo legal-validator
pip install -e src/pip/legal-validator
pip install -r src/pip/legal-validator/requirements.txt
```

---

## 🧪 Ejecutar Pruebas

```bash
# Pruebas Python
pytest tests/python/

# Pruebas Bash
bash tests/bash/test_scripts.sh

# Pruebas IaC
cd src/iac/terraform && terraform validate
ansible-playbook --syntax-check src/iac/ansible/playbook.yml
```

---

## 🧠 Tips para Contribuir

- Estructura tu módulo dentro de la carpeta correspondiente
- Usa `pytest` o `shellcheck`/`terratest` para pruebas automatizadas
- Documenta funciones clave en `docs/` y usa `mkdocs serve` para previsualizar
- Usa GitHub Actions como laboratorio de validación

---

## 🔁 Flujo de CI/CD

1. Cada push ejecuta validaciones para cada tecnología.
2. Todos los resultados se muestran en GitHub Actions.
3. Los PRs deben pasar tests antes de mergear.

---

## 🧠 Aceleradores de Productividad

| Comando            | Descripción                        |
|--------------------|------------------------------------|
| `make test`        | Ejecuta pruebas completas          |
| `make format`      | Autoformatea código (si configurado)|
| `make docs-serve`  | Lanza documentación localmente     |

---

## 🧩 Roadmap Tecnológico

- [ ] Validación semántica con transformers
- [ ] Integración Open Contracting (OCDS)
- [ ] Firma digital de contratos
- [ ] UI visual para navegación legal

---

Con esta guía, puedes integrarte rápidamente y aportar de forma significativa al ecosistema Legal Validator.

Nos vemos en tu primer PR 🚀