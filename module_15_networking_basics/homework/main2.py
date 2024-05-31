from flask import make_response, Flask, request, jsonify, g
import sqlite3

app = Flask(__name__)

@app.route(rule='/room', methods=['get', 'post', 'delete'])
def get_room():
    try:
        with sqlite3.connect('rooms.sqlite3') as conn:
            cursor = conn.cursor()
            if request.method == 'GET':
                rooms = cursor.execute("SELECT * FROM rooms").fetchall()
                data = [
                    {
                        'roomid': room[0],
                        'floor': room[1],
                        'beds': room[2],
                        'guestnum': room[3],
                        'price': room[4],
                        'links': {'room_info': "/room/" + str(room[0])}
                    }
                    for room in rooms
                ]
                return jsonify({'rooms': data}), 200
            elif request.method == "POST":
                data = request.json
                cursor.execute("INSERT INTO rooms (floor, beds, guestnum, price) VALUES (?, ?, ?, ?)", (data['floor'], data['beds'], data['guestnum'], data['price']))
                conn.commit()
                return jsonify(success=True, message="room is created"), 201
            elif request.method == 'DELETE':
                data = request.json
                room_id = data.get('roomid')
                room = cursor.execute("SELECT * FROM rooms WHERE roomid = ?", (room_id,)).fetchone()
                if room is None:
                    return jsonify(error='Room not found'), 404
                cursor.execute("DELETE FROM rooms WHERE roomid = ?", (room_id,))
                conn.commit()
                response = make_response(jsonify(success=True, deleted_room=f"Room (roomid: {room_id}) successfully deleted"), 200)
                return response
    except Exception as err:
        return jsonify(error=str(err)), 500

@app.route(rule="/room/<int:room_id>", methods=['get', 'post'])
def room_info(room_id):
    try:
        with sqlite3.connect('rooms.sqlite3') as conn:
            cursor = conn.cursor()
            if request.method == 'GET':
                room = cursor.execute("SELECT * FROM rooms WHERE roomid = ?", (room_id,)).fetchone()
                if room is None:
                    return jsonify(error='Room not found'), 404
                response = make_response(jsonify(success=True, bookedroom={'floor': room[1], 'beds': room[2], 'guestnum': room[3], 'price': room[4]}, description="Some description about this room, links to photos."), 200)
                return response
            elif request.method == 'POST':
                room = cursor.execute("SELECT * FROM rooms WHERE roomid = ?", (room_id,)).fetchone()
                if room is None:
                    return jsonify(error='Room not found'), 409
                cursor.execute("INSERT INTO booking SELECT * FROM rooms WHERE roomid = ?", (room_id,))
                cursor.execute("DELETE FROM rooms WHERE roomid = ?", (room_id,))
                conn.commit()
                response = make_response(jsonify(success=True, bookedroom={'floor': room[1], 'beds': room[2], 'guestnum': room[3], 'price': room[4]}, message="Booking is created"), 201)
                return response
    except Exception as err:
        return jsonify(error=str(err)), 500

@app.route(rule='/booking', methods=['get', 'post', 'delete'])
def booking():
    try:
        with sqlite3.connect('rooms.sqlite3') as conn:
            cursor = conn.cursor()
            if request.method == 'GET':
                rooms = cursor.execute("SELECT * FROM booking").fetchall()
                data = [
                    {
                        'roomid': room[0],
                        'floor': room[1],
                        'beds': room[2],
                        'guestnum': room[3],
                        'price': room[4],
                        'links': {'booking_info': '/room/' + str(room[0])}
                    }
                    for room in rooms
                ]
                return jsonify({'rooms': data}), 200
            elif request.method == 'POST':
                data = request.json
                room_id = data.get('roomid')
                room = cursor.execute("SELECT * FROM rooms WHERE roomid = ?", (room_id,)).fetchone()
                if room is None:
                    return jsonify(error='Room not found'), 409
                cursor.execute("INSERT INTO booking SELECT * FROM rooms WHERE roomid = ?", (room_id,))
                cursor.execute("DELETE FROM rooms WHERE roomid = ?", (room_id,))
                conn.commit()
                response = make_response(jsonify(success=True, bookedroom={'floor': room[1], 'beds': room[2], 'guestnum': room[3], 'price': room[4]}, message="Booking is created"), 201)
                return response
            elif request.method == 'DELETE':
                data = request.json
                room_id = data.get('roomid')
                room = cursor.execute("SELECT * FROM booking WHERE roomid = ?", (room_id,)).fetchone()
                if room is None:
                    return jsonify(error="Room not found"), 404
                cursor.execute("INSERT INTO rooms SELECT * FROM booking WHERE roomid = ?", (room_id,))
                cursor.execute("DELETE FROM booking WHERE roomid = ?", (room_id,))
                conn.commit()
                response = make_response(jsonify(success=True, message=f"Booking cancellation successful for roomid: {room_id}"), 200)
                return response
    except Exception as err:
        return jsonify(error=str(err)), 500

@app.route('/booking/<int:room_id>', methods=['GET'])
def booking_info(room_id):
    try:
        with sqlite3.connect('rooms.sqlite3') as conn:
            cursor = conn.cursor()
            room = cursor.execute("SELECT * FROM booking WHERE roomid = ?", (room_id,)).fetchone()
            if room is None:
                return jsonify(error='Room not found'), 404
            return jsonify(success=True, bookedroom={'floor': room[1], 'beds': room[2], 'guestnum': room[3], 'price': room[4]})
    except Exception as err:
        return jsonify(error=str(err)), 500


if __name__ == '__main__':
    app.run(debug=True)