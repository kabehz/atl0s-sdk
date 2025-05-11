import os, yaml
root_dir = 'docs'
nav = []
for root, _, files in os.walk(root_dir):
    for f in sorted(files):
        if f.endswith('.md'):
            path = os.path.join(root, f)
            nav.append({f.replace('.md','').capitalize(): path.replace('\\', '/')})
with open('mkdocs.yml', 'r') as f:
    config = yaml.safe_load(f)
config['nav'] = nav
with open('mkdocs.yml', 'w') as f:
    yaml.dump(config, f)
print("✅ mkdocs.yml actualizado con navegación estructurada.")