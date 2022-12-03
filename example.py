from flask import Flask
from flask import request
from flask import render_template


def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])



app = Flask(__name__)
users = ['mike', 'mishel', 'adel', 'keks', 'kamila']

def index():
    return 'Hello, World!'

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        return 'Hello from POST /users'
    else:
        return 'Hello from GET /users'


@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'