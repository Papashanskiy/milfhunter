import argparse
import json
import os
import logging

from application import run


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
    return parser.parse_args()


def main():
    args = parse_arguments()
    login = args.login
    password = args.password
    age_interval_start, age_interval_end = args.age.split('-')
    result_file = args.result_file
    iter_number = args.iter_number
    with open(args.phrases) as phrases_file:
        phrases = json.load(phrases_file)

    logger.info('Initiate application')
    run(login, password, phrases, result_file, iter_number, age_interval_start, age_interval_end, args.browser)


if __name__ == '__main__':
    main()
