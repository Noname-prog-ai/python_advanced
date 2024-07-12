import json
from urllib.parse import parse_qs


class App:
    def __init__(self, routes):
        self.routes = routes

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '').lstrip('/')

        if path.startswith('static/'):
            static_file_path = path.replace('static/', 'Static/')  # путь к статическому файлу
            try:
                with open(static_file_path, 'rb') as f:
                    status = '200 OK'
                    headers = [('Content-type', 'image/jpeg')]
                    start_response(status, headers)
                    return [f.read()]
            except FileNotFoundError:
                status = '404 Not Found'
                headers = [('Content-type', 'application/json')]
                start_response(status, headers)
                return [json.dumps({'message': 'File not found'}).encode()]

        method = environ.get('REQUEST_METHOD', '')

        for route, handler in self.routes:
            if route == path:
                status = '200 OK'
                headers = [('Content-type', 'application/json')]
                start_response(status, headers)
                return [handler()]

        status = '404 Not Found'
        headers = [('Content-type', 'application/json')]
        start_response(status, headers)
        return [json.dumps({'message': 'Page not found'}).encode()]


def route(path):
    def decorator(handler):
        def wrapper(*args, **kwargs):
            return handler(*args, **kwargs)

        return path, wrapper

    return decorator


@app.route("/hello")
def say_hello():
    return json.dumps({"response": "Hello, world!"}, indent=4).encode()


@app.route("/hello/<name>")
def say_hello_with_name(name):
    return json.dumps({"response": f"Hello, {name}!"}, indent=4).encode()


app = App([route("/hello"), route("/hello/<name>")])