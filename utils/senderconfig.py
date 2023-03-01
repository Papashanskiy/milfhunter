import logging

import requests

logger = logging.getLogger('hunting_app')


class SenderConfig:
    url = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SenderConfig, cls).__new__(cls)
        return cls.instance

    def set_url(self, url):
        self.url = url


def prepare_user_data(username, full_name, age, phones, photo_url, description):
    return dict(
        username=username,
        full_name=full_name,
        age=age,
        phones=phones,
        photo_url=photo_url,
        description=description
    )


def send_info_into_1c(username, full_name, age, phones, photo_url, description):
    sender = SenderConfig()

    if not sender.url:
        logger.error('Url to send user info 1C system has not been entered')

    user_data = prepare_user_data(username, full_name, age, phones, photo_url, description)
    response = requests.post(sender.url, json=user_data)
    logger.info(f'Request to url {sender.url} has response: {response.json()}')
