from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    host = "http://127.0.0.1:51811"
    wait_time = between(1, 5)

    @task
    def index(self):
        self.client.get("/")