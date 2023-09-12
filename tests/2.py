from pykka import ThreadingActor

# Define un actor para realizar la suma
class ActorSuma(ThreadingActor):
    def __init__(self):
        super().__init__()

    def on_receive(self, message):
        res = message[0] + message[1]
        print(res)
        return res

# Crea una instancia del actor
actor_suma = ActorSuma.start()

# Envía dos números al actor
num1 = 5
num2 = 7
resp = actor_suma.tell([num1, num2])

# Detén el actor
actor_suma.stop()
