import logging

from driverutil.context import get_driver
from page_objects.love_planet.login import LovePlanetLogin
from utils.loop import main_loop

logger = logging.getLogger('hunting_app')


def run(login, password, phrases, result_file, iter_number, age_interval_start, age_interval_end, browser='chrome'):
    with get_driver(browser) as driver:
        LovePlanetLogin(driver).login(login, password)
        logger.info('Success auth')
        main_loop(driver, phrases, result_file, iter_number, age_interval_start, age_interval_end)
