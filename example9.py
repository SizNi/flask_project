from flask import Flask,redirect
from flask import request
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email
import os


app = Flask(__name__)

@app.route('/schools/new')
def new_school():
    school = []
    errors = []
    return render_template(
            'index9.html',
            school=school,
            errors=errors,
            )


@app.post('/schools')
def post_school():
    repo = SchoolRepository()

    # Извлекаем данные формы
    data = request.form.to_dict()

    # Проверяем корректность данных
    errors = validate(data)
    if errors:
        # Если возникли ошибки, то устанавливаем код ответа в 422 и рендерим форму с указанием ошибок
        return render_template(
            'schools/new.html',
            school=data,
            errors=errors
            ), 422

    # Если данные корректны, то сохраняем, добавляем флеш и выполняем редирект
    repo.save(data)
    flash('School has been created', 'success')
    # Обратите внимание на использование именованного роутинга
    return redirect(url_for('schools'))