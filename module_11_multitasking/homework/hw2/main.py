import requests
import threading
import time


# Функция для загрузки данных о персонаже через API и записи в БД
def get_character_data(character_id):
    url = f"https://swapi.dev/api/people/{character_id}/"
    response = requests.get(url)
    character_data = response.json()

    # Здесь можно добавить код для записи данных в БД

    print(f"Name: {character_data['name']}, Age: {character_data['birth_year']}, Gender: {character_data['gender']}")


# Функция для последовательного выполнения запросов
def sequential_requests():
    start_time = time.time()
    for i in range(1, 21):
        get_character_data(i)
    end_time = time.time()
    print(f"Sequential execution time: {end_time - start_time} seconds")


# Функция для параллельного выполнения запросов с использованием потоков
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
    print(f"Threaded execution time: {end_time - start_time} seconds")


# Вызываем функции для замера времени выполнения
sequential_requests()
threaded_requests()