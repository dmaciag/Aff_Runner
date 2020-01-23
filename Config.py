import logging
import os

class FilerReaderConfig:
    OVERRIDE_PATH = 1
    FOLDER_NAME = "JOHNC" if OVERRIDE_PATH else os.getenv('username')
    BASE_PATH_DL = 'C:\\Users\\' + FOLDER_NAME + '\\Downloads\\'
    FILE_EXTENSION = ".csv"

class LogConfig:
    LOG_FILE_NAME = 'RunnerLog'
    LOG_LEVEL = logging.DEBUG

class ApiConfig:
    class Stooq:
        URL_PREFIX = 'https://stooq.pl/q/d/l/?s='
        URL_SUFFIX = '&i=d'