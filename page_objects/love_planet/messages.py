import logging
import random
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from page_objects import PageObject
from utils.user_data import create_user_data
from utils.notifier import TelegramBot, send_in_tg_chat
from utils.phones import get_phone
from utils.saver import save
from utils.outer_sender import send_info_into_1c

logger = logging.getLogger('hunting_app')


class LovePlanetMessages(PageObject):
    ALL_MESSAGES = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[1]/ul')
    OUR_MESSAGES = (By.CLASS_NAME, 'outbox')
    THEIR_MESSAGES = (By.CLASS_NAME, 'inbox')
    MESSAGES = (By.XPATH, '/html/body/div[4]/div/div[2]/div/ul')
    TEXT_INPUT = (By.XPATH, '/html/body/div[4]/div[2]/div[3]/div[2]/textarea')
    SUBMIT = (By.XPATH, '/html/body/div[4]/div[2]/div[3]/div[2]/button')
    BACK = (By.XPATH, '/html/body/div[4]/div/div[1]/div/div[1]')
    MODAL = (By.XPATH, '/html/body/div[2]')
    PHOTO = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/img')
    FULL_NAME = (By.XPATH, '/html/body/div[4]/div[2]/div[1]/div/div[3]/div[2]/span/span')
    AGE = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/span[1]/span[2]')
    DESCRIPTION = (By.CLASS_NAME, 'profile-container')

    def _is_user_exist(self):
        try:
            self.driver.find_element(*self.TEXT_INPUT)
            return True
        except NoSuchElementException:
            self.driver.find_element(*self.BACK).click()
            time.sleep(2)
            return False

    def get_profile_info(self, username):
        start_point_url = self.driver.current_url

        full_name = None
        try:
            full_name = self.driver.find_element(*self.FULL_NAME).text
        except Exception:
            pass

        self.driver.get(f'https://m.loveplanet.ru/index/page/{username}')
        time.sleep(3)

        age = None
        try:
            age = self.driver.find_element(*self.AGE).text
        except Exception:
            pass

        description = None
        try:
            description = self.driver.find_element(*self.DESCRIPTION).text
        except Exception:
            pass

        photo_url = None
        try:
            photo_url = self.driver.find_element(*self.PHOTO).get_attribute("src")
        except Exception:
            pass
        self.driver.get(start_point_url)
        return full_name, age, description, photo_url

    def save_phones(self, result_file, username):
        their_messages = self.driver.find_elements(*self.THEIR_MESSAGES)
        if not their_messages:
            return

        text_of_messages = ' '.join([x.text for x in their_messages])
        phones = get_phone(text_of_messages)
        if phones:
            logger.info(f'Found phones {phones}. Save it in file {result_file}')
            full_name, age, description, photo_url = self.get_profile_info(username)

            user_data = create_user_data(username, full_name, age, phones, photo_url, 
                                         description, TelegramBot().session_name)

            if save(result_file, user_data):
                send_in_tg_chat(username, full_name, phones, photo_url)
                send_info_into_1c(user_data)

    def get_all_messages(self):
        return [x.get_attribute('class') for x in self.driver.find_element(
            *self.ALL_MESSAGES).find_elements(By.TAG_NAME, 'li')]

    def send_message(self, message):
        self.driver.find_element(*self.TEXT_INPUT).send_keys(message)
        time.sleep(2)
        self.driver.find_element(*self.SUBMIT).click()
        time.sleep(2)

    def chatting(self, phrases, result_file):
        username = self.driver.current_url.split('/').pop()
        logger.info(f'Chatting with user {username}')

        if not self._is_user_exist():
            logger.info(f'User {username} doesn`t exist. Skip this user')
            return

        all_messages = self.get_all_messages()
        their_messages_count = all_messages.count('inbox')
        our_messages_count = all_messages.count('outbox')

        if their_messages_count > 0:
            self.save_phones(result_file, username)

        if our_messages_count > 3:
            logger.info('We send 4 messages. Skip this user')
            return

        if our_messages_count == 0 and their_messages_count > 0:
            self.send_message('Привет')
            return

        phrase = random.choice(phrases.get(our_messages_count))
        self.send_message(phrase)

        modal = self.driver.find_element(*self.MODAL)
        if modal.text:
            logger.warning('There are captcha! Enter it and submit!')
            time.sleep(45)

        self._bypass_modal_window()
