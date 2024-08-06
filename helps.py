import requests
import random
import string

from endpoints import Endpoints


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def register_new_courier_and_return_login_password():
    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(Endpoints.create_courier, data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


logins = register_new_courier_and_return_login_password()
payload_without_login_for_registration = {
    "password": generate_random_string(10),
    "firstName": generate_random_string(10)
}

payload_without_password_for_registration = {
    "login": generate_random_string(10),
    "firstName": generate_random_string(10)
}

payload_empty_for_registration = {}

payload_correct_for_registration = {
    "login": generate_random_string(10),
    "password": generate_random_string(10),
    "firstName": generate_random_string(10)
}

payload_without_password_for_authorization = {
    "login": logins[0],
}

payload_without_login_for_authorization = {
    "password": logins[1]
}

payload_empty_for_authorization = {}

payload_correct_for_authorization ={
    "login": logins[0],
    "password": logins[1],
}

color_black = ["BLACK"]
color_gray = ['GREY']
color_black_and_grey = ['BLACK', 'GREY']
payload_without_color = {
    "firstName": "Имя",
    "lastName": "Фамилия",
    "address": "Москва",
    "metroStation": 4,
    "phone": "89879879898",
    "rentTime": 2,
    "deliveryDate": "2024-06-25",
    "comment": "comment"
}
