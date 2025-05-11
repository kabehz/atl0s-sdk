import json

with open("changes_detected.json") as f:
    changes = json.load(f)

lines = ["# 💚 Contribución Social de Componentes ATLANTYDE", "", 
         "Este documento se genera automáticamente en cada release para informar del impacto positivo de los módulos actualizados para la sociedad digital.", ""]

for section, items in changes.items():
    if items:
        lines.append(f"## 📦 {section.capitalize()}")
        for item in items:
            lines.append(f"- `{item}` → Mejora trazabilidad, automatización o acceso libre al conocimiento.")
        lines.append("")

lines.append("---")
lines.append("🧠 *Cada línea de código libre aquí es una acción en defensa de una inteligencia colectiva.*")

with open("docs/components/impacto_social.md", "w") as f:
    f.write("\n".join(lines))