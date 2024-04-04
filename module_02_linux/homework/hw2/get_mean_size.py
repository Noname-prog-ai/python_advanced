"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys


def get_mean_size(data):
    lines = data.split('\n')[1:]  # отбрасываем первую строку
    sizes = [int(line.split()[4]) for line in lines if len(line.split()) > 4]

    if sizes:
        return sum(sizes) // len(sizes)
    else:
        return 0


if __name__ == "__main__":
    data = sys.stdin.read()
    print(get_mean_size(data))
