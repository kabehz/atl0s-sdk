import requests

def test_opa_authorization_allow_architect():
    input_data = {
        "input": {
            "user": {"role": "architect"},
            "action": "invoke_private_logic"
        }
    }
    res = requests.post("http://localhost:8181/v1/data/legal_validator/authz/allow", json=input_data)
    assert res.status_code == 200
    assert res.json().get("result") is True

def test_opa_authorization_deny_collaborator():
    input_data = {
        "input": {
            "user": {"role": "collaborator"},
            "action": "invoke_private_logic"
        }
    }
    res = requests.post("http://localhost:8181/v1/data/legal_validator/authz/allow", json=input_data)
    assert res.status_code == 200
    assert res.json().get("result") is False