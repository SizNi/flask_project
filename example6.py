from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.post('/users')
def users_post():
    repo = UserRepository()
    user = request.form.to_dict()
    errors = validate(user)
    if errors:
        return render_template(
          'users/new.html',
          user=user,
          errors=errors,
        )
    repo.save(user)
    return redirect('/users', code=302)


@app.route('/users/new')
def users_new():
    user = {'name': '',
            'email': '',
            'password': '',
            'passwordConfirmation': '',
            'city': ''}
    errors = {}

    return render_template(
        'new.html',
        user=user,
        errors=errors
    )