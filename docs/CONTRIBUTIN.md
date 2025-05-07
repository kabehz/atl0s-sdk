# Guía de Contribución – Validador Semántico Jurídico

¡Gracias por tu interés en contribuir al proyecto "Validador Semántico Jurídico"! Esta guía detalla el proceso para colaborar de manera efectiva, asegurando la calidad, trazabilidad y escalabilidad del código.

---

## Índice

1. [Requisitos Previos](#requisitos-previos)
2. [Cómo Contribuir](#cómo-contribuir)
3. [Estilo de Código](#estilo-de-código)
4. [Automatización y Tests](#automatización-y-tests)
5. [Entorno de Desarrollo](#entorno-de-desarrollo)
6. [Revisión de Pull Requests](#revisión-de-pull-requests)
7. [Seguridad y Privacidad](#seguridad-y-privacidad)
8. [Licencia](#licencia)

---

## Requisitos Previos

Antes de comenzar, asegúrate de tener:

- Conocimientos de Python 3.10+
- Familiaridad con Docker y Git
- Leído el archivo `README.md`
- Instalado `pre-commit`, `pytest`, `flake8`, y `bandit`

---

## Cómo Contribuir

1. **Fork** del repositorio y clona tu fork.
2. Crea una rama con nombre descriptivo:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios siguiendo el estilo de código.
4. Asegúrate de que los tests pasen localmente:
   ```bash
   make test
   ```
5. Empuja tu rama:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
6. Abre un Pull Request describiendo claramente:
   - Propósito del cambio
   - Cambios realizados
   - Referencias a issues existentes

---

## Estilo de Código

- Utiliza `black` para formato.
- Usa `flake8` para estilo.
- Incluye anotaciones de tipo (`typing`) en funciones.
- Añade `docstrings` con formato `Google`.

Ejemplo:

```python
def extract_text(path: str) -> str:
    """
    Extrae texto de un archivo.

    Args:
        path (str): Ruta al archivo.

    Returns:
        str: Texto extraído.
    """
```

---

## Automatización y Tests

- Todos los cambios deben incluir pruebas (`tests/`)
- Usa `pytest` y ejecuta:
  ```bash
  pytest tests/
  ```
- Verifica errores con:
  ```bash
  bandit -r .
  flake8 .
  ```

---

## Entorno de Desarrollo

Recomendado usar VSCode con `.devcontainer/`.

Pasos:

1. Abre el proyecto con Dev Containers.
2. Ejecuta `make build` para construir servicios.
3. Usa `make up` para levantar el entorno.

---

## Revisión de Pull Requests

El flujo CI/CD en `.github/workflows/` verifica:

- Tests
- Seguridad (`bandit`)
- Estilo (`flake8`)
- Formato (`black`)
- Generación de documentación (`mkdocs build`)

Todo PR debe pasar estas validaciones para ser aceptado.

---

## Seguridad y Privacidad

- No subas datos sensibles.
- Usa `.env.template` como referencia.
- Escanea dependencias con:
  ```bash
  pip list --outdated
  pipdeptree
  ```

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta `LICENSE` para más detalles.

---

Gracias por contribuir con calidad y propósito. ¡Tu ayuda hace la diferencia! 🙌
