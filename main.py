import argparse
import json
import os
import logging

from controllers import available_controllers
from utils.loop import MainLoop
from utils.notifier import TelegramBot

logger = logging.getLogger('milfhunter')
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
    parser.add_argument('--site', required=True,
                        help='site from list: (mamba.ru, loveplanet.ru)')
    return parser.parse_args()


def main():
    args = parse_arguments()
    age_interval_start, age_interval_end = args.age.split('-')
    with open(args.phrases, encoding='utf-8') as phrases_file:
        phrases = json.load(phrases_file)

    tg_bot = TelegramBot()
    tg_bot.set_token(args.telegram_token)
    tg_bot.set_chat_id(args.telegram_chat_id)
    tg_bot.set_session_name(args.session_name)

    controller = available_controllers.get(args.site)
    if not controller:
        raise RuntimeError(f'Entered site {args.site} does not support by this application.'
                           f'Available sites: {available_controllers.keys()}')

    logger.info('Initiate application')
    MainLoop(controller).run(args.login, args.password, phrases, args.result_file, args.iter_number,
                             age_interval_start, age_interval_end, args.browser)


if __name__ == '__main__':
    main()
