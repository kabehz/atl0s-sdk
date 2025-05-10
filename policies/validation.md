# 🧪 Política de Validación Semántica – ATLANTYDE

Esta política establece cómo deben realizarse las validaciones semánticas de entradas, reglas y resultados en el entorno del proyecto ATLANTYDE.

---

## 📌 Alcance

* Evaluaciones semánticas legales en `src/validator_service.py`
* Reglas Rego en `src/policies/opa/`
* Test semántico automatizado en `tests/`

---

## 📜 Principios

* Toda acción computable debe ser legalmente interpretable.
* Toda validación debe ser auditable.
* Las reglas semánticas deben reflejar derechos y obligaciones reales.

---

## 🧰 Herramientas

* `OPA` + `Rego`
* `legal_semantic_taxon.json`
* `pytest`, `bandit`, `coverage`
* `mkdocs` + `Mermaid`

---

## ✅ Flujo de Validación

1. Enriquecimiento semántico desde taxonomía.
2. Evaluación contra políticas OPA.
3. Comparación esperada contra test automatizado.
4. Registro y reporte.

---

## 🔄 Frecuencia

* En cada PR (`ci-pytest.yml`)
* Semanal vía `cron job`
* Manual tras cambios legales estructurales

🧠 *Validar semánticamente es reflejar la intención humana en acciones técnicas trazables.*
