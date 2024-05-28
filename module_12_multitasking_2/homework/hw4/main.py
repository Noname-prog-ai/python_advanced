import requests
import threading
from queue import Queue
from datetime import datetime
import time

# Функция для получения timestamp с сервера
def get_timestamp():
    response = requests.get('http://127.0.0.1:8080/timestamp/1549892280') # Можно использовать текущий timestamp
    return response.text

# Функция для записи логов в файл
def write_log(timestamp, message):
    with open('logs.txt', 'a') as file:
        file.write(f'{timestamp} {message}\n')

# Функция для работы каждого потока
def thread_function(thread_id, timestamp):
    for _ in range(20):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        write_log(timestamp, f'Thread {thread_id} | Time: {current_time}')
        time.sleep(1)

# Очередь для хранения timestamp
q = Queue()

# Получаем timestamp с сервера
timestamp = get_timestamp()
q.put(timestamp)

# Создаем и запускаем 10 потоков
threads = []
for i in range(10):
    t = threading.Thread(target=thread_function, args=(i+1, q.get()))
    threads.append(t)
    t.start()

# Ждем завершения всех потоков
for t in threads:
    t.join()

# Сортируем логи по timestamp
with open('logs.txt', 'r') as file:
    lines = file.readlines()
    lines.sort(key=lambda x: float(x.split()[0]))

# Перезаписываем файл с отсортированными логами
with open('logs.txt', 'w') as file:
    for line in lines:
        file.write(line)