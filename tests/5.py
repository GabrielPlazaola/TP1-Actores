import pykka
from pykka import ThreadingActor, ThreadingFuture, Actor

class MyActor(pykka.Actor):
    def on_receive(self, message):
        print(f"Actor {self}: Received message: {message}")

actor1 = MyActor.start()
actor2 = MyActor.start()

actor1.tell("Hello from actor1 to actor2")
actor2.tell("Hello from actor2 to actor1")

pykka.ActorRegistry.stop_all()
