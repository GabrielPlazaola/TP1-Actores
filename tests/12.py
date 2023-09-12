import ray
import time

ray.init(ignore_reinit_error=True)

# Define un actor remoto
@ray.remote
class MyActor:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value

# Crea varias instancias de MyActor en diferentes procesos
actors = [MyActor.remote() for _ in range(3)]

# Llama a los métodos de los actores en paralelo
results = ray.get([actor.increment.remote() for actor in actors])

# Imprime los resultados
for i, result in enumerate(results):
    print(f"Actor {i + 1} resultado: {result}")

ray.shutdown()