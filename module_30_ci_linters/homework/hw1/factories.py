import factory
from factory import Faker
from app import Client, Parking

class ClientFactory(factory.SQLAlchemyModelFactory):
    class Meta:
        model = Client
        sqlalchemy_session = db.session

    name = Faker('first_name')
    surname = Faker('last_name')
    credit_card = Faker('credit_card_number')
    car_number = Faker('license_plate')

class ParkingFactory(factory.SQLAlchemyModelFactory):
    class Meta:
        model = Parking
        sqlalchemy_session = db.session

    address = Faker('address')
    opened = Faker('boolean')
    count_places = factory.LazyAttribute(lambda _: factory.Faker('random_int', min=1, max=20).generate())
    count_available_places = factory.SelfAttribute('count_places')

# Теперь вы можете переписать тесты, используя созданные фабрики:


from factories import ClientFactory, ParkingFactory

def test_create_client_using_factory(client):
    new_client = ClientFactory()
    response = client.post('/clients', json={
        'name': new_client.name,
        'surname': new_client.surname,
        'car_number': new_client.car_number,
        'credit_card': new_client.credit_card
    })
    assert response.status_code == 201

def test_create_parking_using_factory(client):
    new_parking = ParkingFactory()
    response = client.post('/parkings', json={
        'address': new_parking.address,
        'count_places': new_parking.count_places,
        'opened': new_parking.opened
    })
    assert response.status_code == 201