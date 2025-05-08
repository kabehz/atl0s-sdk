FROM openpolicyagent/opa:latest

COPY policies /policies
ENTRYPOINT ["/opa", "run", "--server", "--set=decision_logs.console=true", "/policies"]