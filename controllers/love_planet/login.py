import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from controllers import LoginController


class LovePlanetLogin(LoginController):
    HAVE_LOVE_PLANET_ACCOUNT = (By.XPATH, '/html/body/div/div/amp-script/div[2]/a[3]')
    LOGIN_FIELD = (By.XPATH, '/html/body/div[2]/div/div/div[2]/form/ul/li[1]/input')
    PASSWORD_FIELD = (By.XPATH, '/html/body/div[2]/div/div/div[2]/form/ul/li[2]/input')
    AUTH_FIELD = (By.XPATH, '/html/body/div[2]/div/div/div[2]/form/ul')
    MODAL = (By.XPATH, '/html/body/div[2]')
    CLOSE_MODAL = (By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://m.loveplanet.ru/')

    def _is_captcha(self):
        if 'Enter the code from the picture' in self.driver.find_element(*self.AUTH_FIELD).text:
            return True
        return False

    def _bypass_modal_window(self):
        modal = self.driver.find_element(*self.MODAL)
        if modal.text and 'Не упусти новое знакомство!' in modal.text:
            self.driver.find_element(*self.CLOSE_MODAL).click()

    def login(self, login, password):
        self.driver.find_element(*self.HAVE_LOVE_PLANET_ACCOUNT).click()
        self.driver.find_element(*self.LOGIN_FIELD).send_keys(login)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

        if self._is_captcha():
            time.sleep(45)
        self._bypass_modal_window()
        try:
            self._is_captcha()
        except NoSuchElementException:
            return

        self.driver.find_element(*self.LOGIN_FIELD).send_keys(Keys.RETURN)
        time.sleep(2)
