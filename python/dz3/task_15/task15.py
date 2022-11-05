import json

def mean_age(json_string):
    age = [js['age'] for js in json.loads(json_string)]
    return json.dumps({'mean_age': sum(age) / len(age)})

if __name__ == '__main__':
    print(mean_age(
        """[
    {
        "name": "Петр",
        "surname": "Петров",
        "patronymic": "Васильевич",
        "age": 23,
        "occupation": "ойтишнек"
    },
    {
        "name": "Василий",
        "surname": "Васильев",
        "patronymic": "Петрович",
        "age": 24,
        "occupation": "дворник"
    }
]"""
    ))
