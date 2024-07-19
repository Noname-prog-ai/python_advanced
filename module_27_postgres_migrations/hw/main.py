import os
import requests
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@localhost/skillbox_db'
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
def create_users_and_coffee():
    for _ in range(10):
        coffee_data = requests.get("https://random-data-api.com/api/coffee/random_coffee").json()
        coffee = Coffee(title=coffee_data['blend_name'], origin=coffee_data['origin'],
                        notes=coffee_data['notes'], intensifier=coffee_data['intensifier'])
        db.session.add(coffee)

        user_data = requests.get("https://random-data-api.com/api/address/random_address").json()
        user = User(name=user_data['name'], address=user_data, coffee_id=coffee.id)
        db.session.add(user)
    db.session.commit()

# Define routes for adding a user, searching coffee, etc.

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)