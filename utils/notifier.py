import logging
import requests

logger = logging.getLogger('hunting_app')


DEFAULT_PHOTO_URL = 'https://cdn-icons-png.flaticon.com/512/456/456212.png'


class TelegramBot:
    chat_id = None
    token = None
    session_name = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TelegramBot, cls).__new__(cls)
        return cls.instance

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def set_token(self, token):
        self.token = token

    def set_session_name(self, session_name):
        self.session_name = session_name


def send_photo(text, photo_url):
    telegram_bot = TelegramBot()
    message_data = dict(chat_id=telegram_bot.chat_id, caption=text, photo=photo_url)
    try:
        response = requests.get(f"https://api.telegram.org/bot{telegram_bot.token}/sendPhoto", params=message_data)
        response.raise_for_status()
        return True
    except requests.exceptions.HTTPError as e:
        logger.error(f'Telegram send error: {e}')
        return False


def send_in_tg_chat(username, full_name, phones, photo_url):
    telegram_bot = TelegramBot()
    text = f'Название сессии: #{telegram_bot.session_name} \n\n' \
           f'Имя: {full_name}\n\n' \
           f'💌Адрес анкеты: https://loveplanet.ru/page/{username}\n\n' \
           f'📱Номер телефона: {", ".join(phones)}'
    if not send_photo(text, photo_url):
        send_photo(text, DEFAULT_PHOTO_URL)
