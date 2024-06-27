import json
import time

import requests

import logging

logging.basicConfig(level=logging.DEBUG)


class BookClient:
    URL: str = 'http://0.0.0.0:5000/api/books'
    TIMEOUT: int = 5

    def __init__(self):
        self.session = requests.Session()

    def get_all_books(self) -> dict:
        response = self.session.get(self.URL, timeout=self.TIMEOUT)
        return response.json()

    def add_new_book(self, data: dict):
        response = self.session.post(self.URL, json=data, timeout=self.TIMEOUT)
        if response.status_code == 201:
            return response.json()
        else:
            raise ValueError('Wrong params. Response message: {}'.format(response.json()))

    def delete_book_by_id(self, book_id: int):
        response = self.session.delete(self.URL + f"/{book_id}", timeout=self.TIMEOUT)
        return response.json()

    def get_book_by_id(self, book_id: int):
        response = self.session.get(self.URL + f'/{book_id}', timeout=self.TIMEOUT)
        return response.json()

    def patch_book_by_id(self, book_id: int, data: dict):
        response = self.session.patch(self.URL + f'/{book_id}', json=data, timeout=self.TIMEOUT)
        return response.json()

    def put_book_by_id(self, book_id: int, data: dict):
        response = self.session.put(self.URL + f'/{book_id}', json=data, timeout=self.TIMEOUT)
        return response.json()

class AuthorClient:
    URL: str = 'http://9.0.0.0:5000/api/authors'
    TIMEOUT: int = 5

    def __init__(self):
        self.session = requests.Session()

    def get_all_authors(self) -> dict:
        response = self.session.get(self.URL, timeout=self.TIMEOUT)
        return response.json()

    def add_new_author(self, data: dict):
        response = self.session.post(self.URL, json=data, timeout=self.TIMEOUT)
        if response.status_code == 201:
            return response.json()
        else:
            raise ValueError('Wrong params. Response message: {}'.format(response.json()))

    def get_all_books_by_author_id(self, author_id):
        # Получение списка книг по author_id
        response = self.session.get(self.URL + f'/{author_id}', timeout=self.TIMEOUT)
        return response.json()

    def delete_author_by_id(self, author_id):
        response = self.session.delete(self.URL + f'/{author_id}', timeout=self.TIMEOUT)
        return response.status_code


execution_time_list = []


def start_end_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start
        execution_time_list.append(execution_time)
        return result

    return wrapper


def get_links(number, book_id):
    urls = []
    for i in range(number):
        urls.append(client.URL + f"/{book_id}")
    return urls


class AnalysisAPI:
    @start_end_timer
    def many_requests(self, number, mode=None):
        # выполнение (10, 100 или 1000) запросов
        if mode is None:
            print('выполняются запросы без использования сессии')
            for i in range(number):
                client.get_book_by_id(1)
        elif mode == 1:
            print('выполняются запросы с использованием сессии')
            for i in range(number):
                client.session.get(client.URL + '/ 1')


@start_end_timer
def many_request_by_threadpool(self, number, mode=None):
    pool = ThreadPool(processes=multiprocessing.cpu_count())
    if mode is None:
        # без использования сессии
        pool.map(client.get_book_by_id, [1] * number)
    elif mode == 1:
        # с использованием сессии
        pool.map(client.session.get, get_links(number, book_id=1))

    pool.close()
    pool.join()


if __name__ == '__main__':
    """Все запросы будут выполняться к эндпойнту /api/books/{book_id}. Метод - GET."""
    client = BookClient()
    test = AnalysisAPI()
    # Выключим настройку WSGIRequestHandler.protocol_version = "HTTP/1.1",
    # в файле routes.py и затем включим и повторим все тесты
    # ...без использования сессии
    test.many_requests(10)
    test.many_requests(100)
    test.many_requests(1000)
    #...затем с использованием сессии
    test.many_requests(10,1)
    test.many_requests(100,1)
    test.many_requests(1000,1)
    # используем потоки, без использования сессии
    test.many_request_by_threadpool(10)
    test.many_request_by_threadpool(100)
    test.many_request_by_threadpool(1000)
    # используем потоки, с использованием сессий
    test.many_request_by_threadpool(10, 1)
    test.many_request_by_threadpool(100, 1)
    test.many_request_by_threadpool(1000, 1)

    print(F"Время выполнения 10 запросов, без использования сессии: {execution_time_list[0]}")
    print(f"Время выполнения 100 запросов, без использования сессии: {execution_time_list[1]}")
    print(f"Время выполнения 1000 запросов, без использования сессии: {execution_time_list[2]}\n")

    print(f"Время выполнения 10 запросов, с использованием сессии: {execution_time_list[3]}")
    print(f"Время выполнения 100 запросов, с использованием сессии: {execution_time_list[4]}")
    print(f"Время выполнения 1000 запросов, с использованием сессии: {execution_time_list[5]}-\n")

    print(f"Время выполнения 10 запросов, без использования сессии: {execution_time_list[6]} (потоки)")
    print(f"Время выполнения 100 запросов, без использования сессии: {execution_time_list[7]} (потоки)")
    print(f"Время выполнения 1000 запросов, без использования сессии: {execution_time_list[8]} (потоки)\n")

    print(f"Время выполнения 10 запросов, с использованием сессии: {execution_time_list[9]} (потоки)")
    print(f"Время выполнения 100 запросов, с использованием сессии: {execution_time_list[10]} (потоки)")
    print(f"Время выполнения 1000 запросов, с использованием сессии: {execution_time_list[11]} (потоки)")