import pytest  # noqa: F401  # Import presente aunque no se use directamente


def test_obtener_viaje(client, auth_headers, viaje_base):
    # primero crear
    client.post(
        "/viajes/",
        json=viaje_base,
        headers=auth_headers,
    )
    r = client.get(
        f"/viajes/{viaje_base['id']}",
        headers=auth_headers,
    )
    assert r.status_code == 200
    assert r.json()["id"] == viaje_base["id"]


def test_actualizar_viaje(client, auth_headers, viaje_base):
    client.post(
        "/viajes/",
        json=viaje_base,
        headers=auth_headers,
    )
    update = {"destino": "Santa Marta", "cupo": 40}
    r = client.put(
        f"/viajes/{viaje_base['id']}",
        json=update,
        headers=auth_headers,
    )
    assert r.status_code == 200
    data = r.json()
    assert data["destino"] == "Santa Marta"
    assert data["cupo"] == 40


def test_eliminar_viaje(client, auth_headers, viaje_base):
    client.post(
        "/viajes/",
        json=viaje_base,
        headers=auth_headers,
    )
    r = client.delete(
        f"/viajes/{viaje_base['id']}",
        headers=auth_headers,
    )
    assert r.status_code == 204
    # verificar que ya no existe
    r2 = client.get(
        f"/viajes/{viaje_base['id']}",
        headers=auth_headers,
    )
    assert r2.status_code == 404
