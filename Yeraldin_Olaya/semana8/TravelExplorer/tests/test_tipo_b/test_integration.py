def test_flujo_completo(client, auth_headers):
    viaje = {
        "id": 2,
        "destino": "Medellín",
        "fecha_salida": "2025-11-10T09:00:00",
        "fecha_regreso": "2025-11-15T20:00:00",
        "cupo": 25,
    }
    r = client.post("/viajes/", json=viaje, headers=auth_headers)
    assert r.status_code == 201

    r = client.get("/viajes/", headers=auth_headers)
    assert r.status_code == 200
    destinos = [v["destino"] for v in r.json()]
    assert "Medellín" in destinos
