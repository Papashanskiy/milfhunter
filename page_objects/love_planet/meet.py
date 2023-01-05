import logging
import time

from selenium.webdriver.common.by import By

logger = logging.getLogger('hunting_app')


class LovePlanetMeet:
    OUR_MESSAGES = (By.CLASS_NAME, 'outbox')
    ALL_MESSAGES = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div/ul')
    LI = (By.TAG_NAME, 'li')
    CHAT = (By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/div[2]/div[1]/div[1]/span[2]')
    TEXT_INPUT = (By.XPATH, '/html/body/div[4]/div[2]/div[3]/div[1]/textarea')
    SUBMIT = (By.XPATH, '/html/body/div[4]/div[2]/div[3]/div[1]/button')
    BACK = (By.XPATH, '/html/body/div[4]/div[2]/div[1]/div/div/div[1]')
    LIKE = (By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/div[2]/div[1]/div[1]/span[3]')

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://m.loveplanet.ru/index/meet')

    def matching(self, welcome_phrase):
        self.driver.find_element(*self.CHAT).click()

        self.driver.find_element(*self.TEXT_INPUT).send_keys(welcome_phrase)
        time.sleep(2)

        username = self.driver.current_url.split('/').pop()
        logger.info(f'Hunting user with username {username}')

        messages = self.driver.find_element(*self.ALL_MESSAGES)
        if messages.text:
            logger.info('We already send message to this user. Skip him')
            self.driver.find_element(*self.BACK).click()
            self.driver.find_element(*self.LIKE).click()
            time.sleep(2)
            return

        self.driver.find_element(*self.SUBMIT).click()
        self.driver.find_element(*self.BACK).click()
        self.driver.find_element(*self.LIKE).click()
        time.sleep(2)
