package legal_validator.authz
default allow = false
allow { input.user.role == "architect"; input.action == "invoke_private_logic" }
allow { input.user.role == "maintainer"; input.action == "invoke_private_logic"; input.user.clearance == "granted" }

default allow = false

# Política de ejemplo: solo usuarios con rol 'architect' pueden usar lógica privada
allow {
    input.user.role == "architect"
    input.action == "invoke_private_logic"
}

# Extensión: permitir colaboración avanzada
allow {
    input.user.role == "maintainer"
    input.action == "invoke_private_logic"
    input.user.clearance == "granted"
}