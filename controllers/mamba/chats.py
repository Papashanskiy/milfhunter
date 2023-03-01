import time

from selenium.webdriver.common.by import By

from controllers.controller import ChatsController


class MambaChats(ChatsController):
    CHATS_MENU = (By.XPATH, '/html/body/div[2]/div[1]/div[4]/div/div[1]/div/header/div/span')
    SHARED_FOLDER = (By.XPATH, '//label[@data-name="contacts-folder-Income-action"]')
    LI = (By.TAG_NAME, 'li')
    CHATS_CONTAINER = (By.XPATH, '/html/body/div[2]/div[1]/div[4]/div/div[1]/div/div/section/div/div[1]/div')

    def __init__(self, driver):
        super().__init__(driver)
        self._visit_rating()

    def _visit_rating(self):
        self.driver.get('https://www.mamba.ru/rating')
        time.sleep(2)

    def _select_all_chats(self):
        self.driver.find_element(*self.CHATS_MENU).click()
        time.sleep(2)
        self.driver.find_element(*self.SHARED_FOLDER).click()
        time.sleep(2)

    def get_chats(self):
        self._select_all_chats()

        chats_container = self.driver.find_element(*self.CHATS_CONTAINER)

        chats_container = self.driver.find_element(*self.CHATS)
        if not chats_container.text:
            return []
        chats = chats_container.find_elements("tag name", 'li')
        return chats
