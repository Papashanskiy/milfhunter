import logging
import random

from utils.driverutil.context import get_driver
from utils.phrases import prepare_phrases_for_processing

logger = logging.getLogger('milfhunter')


class MainLoop:

    def __init__(self, controller):
        self.controller = controller

    def _chatting(self, driver, phrases, result_file):
        chats = self.controller.chats(driver).get_chats()
        while chats:
            chats.pop().click()
            self.controller.messages(driver).chatting(phrases, result_file)
            chats = self.controller.chats(driver).get_chats()

    def _hunting(self, driver, welcome_phrases, iter_number=30):
        for i in range(iter_number):
            self.controller.meet(driver).matching(random.choice(welcome_phrases))

    def _run_main_loop(self, driver, phrases, result_file, iter_number, age_interval_start, age_interval_end):
        self.controller.filter(driver).set(age_interval_start, age_interval_end)
        logger.info(f'Filter set on age_interval_start={age_interval_start} age_interval_end={age_interval_end}')

        while True:
            try:
                phrases_for_processing = prepare_phrases_for_processing(phrases)
                self._chatting(driver, phrases_for_processing, result_file)
                self._hunting(driver, phrases.get('welcome')['phrases'], iter_number)
            except Exception as e:
                logger.exception(f'Unexpected exception: {e}')

    def run(self, username, password, phrases, result_file, iter_number,
            age_interval_start, age_interval_end, browser='chrome'):
        with get_driver(browser) as driver:
            self.controller.login(driver).login(username, password)
            logger.info('Success auth')
            self._run_main_loop(driver, phrases, result_file, iter_number, age_interval_start, age_interval_end)
