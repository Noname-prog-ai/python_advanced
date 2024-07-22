from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
import random

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
    has_sale = db.Column(db.Boolean)
    address = db.Column(db.JSON)
    coffee_id = db.Column(db.Integer, db.ForeignKey('coffee.id'))

@app.before_first_request
def create_test_data():
    for _ in range(10):
        coffee_response = requests.get("https://random-data-api.com/api/coffee/random_coffee").json()
        new_coffee = Coffee(
            title=coffee_response['blend_name'],
            origin=coffee_response['origin'],
            notes=coffee_response['notes'],
            intensifier=coffee_response['intensifier']
        )
        db.session.add(new_coffee)

    for _ in range(10):
        user_response = requests.get("https://random-data-api.com/api/address/random_address").json()
        new_user = User(
            name="Random User",
            address=user_response,
            coffee_id=random.randint(1, 10)  # Important: Ensure this id exists in Coffee table
        )
        db.session.add(new_user)

    db.session.commit()

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(
        name=data['name'],
        address=data['address'],
        has_sale=data.get('has_sale', False),
        coffee_id=data['coffee_id']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added!", "user": {
        "id": new_user.id,
        "name": new_user.name,
        "address": new_user.address,
        "has_sale": new_user.has_sale,
        "coffee_id": new_user.coffee_id
    }}), 201

@app.route('/search_coffee', methods=['GET'])
def search_coffee():
    title = request.args.get('title')
    coffee = Coffee.query.filter(Coffee.title.ilike(f'%{title}%')).all()
    return jsonify([{
        "id": c.id,
        "title": c.title,
        "origin": c.origin,
        "intensifier": c.intensifier,
        "notes": c.notes
    } for c in coffee]), 200

@app.route('/unique_notes', methods=['GET'])
def unique_notes():
    notes = db.session.query(Coffee.notes).distinct()
    unique_notes_list = {note for sublist in notes for note in sublist if note is not None}
    return jsonify(list(unique_notes_list)), 200

@app.route('/users_in_country/<country>', methods=['GET'])
def users_in_country(country):
    users = User.query.filter(User.address['country'].astext == country).all()
    return jsonify([{
        "id": u.id,
        "name": u.name,
        "address": u.address,
        "has_sale": u.has_sale,
        "coffee_id": u.coffee_id
    } for u in users]), 200

if __name__ == '__main__':
    app.run(debug=True)