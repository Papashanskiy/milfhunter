import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from controllers.controller import LoginController


class MambaLogin(LoginController):
    LOGIN_FIELD = (By.XPATH, '/html/body/div[2]/div[1]/div[4]/div/div/div/main/form/div[1]/div/input')
    PASSWORD_FIELD = (By.XPATH, '/html/body/div[2]/div[1]/div[4]/div/div/div/main/form/div[2]/div/div/input')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.mamba.ru/ru/login')

    def login(self, login, password):
        self.driver.find_element(*self.LOGIN_FIELD).send_keys(login)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password + Keys.RETURN)
        time.sleep(2)
