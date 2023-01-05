import logging
import random

from selenium.common import ElementClickInterceptedException, NoSuchElementException

from page_objects.love_planet.chats import LovePlanetChats
from page_objects.love_planet.filter import LovePlanetFilter
from page_objects.love_planet.meet import LovePlanetMeet
from page_objects.love_planet.messages import LovePlanetMessages

logger = logging.getLogger('hunting_app')


def hunting(driver, welcome_phrases, iter_number=30):
    for i in range(iter_number):
        try:
            LovePlanetMeet(driver).matching(random.choice(welcome_phrases))
        except (NoSuchElementException, ElementClickInterceptedException):
            pass


def chatting(driver, phrases, result_file):
    chats = LovePlanetChats(driver).get_chats()
    while chats:
        try:
            LovePlanetMessages(driver).chatting(chats.pop(), phrases, result_file)
        except ElementClickInterceptedException:
            pass
        chats = LovePlanetChats(driver).get_chats()


def prepare_phrases_for_processing(phrases):
    return {x['sequence']: x['phrases'] for x in phrases.values()}


def main_loop(driver, phrases, result_file, iter_number, age_interval_start, age_interval_end):
    LovePlanetFilter(driver).set(age_interval_start, age_interval_end)
    logger.info(f'Filter set on age_interval_start={age_interval_start} age_interval_end={age_interval_end}')

    while True:
        phrases_for_processing = prepare_phrases_for_processing(phrases)
        chatting(driver, phrases_for_processing, result_file)
        hunting(driver, phrases.get('welcome')['phrases'], iter_number)
