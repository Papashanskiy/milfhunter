from controllers import LoginController


class MambaLogin(LoginController):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.mamba.ru/ru/login')
