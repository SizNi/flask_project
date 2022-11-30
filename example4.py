from flask import Flask

# Это уже нам знакомое callable WSGI-приложение
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Flask!'


@app.get('/users')
def users_get():
    return 'GET /users'


@app.post('/users')
def users_post():
    return 'POST /users'


@app.post('/users')
def users():
    return 'Users', 302