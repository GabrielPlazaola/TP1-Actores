import pykka

# Definimos una subclase personalizada de Actor
class MyActor(pykka.Actor):
    def __init__(self):
        super().__init__()
        self.state = 0

    def on_receive(self, message):
        if message == "increment":
            self.state += 1
        elif message == "get_state":
            self.actor_ref.tell(self.state)

# Creamos una instancia de MyActor
actor = MyActor.start()

# Enviamos mensajes al actor
actor.tell("increment")
actor.tell("increment")

# Obtenemos el estado actual del actor
state_future = actor.ask("get_state")
state = state_future.get()

print(f"State of actor: {state}")

# Detenemos el actor
actor.stop()
