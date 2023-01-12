import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class LovePlanetFilter:
    LUPA = (By.XPATH, '/html/body/div[4]/div/div[1]/div/div[2]')
    AGE_START = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div/form/ul/li[2]/div/select[1]')
    AGE_END = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div/form/ul/li[2]/div/select[2]')
    NEW_PEOPLE = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div/form/ul/li[6]/div/div[1]/label')
    SUBMIT = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div/form/ul/li[7]/div/div')

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://m.loveplanet.ru/index/meet')

    def set(self, age_interval_start, age_interval_end):
        self.driver.find_element(*self.LUPA).click()
        options = Select(self.driver.find_element(*self.AGE_START))
        [x for x in options.options if age_interval_start in x.text][0].click()
        options = Select(self.driver.find_element(*self.AGE_END))
        [x for x in options.options if age_interval_end in x.text][0].click()
        new_people = self.driver.find_element(*self.NEW_PEOPLE)
        if not new_people.is_selected():
            new_people.click()
        self.driver.find_element(*self.SUBMIT).click()
        time.sleep(2)
