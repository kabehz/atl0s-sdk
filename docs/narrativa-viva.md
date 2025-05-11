# 🧠 Narrativa Viva – Módulo Estratégico de Historia ATLANTYDE

Este documento describe el sistema automatizado y colaborativo para construir la narrativa institucional de ATLANTYDE desde su comunidad.

---

## 🎯 Objetivo

Transformar hitos técnicos, sociales y humanos en una historia viva documentada colectivamente, validada por revisión humana y celebrada como parte del legado del proyecto.

---

## 🧩 Estructura del módulo

```
historia-module/
├── data/
│   └── historia-events.csv
├── docs/
│   └── nuestra-historia.md  ← generado automáticamente
├── scripts/
│   └── storyline-generator.sh
├── templates/
│   └── historia-template.md
├── .github/workflows/
│   └── autonarrativa.yml
└── README.md (gamificado)
```

---

## ⚙️ Funcionamiento

1. Se editan nuevos eventos en `data/historia-events.csv`.
2. El script `storyline-generator.sh` genera `nuestra-historia.md` desde plantilla.
3. Cada lunes, `autonarrativa.yml` ejecuta esta lógica vía GitHub Actions.
4. Se crea un PR automático solo si hubo cambios, para revisión humana.

---

## 🧠 Formato de eventos

```csv
fecha,autor,tipo,hito,impacto,enlace,media_type
2025-05-12,TuNombre,colaborativo,Contribuí al manifiesto ético,Alta,https://youtu.be/mi-video,video
```

- `tipo`: fundacional, tecnológico, comunitario, colaborativo, legal, artístico, etc.
- `media_type`: video, call, doc, imagen, text

---

## 🛡️ Validación humana

Aunque el sistema automatiza la narrativa, **la comunidad siempre valida**:

- Se revisan PR creados automáticamente
- Se moderan entradas no verificadas o sin impacto
- Se fomenta la curaduría emocional y estratégica

---

## 🎮 Gamificación

El archivo `README.md` del módulo funciona como desafío narrativo:

> “Tu contribución no termina en un commit... se transforma en leyenda.”

Este enfoque crea sentido de pertenencia y refuerza el branding narrativo personal/colectivo.

---

## 🧲 Uso recomendado en el sitio

- Incluir `nuestra-historia.md` en MKDocs como sección emocional
- Mostrar fragmentos en el footer o sección *Quiénes somos*
- Crear línea del tiempo animada en futuras versiones frontend

---

## 🏁 Conclusión

El sistema `narrativa-viva` convierte la historia organizacional en un activo emocional, técnico y cultural que evoluciona con cada commit y cada persona.

