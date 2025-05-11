import json
changes = ['Component X: updated', 'Policy Y: refined']
with open('RELEASE_NOTES.md', 'w') as f:
    f.write('# Notas de Lanzamiento\n\n')
    f.writelines([f'- {line}\n' for line in changes])
print("✅ RELEASE_NOTES.md generado.")