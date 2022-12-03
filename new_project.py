from flask import Flask
from flask import request
from flask import render_template
# поиск по именам
app = Flask(__name__)
users = ['mike', 'mishel', 'adel', 'keks', 'kamila']


@app.route('/courses/')
def courses():
    filtered_courses = []
    term = request.args.get('term')
    for elem in users:
        if term in elem:
            filtered_courses.append(elem)
    return render_template(
        'users/index.html',
        search = term,
        courses=filtered_courses
    )