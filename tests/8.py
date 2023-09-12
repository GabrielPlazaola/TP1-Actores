from pykka import ThreadingActor
import Pyro4

# Define un actor personalizado que hereda de ThreadingActor
class MyActor(ThreadingActor):
    def __init__(self):
        super().__init__()

    def on_receive(self, message):
        print(f"Actor recibió el mensaje: {message}")

if __name__ == "__main__":
    from pykka import ThreadingActor
    import Pyro4

    # Configura Pykka para utilizar Pyro para comunicación entre procesos
    ThreadingActor.start_default_use_threads = False
    ThreadingActor.start_default_use_pyro = True

    # Crea una instancia del actor
    actor = MyActor.start()

    # Registra el actor con Pyro
    daemon = Pyro4.Daemon()
    uri = daemon.register(actor)

    # Comienza el servicio Pyro para permitir la comunicación entre procesos
    with Pyro4.Proxy(uri) as proxy:
        # Envía mensajes al actor en otro proceso
        proxy.tell("Mensaje 1")
        proxy.tell("Mensaje 2")

    # Detiene el actor
    actor.stop()