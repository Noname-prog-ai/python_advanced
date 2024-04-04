"""
Реализуйте endpoint, начинающийся с /max_number, в который можно передать список чисел, разделённых слешем /.
Endpoint должен вернуть текст «Максимальное переданное число {number}»,
где number — выделенное курсивом наибольшее из переданных чисел.

Примеры:

/max_number/10/2/9/1
Максимальное число: 10

/max_number/1/1/1/1/1/1/1/2
Максимальное число: 2

"""

from flask import Flask


app = Flask(__name__)


@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    number_list = numbers.split('/')

    # Фильтруем введенные значения, оставляя только числа
    number_list = [num for num in number_list if num.isdigit()]

    if not number_list:
        return "Нет переданных чисел"

    max_number = max(int(num) for num in number_list)

    return f"Максимальное число: {max_number}"


if __name__ == "__main__":
    app.run()
