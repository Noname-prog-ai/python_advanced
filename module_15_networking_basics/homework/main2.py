from flask import make_response, Flask, request, jsonify
import sqlite3

app = Flask(__name__)

class Room:
    def __init__(self, room_id, floor, beds, guestnum, price):
        self.room_id = room_id
        self.floor = floor
        self.beds = beds
        self.guestnum = guestnum
        self.price = price

@app.route('/room', methods=['GET', 'POST', 'DELETE'])
def handle_room():
    try:
        with sqlite3.connect('rooms.sqlite3') as conn:
            cursor = conn.cursor()
            if request.method == 'GET':
                rooms = cursor.execute("SELECT * FROM rooms").fetchall()
                data = [{'roomid': room[0], 'floor': room[1], 'beds': room[2], 'guestnum': room[3], 'price': room[4], 'links': {'room_info': f"/room/{room[0]}"}} for room in rooms]
                return jsonify({'rooms': data}), 200
            elif request.method == 'POST':
                data = request.json
                cursor.execute("INSERT INTO rooms (floor, beds, guestnum, price) VALUES (?, ?, ?, ?)", (data["floor"], data["beds"], data["guestnum"], data["price"]))
                conn.commit()
                return jsonify(success=True, message="Room created"), 201
            elif request.method == 'DELETE':
                data = request.json
                room_id = data.get('roomid')
                cursor.execute("DELETE FROM rooms WHERE roomid = ?", (room_id,))
                conn.commit()
                return jsonify(success=True, message=f"Room {room_id} deleted"), 200
    except Exception as err:
        return jsonify(error=str(err)), 500

@app.route('/room/<int:room_id>', methods=['GET', 'POST'])
def room_info(room_id):
    try:
        with sqlite3.connect('rooms.sqlite3') as conn:
            cursor = conn.cursor()
            if request.method == 'GET':
                room = cursor.execute("SELECT * FROM rooms WHERE roomid = ?", (room_id,)).fetchone()
                if room is None:
                    return jsonify(error='Room not found'), 404
                return jsonify({'floor': room[1], 'beds': room[2], 'guestnum': room[3], 'price': room[4]}), 200
            elif request.method == 'POST':
                room = cursor.execute("SELECT * FROM rooms WHERE roomid = ?", (room_id,)).fetchone()
                if room is None:
                    return jsonify(error='Room not found'), 404
                cursor.execute("INSERT INTO booking SELECT * FROM rooms WHERE roomid = ?", (room_id,))
                cursor.execute("DELETE FROM rooms WHERE roomid = ?", (room_id,))
                conn.commit()
                return jsonify(success=True, message="Booking created"), 201
    except Exception as err:
        return jsonify(error=str(err)), 500

@app.route('/booking', methods=['GET', 'POST', 'DELETE'])
def handle_booking():
    try:
        with sqlite3.connect('rooms.sqlite3') as conn:
            cursor = conn.cursor()
            if request.method == 'GET':
                bookings = cursor.execute("SELECT * FROM booking").fetchall()
                data = [{'roomid': booking[0], 'floor': booking[1], 'beds': booking[2], 'guestnum': booking[3], 'price': booking[4], 'links': {'booking_info': f"/room/{booking[0]}"}} for booking in bookings]
                return jsonify({'bookings': data}), 200
            elif request.method == 'POST':
                data = request.json
                room_id = data.get('room_id')
                room = cursor.execute("SELECT * FROM rooms WHERE roomid = ?", (room_id,)).fetchone()
                if room is None:
                    return jsonify(error='Room not found'), 404
                cursor.execute("INSERT INTO booking SELECT * FROM rooms WHERE roomid = ?", (room_id,))
                cursor.execute("DELETE FROM rooms WHERE roomid = ?", (room_id,))
                conn.commit()
                return jsonify(success=True, message="Booking created"), 201
            elif request.method == 'DELETE':
                data = request.json
                room_id = data.get('roomid')
                cursor.execute("DELETE FROM booking WHERE roomid = ?", (room_id,))
                conn.commit()
                return jsonify(success=True, message=f"Booking {room_id} deleted"), 200
    except Exception as err:
        return jsonify(error=str(err)), 500

if __name__ == "__main__":
    app.run(debug=True)