import requests

def test_opa_allow_architect():
    res = requests.post("http://localhost:8181/v1/data/legal_validator/authz/allow", json={
        "input": {"user": {"role": "architect"}, "action": "invoke_private_logic"}
    })
    assert res.status_code == 200
    assert res.json().get("result") is True

def test_opa_deny_collaborator():
    res = requests.post("http://localhost:8181/v1/data/legal_validator/authz/allow", json={
        "input": {"user": {"role": "collaborator"}, "action": "invoke_private_logic"}
    })
    assert res.status_code == 200
    assert res.json().get("result") is False