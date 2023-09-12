import ray
import time
from actor_gen import MyActorGen  # Importa el actor desde el Archivo 2
from actor_chara import MyActorChara  # Importa el actor desde el Archivo 3
from top import top_10_pokemon
from tabulate import tabulate

ray.init(ignore_reinit_error=True)

lista_poke = []

#Generaciones a tomar
gens = [1,2]

#Tipos a tomar
#tipos = ['Planta','Fuego','Agua','Normal','Eléctrico','Bicho','Roca','Volador','Psíquico','Tierra','Veneno','Lucha','Fantasma','Hielo','Dragón','Siniestro','Acero','Hada']
tipos = ['Fuego','Agua']

#Caracteristica a tomar
caracteristica = "Velocidad"

# Crea varias instancias de MyActor en diferentes procesos
actors = [MyActorGen.remote() for _ in range(len(gens))]

# Llama a los métodos de los actores en paralelo
results = ray.get([actor.generacion.remote(gens[actors.index(actor)], tipos) for actor in actors])

# Imprime los resultados
for i, result in enumerate(results):
    #print(f"Actor {i + 1} resultado: {result}")
    for a in result:
        lista_poke.append(a)
#print(lista_poke)

# Crea varias instancias de MyActor en diferentes procesos
actors2 = [MyActorChara.remote() for _ in range(len(lista_poke))]

# Llama a los métodos de los actores en paralelo
results = ray.get([actor.buscarpokemon.remote(lista_poke[actors2.index(actor)], caracteristica) for actor in actors2])

# Imprime los resultados
#for i, result in enumerate(results):
    #print(f"Actor {i + 1} resultado: {result}")

resultado_final = top_10_pokemon(results, caracteristica)

tabla = [['Num', 'Pokemon', caracteristica, 'Tipos']]

for pokemon in resultado_final:
    #print(f"{pokemon['Numero']}: {pokemon['Nombre']}: {pokemon[caracteristica]}")
    tabla.append([pokemon['Numero'], pokemon['Nombre'], pokemon[caracteristica], pokemon['Tipos']])

print(tabulate(tabla))

ray.shutdown()