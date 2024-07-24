from flask import request, jsonify

app = create_app()

@app.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([{'id': client.id, 'name': client.name, 'surname': client.surname} for client in clients]), 200

@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = Client.query.get_or_404(client_id)
    return jsonify({'id': client.id, 'name': client.name, 'surname': client.surname}), 200

@app.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    new_client = Client(
        name=data['name'],
        surname=data['surname'],
        credit_card=data.get('credit_card'),
        car_number=data.get('car_number')
    )
    db.session.add(new_client)
    db.session.commit()
    return jsonify({'id': new_client.id}), 201

@app.route('/parkings', methods=['POST'])
def create_parking():
    data = request.json
    new_parking = Parking(
        address=data['address'],
        opened=data.get('opened', True),
        count_places=data['count_places'],
        count_available_places=data['count_places']
    )
    db.session.add(new_parking)
    db.session.commit()
    return jsonify({'id': new_parking.id}), 201

@app.route('/client_parkings', methods=['POST'])
def client_parking_in():
    data = request.json
    client = Client.query.get_or_404(data['client_id'])
    parking = Parking.query.get_or_404(data['parking_id'])

    if not parking.opened or parking.count_available_places <= 0:
        return jsonify({'message': 'Parking is closed or full'}), 400

    new_log = ClientParking(client_id=client.id, parking_id=parking.id)
    parking.count_available_places -= 1
    db.session.add(new_log)
    db.session.commit()
    return jsonify({'id': new_log.id}), 201

@app.route('/client_parkings', methods=['DELETE'])
def client_parking_out():
    data = request.json
    log = ClientParking.query.filter_by(client_id=data['client_id'], parking_id=data['parking_id']).first_or_404()

    # Здесь должна быть логика оплаты (проверка наличия карты и т.д.)
    log.time_out = datetime.utcnow()  # Установим время выезда.

    parking = Parking.query.get(log.parking_id)
    parking.count_available_places += 1

    db.session.commit()
    return jsonify({'id': log.id}), 200