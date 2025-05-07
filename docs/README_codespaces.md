# 💻 Desarrollo con GitHub Codespaces

Este repositorio está listo para ser clonado y ejecutado en entornos remotos con GitHub Codespaces o Visual Studio Code con soporte para `.devcontainer`.

---

## 🚀 Abrir en Codespaces

Haz clic en el siguiente botón para abrir este proyecto directamente en Codespaces:

[![Abrir en GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&repo=tu_usuario%2Fvalidador-semantic&ref=main&machine=basicLinux32gb&devcontainer_path=.devcontainer%2Fdevcontainer.json)

---

## 🧰 Requisitos para desarrollo local (opcional)

- VSCode
- Extensión: **Remote - Containers**
- Docker Desktop

---

## 🧪 Tareas útiles

```bash
make test        # Ejecutar tests
make analyze     # Lanzar validador IA
make serve       # Lanzar MkDocs en local
make deploy      # Publicar portal de documentación
```

---

## 🧠 Beneficios de este entorno

- Configuración automática de dependencias
- Contenedor Linux ligero con Python 3.11
- OCR, análisis semántico, MkDocs y CI/CD listos
- Compatible con GitHub Actions y MicroK8s