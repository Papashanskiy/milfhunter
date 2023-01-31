import logging
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common import ElementClickInterceptedException, NoSuchElementException

from controllers.controller import MeetController

logger = logging.getLogger('milfhunter')


class MambaMeet(MeetController):
    OUR_MESSAGES = (By.CLASS_NAME, 'outbox')
    ALL_MESSAGES = (By.XPATH, '/html/body/div[2]/div[1]/div[4]/div/div[2]/div/div/div[2]/div[1]/li/ul')
    LI = (By.TAG_NAME, 'li')
    CHAT = (By.XPATH, '/html/body/div[2]/div[1]/div[4]/div/div[2]/div/div/section'
                      '/div/div[1]/div[7]/div[2]/div[1]/div[4]/div/button[4]')
    TEXT_INPUT = (By.XPATH, '/html/body/div[2]/div[1]/div[4]/div/div[2]/div/'
                            'div/div[3]/div[2]/div/div[2]/div[1]/textarea')
    SUBMIT = (By.XPATH, '/html/body/div[4]/div[2]/div[3]/div[1]/button')
    BACK = (By.XPATH, '/html/body/div[4]/div[2]/div[1]/div/div[1]')
    LIKE = (By.XPATH, '/html/body/div[2]/div[1]/div[4]/div/div[2]/div/div/section'
                      '/div/div[1]/div[7]/div[2]/div[1]/div[4]/div/button[3]')
    MESSAGES_BODY = (By.XPATH, '/html/body/div[2]/div[1]/div[4]/div/div[2]')

    CLEAN_CHAT_TEXT = 'Начать знакомство — это просто! Нужно всего лишь написать "Привет!".'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.mamba.ru/rating')

    def matching(self, welcome_phrase):
        try:
            self.driver.find_element(*self.CHAT).click()
            time.sleep(2)

            username = self.driver.current_url.split('/')[-2]
            logger.info(f'Hunting user with username {username}')

            # ######### We need to finish this part ######### #
            messages_body = self.driver.find_element(*self.MESSAGES_BODY).text
            if self.CLEAN_CHAT_TEXT in messages_body:
                self.driver.find_element(*self.TEXT_INPUT).send_keys(welcome_phrase + Keys.RETURN)
                time.sleep(2)
                self.driver.back()
                time.sleep(2)

                self.driver.find_element(*self.LIKE).click()
                time.sleep(2)


            messages = self.driver.find_element(*self.ALL_MESSAGES)
            if messages.text:
                logger.info('We already send message to this user. Skip him')
                self.driver.find_element(*self.BACK).click()
                self.driver.find_element(*self.LIKE).click()
                time.sleep(2)
                return
            # ############################################### #


        except (NoSuchElementException, ElementClickInterceptedException):
            pass
