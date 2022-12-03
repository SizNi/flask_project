from flask import Flask,redirect
from flask import request
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email
import os

users = [{'Sergei':'pidor@pidor.ru'}, {'dania':'kloun@neadequat.gdn'}, {'Nikolai':'pedik@pedik.ru'}]

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = EmailField('email', validators = [DataRequired(), Email()])
    submit = SubmitField('Send')


def validate(user, email):
    for elem in users:
        name = list(elem.keys())[0]
        mail = elem[name]
        if user == name:
            return 'Имя занято'
        if email == mail:
            return 'Почта занята'
    

@app.route('/user')
def login():
    form = LoginForm()
    user = request.form.get('username')
    email = request.form.get('email')
    if validate(user, email) is not None:
        errors = (validate(user, email), '')
    else:
        errors = ''
    if errors:
        return render_template(
            'users/index7.html',
            form = form,
            errors=errors,
        )
    users.append({user:email})
    return redirect('/user/success')


@app.route('/user/success')
def suc():
    return render_template(
        'users/index7_1.html',
    )
