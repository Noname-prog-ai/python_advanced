"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""

from flask import Flask
from datetime import datetime

app = Flask(__name__)

days_of_week = {
    0: 'понедельника',
    1: 'вторника',
    2: 'среды',
    3: 'четверга',
    4: 'пятницы',
    5: 'субботы',
    6: 'воскресенья'
}

@app.route('/hello-world/<name>')
def hello_world(name):
    weekday = datetime.today().weekday()
    day_of_week = days_of_week[weekday]
    return f"Привет, {name}. Хорошего {day_of_week}!"

if __name__ == "__main__":
    app.run()