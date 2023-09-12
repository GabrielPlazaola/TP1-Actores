from pykka import ThreadingActor
import time

# Define un actor personalizado que hereda de ThreadingActor
class MyActor(ThreadingActor):
    def __init__(self):
        super().__init__()

    def on_receive(self, message):
        print(f"Actor recibió el mensaje: {message}")
        return message
    
    def sumar(self, i):
        resultado = i[0] + i[1]
        return resultado

if __name__ == "__main__":
    # Configura Pykka para utilizar procesos en lugar de hilos
    ThreadingActor.start_default_use_threads = False

    # Crea dos instancias de actores en diferentes procesos
    actor1 = MyActor.start()
    actor2 = MyActor.start()

    # Envía mensajes a los actores
    actor1.tell("Mensaje para Actor 1")
    actor2.tell("Mensaje para Actor 2")

    nums = [2, 3]
    res = actor1.sumar(nums)
    print(res)

    # Detiene los actores
    actor1.stop()
    actor2.stop()