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


def send_info_into_1c(user_data):
    sender = SenderConfig()

    if not sender.url:
        logger.error('Url to send user info 1C system has not been entered')
        return

    session = requests.Session()
    session.auth = ('exchange', 'APK13gym')
    response = session.post(sender.url, json=user_data)
    logger.info(f'Request to url {sender.url} has response: {response.json()}')
