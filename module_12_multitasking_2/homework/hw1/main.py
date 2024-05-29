import requests
import threading
from multiprocessing.dummy import Pool as ThreadPool
import time

# функция для загрузки данных о персонаже через api и записи в бд
def get_character_data(character_id):
    url = f"https://swapi.dev/api/people/{character_id}/"
    response = requests.get(url)
    character_data = response.json()

    # здесь можно добавить код для записи данных в бд

    print(f"name: {character_data['name']}, age: {character_data['birth_year']}, gender: {character_data['gender']}")

# функция для последовательного выполнения запросов
def sequential_requests():
    start_time = time.time()
    for i in range(1, 21):
        get_character_data(i)
    end_time = time.time()
    print(f"sequential execution time: {end_time - start_time} seconds")

# функция для параллельного выполнения запросов с использованием pool
def pool_requests():
    start_time = time.time()
    pool = ThreadPool(5)  # указываем количество потоков
    results = pool.map(get_character_data, range(1, 21))  # запускаем задачи параллельно
    pool.close()
    pool.join()
    end_time = time.time()
    print(f"pool execution time: {end_time - start_time} seconds")

# функция для параллельного выполнения запросов с использованием потоков
def threaded_requests():
    start_time = time.time()
    threads = []
    for i in range(1, 21):
        thread = threading.Thread(target=get_character_data, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"threaded execution time: {end_time - start_time} seconds")

# вызываем функции для замера времени выполнения
sequential_requests()
pool_requests()
threaded_requests()