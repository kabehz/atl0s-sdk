// Verifica acceso a lógica privada en Legal Validator

async function verificarAcceso(usuario) {
  const input = {
    user: usuario,
    action: "invoke_private_logic"
  };

  const response = await fetch("http://localhost:8181/v1/data/legal_validator/authz/allow", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ input })
  });

  const data = await response.json();
  return data.result === true;
}

// Ejemplo de uso:
verificarAcceso({ role: "maintainer", clearance: "granted" })
  .then(access => {
    if (access) {
      console.log("✅ Acceso permitido a la lógica privada");
    } else {
      console.warn("⛔ Acceso denegado");
    }
  });