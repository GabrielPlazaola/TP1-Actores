import multiprocessing

# Define una función para un actor
def actor_func(actor_id, inbox):
    while True:
        message = inbox.get()
        if message == "terminate":
            break
        print(f"Actor {actor_id} recibió el mensaje: {message}")

if __name__ == "__main__":
    num_actors = 4
    actors = []

    for i in range(num_actors):
        inbox = multiprocessing.Queue()
        actor = multiprocessing.Process(target=actor_func, args=(i, inbox))
        actor.start()
        actors.append((actor, inbox))

    # Envía mensajes a los actores
    for i in range(num_actors):
        actors[i][1].put(f"Mensaje {i}")

    # Termina los actores
    for i in range(num_actors):
        actors[i][1].put("terminate")

    for actor, _ in actors:
        actor.join()
