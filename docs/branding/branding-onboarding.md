# 🧠 Onboarding Visual – ATLANTYDE Branding

Este documento guía a nuevos colaboradores como Loky a validar y subir correctamente todos los recursos visuales del branding institucional.

---

## 🚀 Pasos a seguir

### 1. Clona la rama visual
```bash
git checkout -b feature/branding-v1 origin/feature/branding-v1
```

### 2. Ejecuta el validador automático
```bash
chmod +x scripts/branding-validate.sh
./scripts/branding-validate.sh
```

### 3. Verifica estructura esperada
```
docs/assets/branding/
├── header-main.png
├── footer-mission.png
├── nav-bg.svg
├── scroll-bg.png
├── europe-star.png
├── europe-tagline.png
└── coming-soon.png
```

### 4. Si todo es correcto, realiza tu PR
```bash
git add .
git commit -m "feat: integración visual completa ATLANTYDE v1"
git push origin feature/branding-v1

gh pr create --base main --head feature/branding-v1 --title "Branding ATLANTYDE completo" --body "Integración de activos visuales validados"
```

---

## 🛡️ Validaciones incluidas en el script

- Existencia de archivos clave
- Configuración de `mkdocs.yml`
- Accesibilidad (Pa11y)
- Responsive manual

---

💡 *"Si falla algo, no es un error: es aprendizaje para el siguiente commit. Dale Loky, ya estás dentro del sistema."*
