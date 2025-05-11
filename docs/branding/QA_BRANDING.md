# 🧠 MEGAPROMPT – Validación Local + PR Branding ATLANTYDE

**🎯 Objetivo:**  
Consolidar e integrar todos los recursos gráficos generados para ATLANTYDE en esta sesión, validarlos en local y dejar todo listo para un PR hacia `main`.

---

## 📦 RECURSOS VISUALES A VALIDAR

- `header-main.png`
- `footer-mission.png`
- `nav-bg.svg` (o `.png`)
- `scroll-bg.png`
- `europe-star.png`
- `europe-tagline.png`
- `coming-soon.png` (con y sin opacidad)

---

## 🛠️ PASOS PARA VALIDACIÓN LOCAL

### 1. Clonar la rama de diseño visual
```bash
git checkout -b feature/branding-v1 origin/feature/branding-v1
```

---

### 2. Estructura de archivos esperada
```
docs/
└── assets/
    └── branding/
        ├── header-main.png
        ├── footer-mission.png
        ├── nav-bg.svg
        ├── scroll-bg.png
        ├── europe-star.png
        ├── europe-tagline.png
        └── coming-soon.png
mkdocs.yml
```

---

### 3. Configuración en `mkdocs.yml`
```yaml
extra_css:
  - assets/branding/nav-style.css

extra_javascript:
  - assets/branding/scroll-effect.js

theme:
  logo: assets/branding/header-main.png
  favicon: assets/branding/favicon.ico
```

---

### 4. CSS sugerido (`nav-style.css`)
```css
nav.md-header {
  background-image: url('nav-bg.svg');
  background-size: cover;
  opacity: 0.95;
}

.md-main__inner {
  background-image: url('scroll-bg.png');
  background-attachment: fixed;
  background-size: cover;
}

.coming-soon-banner {
  background-image: url('coming-soon.png');
  opacity: 0.3;
  position: fixed;
  bottom: 0;
  width: 100%;
  z-index: -1;
}
```

---

### 5. Test de contraste y accesibilidad
```bash
npx pa11y http://localhost:8000
```

---

### 6. Validación Responsive

| Dispositivo | Resolución     | Resultado esperado   |
|-------------|----------------|----------------------|
| 📱 Móvil     | 360x640        | Logo y nav ok        |
| 📱 Tablet    | 768x1024       | Imagen hero clara    |
| 🖥️ Desktop   | 1920x1080      | Banner adaptado      |

---

✅ Si todo es correcto, procede al PR:
```bash
git add .
git commit -m "feat: integración visual completa ATLANTYDE v1"
git push origin feature/branding-v1

gh pr create --base main --head feature/branding-v1 --title "Branding ATLANTYDE completo" --body "Integración de todos los activos visuales institucionales generados por IA y validados en local."
```

---

💡 *Este documento forma parte del onboarding técnico de ATLANTYDE y debe mantenerse actualizado para futuros colaboradores.*
