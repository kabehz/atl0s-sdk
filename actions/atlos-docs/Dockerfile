FROM python:3.10-slim

WORKDIR /app

COPY atlos_docs_tool.py .

RUN pip install pyyaml pymdown-extensions

ENTRYPOINT ["python3", "/app/atlos_docs_tool.py"]

# # Imagen base
# FROM python:3.10-slim

# # Directorio de trabajo
# WORKDIR /app

# # Dependencias
# COPY atlos_docs_tool.py /app/atlos_docs_tool.py
# RUN pip install pyyaml pymdown-extensions

# # Copiar script wrapper
# COPY atlos_docs.sh /usr/local/bin/atlos-docs
# RUN chmod +x /usr/local/bin/atlos-docs

# ENTRYPOINT ["atlos-docs"]