import ray
import time

# Define un actor remoto
@ray.remote
class MyActor:
    def __init__(self):
        self.value = 0

    def increment(self):
        time.sleep(3)
        self.value += 1
        return self.value
