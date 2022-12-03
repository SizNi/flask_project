import uuid
from flask import session


class Repository:
    def content(self):
        return session.values()

    def find(self, id):
        try:
            return session[id]
        except KeyError as e:
            raise e(f'Wrong item id: {id}')

    def save(self, item):
        item['id'] = str(uuid.uuid4())
        session[item['id']] = item
