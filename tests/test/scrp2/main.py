import ray
from actor_gen import MyActorGen

@ray.remote
class ActorTest:
    def __init__(self) -> None:
        self.factor = 10
    
    def do_work(self, n):
        result = self.factor * n
        print(result)
        return result

if __name__ == '__main__':
    ray.init()
    results = []
    for i in range(10):
        actor = ActorTest.remote()
        results.append(actor.do_work.remote(i)) 
    print(ray.get(results))
    ray.shutdown()