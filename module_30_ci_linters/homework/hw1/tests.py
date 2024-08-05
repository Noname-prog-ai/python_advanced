def test_get_clients(client, db, client_data):
    response = client.post('/clients', json=client_data)
    assert response.status_code == 201
    response = client.get('/clients')
    assert response.status_code == 200
    assert len(response.json) == 1

def test_create_parking(client, db, parking_data):
    response = client.post('/parkings', json=parking_data)
    assert response.status_code == 201

def test_client_parking_in(client, db, client_data, parking_data):
    client_response = client.post('/clients', json=client_data)
    parking_response = client.post('/parkings', json=parking_data)

    data = {'client_id': client_response.json['id'], 'parking_id': parking_response.json['id']}

    response = client.post('/client_parkings', json=data)
    assert response.status_code == 201

def test_client_parking_out(client, db, client_data, parking_data):
    client_response = client.post('/clients', json=client_data)
    parking_response = client.post('/parkings', json=parking_data)

    entry_data = {'client_id': client_response.json['id'], 'parking_id': parking_response.json['id']}
    client.post('/client_parkings', json=entry_data)

    response = client.delete('/client_parkings', json=entry_data)
    assert response.status_code == 200