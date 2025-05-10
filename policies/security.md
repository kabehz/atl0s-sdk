# 🔐 Política de Seguridad – ATLANTYDE

Esta política define los principios, controles y procedimientos operativos que rigen la seguridad de sistemas, datos y operaciones en el proyecto ATLANTYDE.

---

## 🎯 Objetivos

* Prevenir accesos no autorizados.
* Proteger datos personales y sensibles.
* Garantizar disponibilidad y resiliencia de los servicios.

---

## 🧩 Ámbitos de Aplicación

* Código fuente (`src/`, `.vscode/`, `.github/`)
* Documentación (`docs/`)
* Infraestructura (`iac/`, `k8s/`, `scripts/`)
* Pipelines (`.github/workflows/`, `pre-commit`)

---

## 🔒 Controles Técnicos

* Autenticación multifactor (MFA) en GitHub.
* Secretos en `.env`, no versionados.
* `Bandit`, `gitleaks`, `trivy`, `OPA` como herramientas preventivas.
* Encriptación en tránsito (HTTPS) y en reposo.

---

## 🔄 Procedimientos

* Auditorías de seguridad trimestrales.
* Escaneo automático de dependencias en CI.
* Validación de firmas digitales en imágenes Docker.

---

## ⚖️ Cumplimiento Normativo

* Alineado con: GDPR, NIS2, CRA.
* Soporte de auditoría trazable en `docs/compliance/`.

🧠 *La seguridad no es una opción. Es un prerrequisito legal y operativo.*
