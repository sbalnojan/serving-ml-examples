from locust import HttpLocust, TaskSet, task
import numpy as np

class UserBehavior(TaskSet):
    @task(1)
    def get_prediction(self):
        self.client.get("/predict/" + str(np.random.randint(1,1000)) + "/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000