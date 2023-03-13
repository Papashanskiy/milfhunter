import json
from json import JSONDecodeError


def save(file_name, username, phones, full_name=None, age=None, description=None, photo_url=None):
    content = {}
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = json.load(file)
    except (JSONDecodeError, FileNotFoundError):
        pass

    if username in content.keys():
        return False

    content.update(
        {
            username: {
                'phones': phones,
                'full_name': full_name,
                'age': age,
                'description': description,
                'photo_url': photo_url
            }
        }
    )

    with open(file_name, 'wt', encoding='utf-8') as result_file:
        json.dump(content, result_file)

    return True
