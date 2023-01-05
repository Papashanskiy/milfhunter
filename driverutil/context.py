from contextlib import contextmanager

from driverutil.browser import Browser


@contextmanager
def get_driver(browser):
    driver = Browser().get_browser(browser)
    try:
        yield driver
    finally:
        driver.quit()
