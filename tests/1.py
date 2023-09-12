from pykka import ThreadingActor

# Define un actor simple
class MiActor(ThreadingActor):
    def __init__(self):
        super().__init__()

    def on_receive(self, message):
        # Este método se llama cuando el actor recibe un mensaje
        print(f"MiActor recibió: {message}")

# Crea instancias de los actores
actor1 = MiActor.start()
actor2 = MiActor.start()

# Envía mensajes entre los actores
actor1.tell("Hola, Actor 2")
actor2.tell("Hola, Actor 1")

# Detén los actores
actor1.stop()
actor2.stop()
