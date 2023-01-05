import json
from json import JSONDecodeError


def save_in_file(file_name, username, phones):
    content = {}
    try:
        with open(file_name, 'r') as file:
            content = json.load(file)
    except (JSONDecodeError, FileNotFoundError):
        pass

    if username in content.keys():
        return

    content.update({username: {'phones': phones}})

    with open(file_name, 'wt') as result_file:
        json.dump(content, result_file)
