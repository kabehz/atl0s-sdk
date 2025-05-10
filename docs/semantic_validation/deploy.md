# 🚀 Despliegue del Sistema de Validación Semántica

Este documento describe cómo desplegar y operar el subsistema de validación semántica legal del proyecto ATLANTYDE en entornos de desarrollo, staging y producción.

---

## 📦 Empaquetado del Servicio

### Docker

```bash
docker build -t validator-semantic .
docker run -p 8000:8000 validator-semantic
```

### Dockerfile (extracto)

```dockerfile
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "src/validator_service_v4.py"]
```

---

## ⚙️ Despliegue en MicroK8s

```bash
microk8s enable dns ingress storage
microk8s kubectl apply -f k8s/semantic-validator-deployment.yaml
microk8s kubectl apply -f k8s/semantic-validator-service.yaml
```

### Reglas OPA en K8s

```bash
kubectl apply -f opa/rego-policies-configmap.yaml
```

---

## 🛠️ Variables de Entorno

* `TAXON_PATH=/app/data/legal_semantic_taxon.json`
* `OPA_POLICY_PATH=/app/policies/`

Se pueden definir en `.env` o `configmap.yaml`.

---

## 📡 API Gateway Opcional

### Ejemplo con Traefik

```yaml
http:
  routers:
    validator:
      rule: "Host(`validador.atlantyde.local`)"
      service: validator-svc
```

---

## ✅ Check de despliegue

```bash
curl -X POST http://localhost:8000/eval -d @tests/input_example.json -H "Content-Type: application/json"
```

Si responde con `{ "result": "allow" }` → OK

---

## 🔁 Despliegue CI/CD GitHub Actions

* `publish_artifacts.yml`: construye imagen y la publica en GitHub Container Registry
* `deploy_microk8s.yml`: aplica manifests si hay cambios en `k8s/`

---

## 📍 Observabilidad

* Logs: `docker logs` o `kubectl logs`
* Prometheus compatible con endpoints de métricas
* Alertas configurables con Falco, Loki, ELK

🧠 *El despliegue seguro y semántico asegura trazabilidad legal desde el código hasta la infraestructura.*
