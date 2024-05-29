import requests
import threading
import time
import logging
from queue import Queue
from datetime import datetime

queue = Queue()
data = {}


def get_date(timestamp: float) -> str:
    response = requests.get(f'http://127.0.0.1:8080/timestamp/{timestamp}')
    return response.text


class Worker(threading.Thread):

    def run(self):
        current_timestamp = datetime.now().timestamp()
        data[current_timestamp] = None
        queue.put(current_timestamp)
        server_response = get_date(current_timestamp)
        data[current_timestamp] = server_response
        time.sleep(1)


workers = []
for _ in range(10):
    worker = Worker()
    worker.start()
    workers.append(worker)

while not queue.empty():
    timestamp = queue.get()
    while data.get(timestamp) is None:
        continue
    logging.info(f'{timestamp} -- {data[timestamp]}')

for worker in workers:
    worker.join()