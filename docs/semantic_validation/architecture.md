# 📐 Arquitectura: Validación Semántica Legal

Este documento forma parte del sistema cognitivo del proyecto **Legal Validator**, específicamente centrado en describir la arquitectura lógica y técnica del subsistema de validación semántica.

---

## 🔍 Objetivo de la Validación Semántica

Validar que las entidades, acciones y relaciones codificadas en un sistema reflejan intenciones legales y restricciones normativas.

* Garantiza coherencia legal semántica.
* Apoya decisiones automatizadas auditables.
* Permite trazabilidad entre código ↔ ley ↔ contexto humano.

---

## 🧠 Componentes Principales

### 1. `src/validator_service_v4.py`

* Analiza entradas legales en JSON.
* Aplica reglas de decisión y etiquetas cognitivas desde `legal_semantic_taxon.json`.

### 2. `src/policies/opa/`

* Reglas escritas en Rego.
* Evalúan acceso, cumplimiento o excepciones según el rol, contexto o entidad.

### 3. `tests/python/semantic_validation/`

* Pruebas unitarias y de integración para validar los flujos semánticos.
* Cobertura con Pytest + OPA policies.

---

## 🧩 Flujo de Validación Semántica

```mermaid
flowchart TD
  A[Input JSON legal] --> B[Parser Python (validator_service)]
  B --> C[Enriquecimiento semántico por taxonomía]
  C --> D[Evaluación Rego / OPA]
  D --> E[Resultado: Permitido, Denegado, Observado]
```

---

## 🧬 Casos de Uso

* Validación de permisos contractuales entre actores.
* Determinación de conformidad con GDPR, CRA o políticas internas.
* Detección de incoherencias semánticas en plantillas legales.

---

## 📈 Métricas Clave

* % de cobertura semántica sobre casos legales
* Tiempo medio de inferencia por input
* Ratio de falsos positivos/negativos
* Reglas de Rego más invocadas

---

## 🗃️ Repositorios de Conocimiento

* `docs/legal/` → definiciones legales base
* `docs/taxonomy/` → estructura semántica cognitiva
* `src/policies/opa/` → políticas vivas en Rego
* `tests/compliance/` → validadores de cumplimiento europeo

---

## 🧭 Proyección

* Integración con NLP para etiquetado automático desde contratos en lenguaje natural.
* Soporte multilingüe para validación multijurisdiccional.
* Entrenamiento de LLMs sobre contextos validados como corpus legal estructurado.

🧠 *El derecho computable no es una utopía. Es una arquitectura semántica en construcción.*
