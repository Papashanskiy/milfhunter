import json
from json import JSONDecodeError


def save(file_name, username, user_data=None):
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
                'send_to_1C_json': user_data
            }
        }
    )

    with open(file_name, 'wt', encoding='utf-8') as result_file:
        json.dump(content, result_file)

    return True
