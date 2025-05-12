# 🎮 Desafío Narrativo ATLANTYDE – `nuestra-historia`

> *"Quien controla la narrativa, guía el futuro."* – Sabiduría Atlante 🧭

## 🎯 Misión
Construye, junto a la comunidad, la **historia viva** de ATLANTYDE.  
Tu reto: **añadir un nuevo hito al relato colectivo**, dejar huella en el tiempo.

---

## 🧩 ¿Cómo participar?

### 1. Clona el repositorio y navega al módulo
```bash
git clone https://github.com/atlantyde/portal
cd portal/
```

### 2. Abre el archivo de historia colaborativa:
```bash
nano data/historia-events.csv
```

### 3. Añade tu evento 🗓️  
En la última línea, sigue este formato:
```csv
fecha,autor,tipo,hito,impacto,enlace,media_type
2025-05-12,TuNombre,colaborativo,Contribuí al manifiesto ético,Alta,https://youtu.be/mi-video,video
```

Tipos permitidos: `fundacional`, `tecnológico`, `comunitario`, `colaborativo`  
Impacto: `Bajo`, `Medio`, `Alto`  
Media: `video`, `call`, `text`, `doc`, etc.

---

## 🛠️ Genera la historia
```bash
bash scripts/storyline-generator.sh
```

✅ Esto generará o actualizará el archivo:
```
docs/nuestra-historia.md
```

---

## 🧠 Nivel desbloqueado
Al contribuir, aparecerás en la narrativa oficial del proyecto.  
Tu historia será leída por nuevos Atlantes que buscan referentes.

---

## 🛡️ Reglas del juego

- ✔️ Respeta formato CSV (usa comas, sin tildes locas)
- 🌐 Enlaces públicos solo si son relevantes
- 🧬 Sé creativo, pero veraz

---

### 🫂 ¿Y ahora qué?

Abre tu PR con título:

```bash
feat(historia): añado hito personal o comunitario
```

¡Y listo! 🎉  
Serás parte de la leyenda viva de ATLANTYDE 🌊

