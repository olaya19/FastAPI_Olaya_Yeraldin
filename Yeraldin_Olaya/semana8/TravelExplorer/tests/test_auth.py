def test_login_ok(client):
    r = client.post("/auth/login", json={"username": "admin", "password": "admin"})
    assert r.status_code == 200
    data = r.json()
    assert "access_token" in data


def test_login_fail(client):
    r = client.post("/auth/login", json={"username": "x", "password": "y"})
    assert r.status_code == 200  # FastAPI devuelve 200 con error en body
    assert "error" in r.json()
