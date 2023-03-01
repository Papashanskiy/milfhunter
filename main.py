import argparse
import json
import os
import logging

from application import run
from utils.notifier import TelegramBot
from utils.senderconfig import SenderConfig

logger = logging.getLogger('hunting_app')
logger.setLevel(logging.INFO)
format_str = "[%(asctime)s - %(levelname)-8s %(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
date_format = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(format_str, date_format)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--browser', required=False,
                        help='name of the browser', default='chrome')
    parser.add_argument('-l', '--login', required=True,
                        help='login for site')
    parser.add_argument('-p', '--password', required=True,
                        help='password for site')
    parser.add_argument('-ph', '--phrases', required=False,
                        help="json with phrases", default=os.path.join(os.getcwd(), 'phrases.json'))
    parser.add_argument('-r', '--result_file', required=False,
                        help="result json file", default=os.path.join(os.getcwd(), 'result.json'))
    parser.add_argument('-a', '--age', required=False,
                        help='age interval', default='27-50')
    parser.add_argument('-i', '--iter_number', required=False,
                        help='number of iterations', default=10, type=int)
    parser.add_argument('-s', '--session_name', required=False,
                        default='default_session_name', help='name of bot session')
    parser.add_argument('-c', '--telegram_chat_id', required=True,
                        help='chat id of telegram group')
    parser.add_argument('-t', '--telegram_token', required=True,
                        help='telegram bot token')
    parser.add_argument('-u', '--url', required=False,
                        help='url to send info about user')
    return parser.parse_args()


def main():
    args = parse_arguments()
    login = args.login
    password = args.password
    age_interval_start, age_interval_end = args.age.split('-')
    result_file = args.result_file
    iter_number = args.iter_number
    with open(args.phrases, encoding='utf-8') as phrases_file:
        phrases = json.load(phrases_file)
    tg_bot = TelegramBot()
    tg_bot.set_token(args.telegram_token)
    tg_bot.set_chat_id(args.telegram_chat_id)
    tg_bot.set_session_name(args.session_name)
    sender = SenderConfig()
    sender.set_url(args.url)

    logger.info('Initiate application')
    run(login, password, phrases, result_file, iter_number, age_interval_start, age_interval_end, args.browser)


if __name__ == '__main__':
    main()
