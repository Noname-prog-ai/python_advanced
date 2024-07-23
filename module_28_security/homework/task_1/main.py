from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

def cors(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        response = func(*args, **kwargs)
        response.headers.add('Access-Control-Allow-Origin', 'https://example.com')  # Замените на нужный вам origin
        response.headers.add('Access-Control-Allow-Methods', 'POST, GET')
        response.headers.add('Access-Control-Allow-Headers', 'X-My-Fancy-Header')
        return response
    return wrapped_function

@app.route('/data', methods=['POST', 'GET'])
@cors
def data():
    if request.method == 'POST':
        return jsonify({'message': 'Data received!'}), 200
    else:
        return jsonify({'message': 'This is a GET request!'}), 200

if __name__ == '__main__':
    app.run(debug=True)