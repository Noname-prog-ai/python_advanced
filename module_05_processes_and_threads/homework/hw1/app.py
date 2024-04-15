"""
Консольная утилита lsof (List Open Files) выводит информацию о том, какие файлы используют какие-либо процессы.
Эта команда может рассказать много интересного, так как в Unix-подобных системах всё является файлом.

Но нам пока нужна лишь одна из её возможностей.
Запуск lsof -i :port выдаст список процессов, занимающих введённый порт.
Например, lsof -i :5000.

Как мы с вами выяснили, наш сервер отказывается запускаться, если кто-то занял его порт. Напишите функцию,
которая на вход принимает порт и запускает по нему сервер. Если порт будет занят,
она должна найти процесс по этому порту, завершить его и попытаться запустить сервер ещё раз.
"""
from typing import List
import os
import subprocess
from flask import Flask

app = Flask(__name__)

def get_pids(port: int) -> List[int]:
    """
    возвращает список pid процессов, занимающих переданный порт
    @param port: порт
    @return: список pid процессов, занимающих порт
    """
    if not isinstance(port, int):
        raise ValueError

    pids: List[int] = []
    output = subprocess.check_output(['lsof', '-ti', f':{port}'])
    for line in output.decode().splitlines():
        pids.append(int(line))
    return pids

def free_port(port: int) -> None:
    """
    завершает процессы, занимающие переданный порт
    @param port: порт
    """
    pids: List[int] = get_pids(port)
    for pid in pids:
        os.system(f'kill {pid}')

def run(port: int) -> None:
    """
    запускает flask-приложение по переданному порту.
    если порт занят каким-либо процессом, завершает его.
    @param port: порт
    """
    free_port(port)
    app.run(port=port)

if __name__ == '__main':
    run(5000)
