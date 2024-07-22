from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<username>:<password>@db:5432/skillbox_db'
db = SQLAlchemy(app)

class Coffee(db.Model):
    __tablename__ = 'coffee'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    origin = db.Column(db.String(200))
    intensifier = db.Column(db.String(100))
    notes = db.Column(db.ARRAY(db.String))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.JSON)
    coffee_id = db.Column(db.Integer, db.ForeignKey('coffee.id'))

@app.before_first_request
def create_records():
    for _ in range(10):
        response_coffee = requests.get('https://random-data-api.com/api/coffee/random_coffee').json()
        response_address = requests.get('https://random-data-api.com/api/address/random_address').json()

        coffee = Coffee(
            title=response_coffee['blend_name'],
            origin=response_coffee['origin'],
            notes=response_coffee['notes'],
            intensifier=response_coffee['intensifier']
        )

        user = User(
            name='Random User',
            address=response_address,
            coffee=coffee
        )

        db.session.add(coffee)
        db.session.add(user)

    db.session.commit()

@app.route('/add_user', methods=['POST'])
def add_user():
    # Логика добавления пользователя
    pass

@app.route('/search_coffee/<title>', methods=['GET'])
def search_coffee(title):
    # Логика поиска кофе по названию
    pass

@app.route('/unique_notes', methods=['GET'])
def unique_notes():
    # Логика получения уникальных заметок
    pass

@app.route('/users_by_country/<country>', methods=['GET'])
def users_by_country(country):
    # Логика получения пользователей по стране
    pass