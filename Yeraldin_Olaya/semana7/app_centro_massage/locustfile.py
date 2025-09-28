from locust import HttpUser, between, task


class CentroMasajesUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def list_massages(self):
        self.client.get("/massages")

    @task(1)
    def create_massage(self):
        self.client.post(
            "/massages",
            json={
                "terapeuta": "Juan Perez",
                "hora": "10:00",
                "sesion": "Masaje relajante",
            },
        )
