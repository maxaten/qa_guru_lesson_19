import logging
import requests


def test_page_number():
    page = 2

    response = requests.get('https://reqres.in/api/users', params={'page': page})

    assert response.status_code == 200
    assert response.json()['page'] == 2


def test_users_list_def_length():
    default_users_count = 6

    response = requests.get('https://reqres.in/api/users')

    logging.info(response.json())
    assert response.status_code == 200
    assert len(response.json()['data']) == default_users_count


def test_user_not_found_404():
    response = requests.get('https://reqres.in/api/users/23')

    assert response.status_code == 404
    assert response.text == '{}'


def test_create_user_201():
    name = 'Olga'
    job = 'Manager'

    response = requests.post(

        url='https://reqres.in/api/users',
        json={
            'name': name,
            'job': job
        })

    logging.info(response.json())
    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job

def test_delete_users():
    response = requests.delete(url='https://reqres.in/api/users/2')

    logging.info(response.text)
    assert response.status_code == 204
    assert response.text == ''


def test_update_user_200():
    name = 'Ololosha'
    job = 'President'
    response = requests.put(
        url='https://reqres.in/api/users/2',
        json={
            "name": name,
            "job": job
        }
    )

    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job


def test_login_user_200():
    email = 'eve.holt@reqres.in'
    password = 'cityslicka'

    response = requests.post(
        url='https://reqres.in/api/login',
        json={
            "email": email,
            "password": password
        }
    )

    logging.info(response.json())
    assert response.status_code == 200


def test_user_login_unsuccessful():
    email = 'peter@klaven'
    text_error = 'Missing password'

    response = requests.post(
        url='https://reqres.in/api/login',
        json={
            'email': email
        }
    )

    logging.info(response.json())
    assert response.status_code == 400
    assert response.json()['error'] == text_error


def test_register_user_200():
    email = 'eve.holt@reqres.in'
    password = 'pistol'

    response = requests.post(
        url='https://reqres.in/api/register',
        json={
            "email": email,
            "password": password
        }
    )

    logging.info(response.json())
    assert response.status_code == 200


def test_unregister_user_200():
    email = 'sydney@fife'

    response = requests.post(
        url='https://reqres.in/api/register',
        json={
            "email": email
        }
    )

    logging.info(response.json())
    assert response.status_code == 400