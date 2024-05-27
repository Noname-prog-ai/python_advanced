import threading
import queue
import time

class Task:
    def __init__(self, priority, function, args):
        self.priority = priority
        self.function = function
        self.args = args

class Producer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        print("Producer: Running")
        tasks = [
            Task(0, time.sleep, (0.019658567230089852,)),
            Task(0, time.sleep, (0.8260261640443046,)),
            Task(1, time.sleep, (0.5049788914608555,)),
            Task(1, time.sleep, (0.9939451305978486,)),
            Task(2, time.sleep, (0.6217303299399963,)),
            Task(2, time.sleep, (0.7283236739267553,)),
            Task(3, time.sleep, (0.13090364153051426,)),
            Task(3, time.sleep, (0.21140406953974167,)),
            Task(4, time.sleep, (0.8426715099235477,)),
            Task(6, time.sleep, (0.43248434769420785,))
        ]

        for task in tasks:
            self.queue.put((task.priority, task.function, task.args))
        print("Producer: Done")

class Consumer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        print("Consumer: Running")
        while True:
            priority, function, args = self.queue.get()
            if function is None:
                break
            print(f">running Task(priority={priority}). sleep({args[0]})")
            function(*args)
            self.queue.task_done()
        print("Consumer: Done")

if __name__ == "__main__":
    q = queue.PriorityQueue()
    producer = Producer(q)
    consumer = Consumer(q)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()