import logging
from Config import LogConfig
from Utility import DataUtility


logging.basicConfig(level=LogConfig.LOG_LEVEL, filename=LogConfig.LOG_FILE_NAME)

class Runner:
    @classmethod
    def start_runner(self):
        logging.info('Starting runner')

        logging.info('Stopping runner')

rics = [
    "NVDA.US",
    "XAUUSD",
    "AMD.US",
    "XAGUSD",
    "NG.F",
    "CL.F",
    "AA.US",
    "HD.US",
    "MCD.US"
]

portfolioRunner = Runner()

nvda_points = DataUtility.retrieve_points("NVDA.US")
thirty_yr_interest_rates = DataUtility.retrieve_points("30yr.dl")

portfolioRunner.start_runner()






