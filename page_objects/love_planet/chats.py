from selenium.webdriver.common.by import By


class LovePlanetChats:
    CHATS = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/ul')
    LI = (By.TAG_NAME, 'li')

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://m.loveplanet.ru/index/mess/new')

    def get_chats(self):
        chats = self.driver.find_element(*self.CHATS).find_elements("tag name", 'li')
        return chats
