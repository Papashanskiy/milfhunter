import logging
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common import ElementClickInterceptedException, NoSuchElementException

from controllers.controller import MeetController

logger = logging.getLogger('milfhunter')


class MambaMeet(MeetController):
    LI = (By.TAG_NAME, 'li')
    TEXT_INPUT = (By.XPATH, '/html/body/div[2]/div[1]/div[4]/div/div[2]/div/'
                            'div/div[3]/div[2]/div/div[2]/div[1]/textarea')
    LIKE = (By.XPATH, '/html/body/div[2]/div[1]/div[4]/div/div[2]/div/div/section'
                      '/div/div[1]/div[7]/div[2]/div[1]/div[4]/div/button[3]')

    MESSAGES_BODY = (By.XPATH, '/html/body/div[2]/div[1]/div[4]/div/div[2]/div/div/div[2]')
    COMPLEMENT = (By.XPATH, '//div[@data-name="modal-gifts-payment"]')
    HTML = (By.XPATH, '/html')

    def __init__(self, driver):
        super().__init__(driver)
        self._visit_rating()

    def _visit_rating(self):
        self.driver.get('https://www.mamba.ru/rating')
        time.sleep(2)

    def _like(self):
        self._visit_rating()
        time.sleep(2)
        self.driver.find_element(*self.HTML).send_keys(Keys.RIGHT)
        time.sleep(2)

    def _start_chatting(self):
        self.driver.find_element(*self.HTML).send_keys(Keys.RETURN)
        time.sleep(2)

    def matching(self, welcome_phrase):
        try:
            self._start_chatting()

            username = self.driver.current_url.split('/')[-2]
            logger.info(f'Hunting user with username {username}')

            messages_body = self.driver.find_element(*self.MESSAGES_BODY)

            if 'li' in [x.tag_name for x in messages_body.find_elements(By.CSS_SELECTOR, '*')]:
                logger.info('We already send message to this user. Skip him')
                self._like()

            self.driver.find_element(*self.TEXT_INPUT).send_keys(welcome_phrase + Keys.RETURN)
            time.sleep(2)
            self._like()
        except (NoSuchElementException, ElementClickInterceptedException):
            pass
