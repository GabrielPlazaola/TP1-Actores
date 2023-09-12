import ray
import time
from actor_file import MyActor  # Importa el actor desde el Archivo 2

ray.init(ignore_reinit_error=True)

#Generaciones a tomar
gens = [1,3]

#Tipos a tomar
#tipos = ['Planta','Fuego','Agua','Normal','Eléctrico','Bicho','Roca','Volador','Psíquico','Tierra','Veneno','Lucha','Fantasma','Hielo','Dragón','Siniestro','Acero','Hada']
tipos = ['Planta','Fuego','Agua']

# Crea varias instancias de MyActor en diferentes procesos
actors = [MyActor.remote() for _ in range(len(gens))]

# Llama a los métodos de los actores en paralelo
results = ray.get([actor.generacion.remote(gens[actors.index(actor)], tipos) for actor in actors])

# Imprime los resultados
for i, result in enumerate(results):
    print(f"Actor {i + 1} resultado: {result}")

ray.shutdown()