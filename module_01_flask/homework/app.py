import random
import datetime
import os
from flask import Flask

app = Flask(__name__)

car_list = ["chevrolet", "renault", "ford", "lada"]
cat_list = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]
base_dir = os.path.dirname(os.path.abspath(__file__))
book_file = os.path.join(base_dir, 'war_and_peace.txt')

def get_words():
    with open(book_file, 'r') as book:
        text = book.read()
        words = re.findall(r'\b\w+\b', text)
        return words

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
def get_random_word():
    words = get_words()
    random_word = random.choice(words)
    return random_word

# Counter variable
counter_visits = 0

@app.route('/counter')
def counter():
    global counter_visits
    counter_visits += 1
    return str(counter_visits)

if __name__ == '__main__':
    app.run()
