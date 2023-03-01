import time

from selenium.webdriver.common.by import By

from controllers.controller import ChatsController


class LovePlanetChats(ChatsController):
    CHATS = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/ul')
    LI = (By.TAG_NAME, 'li')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://m.loveplanet.ru/index/mess/new')

    def get_chats(self):
        time.sleep(2)
        chats_container = self.driver.find_element(*self.CHATS)
        if not chats_container.text:
            return []
        chats = chats_container.find_elements("tag name", 'li')
        return chats
