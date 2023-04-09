from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager


class BrowserOptions:
    headless = False

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(BrowserOptions, cls).__new__(cls)
        return cls.instance
        

class Browser(object):

    def __init__(self):
        self.driver = None

    def get_browser(self, browser_name):

        if browser_name == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser_name == "chrome":
            chrome_options = None
            if BrowserOptions.headless:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
                chrome_options.add_argument('--no-sandbox')
            
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        elif browser_name == "ie":
            self.driver = webdriver.Ie(IEDriverManager().install())
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        return self.driver
