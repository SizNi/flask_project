from flask import Flask
from flask import request

app = Flask(__name__)


def index():
    return 'Hello, World!'

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        return 'Hello from POST /users'
    else:
        return 'Hello from GET /users'