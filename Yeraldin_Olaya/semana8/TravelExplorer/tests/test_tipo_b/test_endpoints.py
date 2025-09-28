def test_crear_viaje(client, viaje_base, auth_headers):
    response = client.post("/viajes/", json=viaje_base, headers=auth_headers)
    assert response.status_code == 201
    data = response.json()
    assert data["destino"] == viaje_base["destino"]
    assert data["cupo"] == viaje_base["cupo"]


def test_listar_viajes(client, auth_headers):
    response = client.get("/viajes/", headers=auth_headers)
    assert response.status_code == 200
    viajes = response.json()
    assert isinstance(viajes, list)
    assert viajes[0]["destino"] == "Cartagena"
