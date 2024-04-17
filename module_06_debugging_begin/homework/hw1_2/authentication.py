"""
1. Сконфигурируйте логгер программы из темы 4 так, чтобы он:

* писал логи в файл stderr.txt;
* не писал дату, но писал время в формате HH:MM:SS,
  где HH — часы, MM — минуты, SS — секунды с ведущими нулями.
  Например, 16:00:09;
* выводил логи уровня INFO и выше.

2. К нам пришли сотрудники отдела безопасности и сказали, что, согласно новым стандартам безопасности,
хорошим паролем считается такой пароль, который не содержит в себе слов английского языка,
так что нужно доработать программу из предыдущей задачи.

Напишите функцию is_strong_password, которая принимает на вход пароль в виде строки,
а возвращает булево значение, которое показывает, является ли пароль хорошим по новым стандартам безопасности.
"""

import getpass
import hashlib
import logging

logger = logging.getLogger("password_checker")
# Настройка логгера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='stderr.txt')

def is_strong_password(password: str) -> bool:
    # Проверка наличия английских слов в пароле
    if any(char.isalpha() and char.isascii() for char in password):
        return False
    return True

def input_and_check_password() -> bool:
    logging.debug("начало input_and_check_password")
    password: str = getpass.getpass()

    if not password:
        logging.warning("вы ввели пустой пароль.")
        return False
    elif is_strong_password(password):
        logging.warning("вы ввели слишком слабый пароль")
        return False

    try:
        hasher = hashlib.md5()
        hasher.update(password.encode("latin-1"))
        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        logging.exception("вы ввели некорректный символ ", exc_info=ex)

    return False

if __name__ == "__main__":
    count_number: int = 3
    logging.info(f"вы пытаетесь аутентифицироваться в skillbox. У вас есть {count_number} попыток")

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    logging.error("пользователь трижды ввёл неправильный пароль!")
    exit(1)
