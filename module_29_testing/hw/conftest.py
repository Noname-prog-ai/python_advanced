import pytest
from app import create_app, db, Client, Parking, ClientParking

@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture
def db(app):
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()

@pytest.fixture
def client_data():
    return {'name': 'John', 'surname': 'Doe', 'car_number': 'ABC123', 'credit_card': '1234567890123456'}

@pytest.fixture
def parking_data():
    return {'address': '123 Park Ave', 'count_places': 5, 'opened': True}