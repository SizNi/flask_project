users = [{'Sergei':'pidor@pidor.ru'}, {'dania':'kloun@neadequat.gdn'}, {'Nikolai':'pedik@pedik.ru'}]


def validate(users):
    for elem in users:
        name = list(elem.keys())[0]
        print(type(name))


validate(users)