import logging
import os
from collections import namedtuple
import argparse

my_format = '{msg}'
logging.basicConfig(filename='info.txt', filemode='a', encoding='utf-8', level=logging.INFO, style='{', format=my_format)
logger = logging.getLogger(__name__)

D_Class = namedtuple('D_Class', ['name', 'is_directory', 'parent_directory'])
F_Class = namedtuple('F_Class', ['name', 'extension', 'is_directory', 'parent_directory'])


def get_info_about_dirs_and_files(path: str):
    for root, dirs, files in os.walk(path):
        for dir_ in dirs:
            dir_path = os.path.join(root, dir_)
            dir_obj = D_Class(dir_, str(os.path.isdir(dir_path)), os.path.basename(os.path.dirname(dir_path)))
            logger.info(msg=f'{dir_obj}')

        for file in files:
            file_path = os.path.join(root, file)
            file_obj = F_Class(os.path.splitext(file)[0], os.path.splitext(file)[1],
                               str(os.path.isfile(file_path)), os.path.basename(os.path.dirname(file_path)))
            logger.info(msg=f'{file_obj}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Information about directories and files')
    parser.add_argument('-path', metavar='path', type=str, help='enter path for get_info_about_dirs_and_files()',
                        default=os.getcwd())
    args = parser.parse_args()
    get_info_about_dirs_and_files(args.path)