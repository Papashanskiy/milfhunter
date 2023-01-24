import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from controllers.controller import FilterController


class MambaFilter(FilterController):
    AGE = (By.XPATH, '/html/body/div[2]/div[3]/div/div/div/form/main/a[3]')
    AGE_START = (By.XPATH, '/html/body/div[2]/div[3]/div/div/form/div/main/div/div/label[1]/div[2]/label/select')
    AGE_END = (By.XPATH, '/html/body/div[2]/div[3]/div/div/form/div/main/div/div/label[2]/div[2]/label/select')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.mamba.ru/rating/rating-settings')

    def set(self, age_interval_start, age_interval_end):
        self.driver.find_element(*self.AGE).click()
        options = Select(self.driver.find_element(*self.AGE_START))
        [x for x in options.options if age_interval_start in x.text][0].click()
        options = Select(self.driver.find_element(*self.AGE_END))
        [x for x in options.options if age_interval_end in x.text][0].click()
        time.sleep(2)
