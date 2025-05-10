# 🧰 Herramientas para Validación Semántica Legal

Este documento describe las principales herramientas utilizadas en el ecosistema ATLANTYDE para habilitar, automatizar y mantener procesos de validación semántica en entornos legales, contractuales o normativos.

---

## 🧠 Motor de Validación Semántica

### 🔹 `validator_service_v4.py`

* Orquestador semántico en Python.
* Recibe input estructurado (`json` o `dict`).
* Dispara reglas desde taxonomías y delega evaluación a OPA.

### 🔹 `legal_semantic_taxon.json`

* Ontología de etiquetas y relaciones legales.
* Aplicado para enriquecer los contextos antes de evaluación.

---

## 🛡️ Evaluación Rego (OPA)

### 🔹 Open Policy Agent (OPA)

* Evaluador de políticas semánticas expresadas en Rego.
* Integrado vía subprocess desde Python.

### 🔹 Scripts auxiliares

* `opa_eval.sh`: ejecutar pruebas o inputs desde CLI.
* `opa-lint`: pre-commit hook para validar sintaxis Rego.

---

## 🔍 Testing y Validación

### 🔹 `pytest + coverage`

* Ejecuta pruebas unitarias y de integración sobre el servicio.

### 🔹 `test_semantic_policy.py`

* Simula escenarios de acceso, contrato o cumplimiento usando OPA.

---

## 🧪 Lint y Formato

* `black`, `flake8`, `isort`: código Python legible y seguro.
* `opa fmt`: normalización de archivos `.rego`
* `markdownlint`, `yamllint`: documentación y config estandarizadas.

---

## 🧭 Integración con CI/CD

* `ci_pytest_opa.yml`: job GitHub Actions para lint, test y validación Rego.
* `pre-commit-config.yaml`: previene errores antes de commit.
* `mkdocs.yml`: mantiene documentación sincronizada y autoindexada.

---

## 🔬 Futuro

* Incorporación de ReasonML o Z3 para validaciones algebraicas.
* Auto-generación de reglas desde corpus legal en lenguaje natural.
* Conexión con herramientas de visualización (Graphviz, Cytoscape).

🧠 *Validar semánticamente es conectar el derecho con su ejecución computable.*
