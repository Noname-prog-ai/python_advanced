import random
import datetime
import os
from flask import Flask

app = Flask(__name__)

car_list = ["chevrolet", "renault", "ford", "lada"]
cat_list = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]
words = []

def generate_word_list():
    with open('war_and_peace.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        words.extend(text.split())

generate_word_list()

def get_random_word():
    return random.choice(words)

def get_current_time():
    current_time = datetime.datetime.now()
    return current_time.strftime("%H:%M:%S")

def get_time_after_one_hour():
    current_time = datetime.datetime.now()
    time_after_one_hour = current_time + datetime.timedelta(hours=1)
    return time_after_one_hour.strftime("%H:%M:%S")

@app.route('/hello_world')
def hello_world():
    return "привет, мир!"

@app.route('/cars')
def cars():
    return ', '.join(car_list)

@app.route('/cats')
def cats():
    random_cat = random.choice(cat_list)
    return random_cat

@app.route('/get_time/now')
def get_current_time_page():
    current_time = get_current_time()
    return f"точное время: {current_time}"

@app.route('/get_time/future')
def get_time_after_hour():
    time_after_one_hour = get_time_after_one_hour()
    return f"точное время через час будет {time_after_one_hour}"

@app.route('/get_random_word')
def random_word():
    word = get_random_word()
    return f"Random word from 'War and Peace': {word}"

# Counter variable
counter_visits = 0

@app.route('/counter')
def counter():
    global counter_visits
    counter_visits += 1
    return str(counter_visits)

if __name__ == '__main__':
    app.run()