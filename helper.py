from data import URL
import random
import string
import requests


def create_random_user():
    name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 8)))
    email = f"{name}@mail.ru"
    password = ''.join(random.choices(
        string.ascii_letters + string.digits + "!@#$%^&*()",
        k=random.randint(6, 10)
    ))
    return {
        "email": email,
        "password": password,
        "name": name,
    }

def get_users_info():
    payload = create_random_user()
    response = requests.post(f'{URL.CREATE_URL}', json=payload)
    return payload, response
