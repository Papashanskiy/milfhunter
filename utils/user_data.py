import base64
import requests


def create_user_data(username, full_name, age, phones, photo_url, description, session_id):
    return {
        'username': username,
        'full_name': full_name,
        'age': age,
        'phones': phones,
        'photo_url': photo_url,
        'photo_base64': base64.b64encode(requests.get(photo_url).content).decode('utf-8'),
        'description': description,
        'session_id': session_id
    }
