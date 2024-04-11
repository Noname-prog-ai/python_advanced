from datetime import datetime

from flask import Flask

app = Flask(__name__)

greetings = (
    'хорошего понедельника',
    'хорошего вторника',
    'хорошей среды',
    'хорошего четверга',
    'хорошей пятницы',
    'хорошей субботы',
    'хорошего воскресенья'
)

def get_weekday_from_username(username: str) -> str:
    return username.split()[-1]

@app.route('/hello-world/<name>')
def hello_world(name: str) -> str:
    weekday = datetime.today().weekday()
    greeting = greetings[weekday]
    return f'привет, {name}. {greeting}!'


if __name__ == '__main__':
    app.run(debug=True)
