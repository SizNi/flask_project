from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/users/<id>')
def courses(id):
    return render_template(
        'users/show.html',
       id = f'{id}',
       name = f'user-{id}'
    )

# 
users = 123
@app.route('/users/<int:id>')
def get_user(id):
    filtered_users = filter(lambda user: user['id'] == id, users)
    user = next(filtered_users, None)

    if user is None:
        return 'Page not found', 404

    return render_template('users/show.html', user=user)


@app.route('/users')
def get_users():
    return render_template('users/index.html', users=users)
#