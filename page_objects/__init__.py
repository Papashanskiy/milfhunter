from selenium.webdriver.common.by import By


class PageObject:
    MODAL = (By.XPATH, '/html/body/div[2]')
    CLOSE_MODAL = (By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]')

    def __init__(self, driver):
        self.driver = driver

    def _bypass_modal_window(self):
        modal = self.driver.find_element(*self.MODAL)
        if modal.text and 'Не упусти новое знакомство!' in modal.text:
            self.driver.find_element(*self.CLOSE_MODAL).click()
