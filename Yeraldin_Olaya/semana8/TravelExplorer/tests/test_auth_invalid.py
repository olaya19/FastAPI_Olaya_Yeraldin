def test_token_invalido(client):
    # Token basura
    r = client.get("/viajes/", headers={"Authorization": "Bearer fake_token"})
    assert r.status_code == 401
