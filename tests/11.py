import multiprocessing
import time

class MyActor:
    def __init__(self, actor_id):
        self.actor_id = actor_id
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value

def actor_process(actor_id, result_queue):
    actor = MyActor(actor_id)
    result = actor.increment()
    result_queue.put((actor_id, result))

if __name__ == "__main__":
    num_actors = 3
    result_queue = multiprocessing.Queue()

    processes = []
    for i in range(num_actors):
        process = multiprocessing.Process(target=actor_process, args=(i, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = {}
    while not result_queue.empty():
        actor_id, result = result_queue.get()
        results[actor_id] = result

    print("Results:")
    for actor_id, result in results.items():
        print(f"Actor {actor_id}: {result}")
