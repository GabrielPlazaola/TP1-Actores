# Ejemplo de configuración de un clúster de Ray en una máquina local

import ray

# Inicializar el clúster de Ray en modo local (en una sola máquina)
ray.init(ignore_reinit_error=True)

# Definir un actor remoto
@ray.remote
class MyActor:
    def __init__(self):
        pass

    def get_node_id(self):
        # Obtener el ID del nodo en el que se ejecuta este actor
        return ray.worker.global_worker.node.unique_id

# Crear varias instancias de MyActor en nodos diferentes
actors = [MyActor.remote() for _ in range(4)]

# Obtener el ID del nodo en el que se ejecuta cada actor
node_ids = ray.get([actor.get_node_id.remote() for actor in actors])

# Mostrar los IDs de los nodos para cada actor
for i, node_id in enumerate(node_ids):
    print(f"Actor {i + 1} se ejecuta en el nodo: {node_id}")

# Finalizar el clúster de Ray
ray.shutdown()
print("FIN")