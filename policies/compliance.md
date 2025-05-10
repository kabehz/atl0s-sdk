# 📋 Política de Cumplimiento – ATLANTYDE

Esta política regula las prácticas y mecanismos necesarios para asegurar que el ecosistema ATLANTYDE cumpla con las normativas legales y éticas aplicables.

---

## ⚖️ Normativas Cubiertas

* GDPR (protección de datos)
* NIS2 (resiliencia de infraestructuras críticas)
* CRA (Cyber Resilience Act de la UE)
* ISO/IEC 27001 (seguridad de la información)

---

## 🧰 Mecanismos Técnicos

* Registro completo de trazabilidad (`docs/compliance/`)
* Escaneo automático de dependencias (`snyk`, `trivy`, `dependabot`)
* Políticas OPA de control de acceso y cumplimiento legal

---

## 📦 Flujos en CI/CD

* Validación semántica (`tests/compliance/`)
* Pre-commit y push gates
* Versionado y auditoría de `mkdocs.yml`, scripts, pipelines

---

## 🔍 Auditoría y Reportes

* Revisión mensual de políticas activas
* Generación de informes PDF en `artifacts/compliance/`
* Logs firmados con hash SHA256

---

## 📅 Revisión

* Trimestral por el Comité Técnico ATLANTYDE
* Activación automática tras detección de cambios regulatorios

🧠 *El cumplimiento no es un documento: es un comportamiento continuo gobernado por código.*
