"""
Реализуйте endpoint, который показывает превью файла, принимая на вход два параметра: SIZE (int) и RELATIVE_PATH —
и возвращая первые SIZE символов файла по указанному в RELATIVE_PATH пути.

Endpoint должен вернуть страницу с двумя строками.
В первой строке будет содержаться информация о файле: его абсолютный путь и размер файла в символах,
а во второй строке — первые SIZE символов из файла:

<abs_path> <result_size><br>
<result_text>

где abs_path — написанный жирным абсолютный путь до файла;
result_text — первые SIZE символов файла;
result_size — длина result_text в символах.

Перенос строки осуществляется с помощью HTML-тега <br>.

Пример:

/head_file/8/docs/simple.txt
/home/user/module_2/docs/simple.txt 8
hello wo

/head_file/12/docs/simple.txt
/home/user/module_2/docs/simple.txt 12
hello world!
"""

from flask import Flask
import os

app = Flask(__name__)


@app.route('/head_file/<int:size>/<path:relative_path>')
def head_file(size, relative_path):
    try:
        abs_path = os.path.abspath(relative_path)

        with open(abs_path, 'r') as file:
            content = file.read(size)
            content_size = len(content)

        return f"<b>{abs_path}</b> {content_size}<br>{content}"

    except FileNotFoundError:
        return "Файл не найден"
    except IsADirectoryError:
        return "Указанный путь ведет к директории"


if __name__ == "__main__":
    app.run()
