import ray
import time
from actor_file import MyActor  # Importa el actor desde el Archivo 2

ray.init(ignore_reinit_error=True)

# Crea varias instancias de MyActor en diferentes procesos
actors = [MyActor.remote() for _ in range(3)]

# Llama a los métodos de los actores en paralelo
results = ray.get([actor.increment.remote() for actor in actors])

# Imprime los resultados
for i, result in enumerate(results):
    print(f"Actor {i + 1} resultado: {result}")

ray.shutdown()