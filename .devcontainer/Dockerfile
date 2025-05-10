FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

# Instalar herramientas adicionales
RUN apt-get update && apt-get install -y \
    terraform \
    shellcheck \
    curl \
    unzip \
    nodejs npm \
    git \
    rustc cargo \
    && apt-get clean

# Instalar OPA
RUN curl -L -o opa https://openpolicyagent.org/downloads/latest/opa_linux_amd64_static \
    && chmod +x opa && mv opa /usr/local/bin/

# Instalar prettier global para lint y docs
RUN npm install -g prettier

# Crear usuario vscode si no existe
ARG USERNAME=vscode
RUN useradd -m $USERNAME || true


# Instalar GitHub CLI
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | gpg --dearmor -o /usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && apt-get update \
    && apt-get install -y gh