from faker import Faker
from flask import Flask, jsonify

fake = Faker()
fake.seed_instance(1234)

domains = [fake.domain_name() for i in range(10)]
phones = [fake.phone_number() for i in range(10)]
print(domains)
print(jsonify(domains))

app = Flask(__name__)


@app.route('/')
def index():
    return 'go to the /phones or /domains'


# BEGIN (write your solution here)
@app.get('/phones')
def phones():
    return jsonify(phones)


@app.get('/domains')
def domains():
    return jsonify(domains)