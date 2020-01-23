import logging
import requests
from Config import FilerReaderConfig, LogConfig, ApiConfig
from datetime import date

from Point import Point

logging.basicConfig(level=LogConfig.LOG_LEVEL, filename=LogConfig.LOG_FILE_NAME)

class DataUtility:
    @staticmethod
    def retrieve_points_from_file(filename):
        if (not filename):
            logging.error('Invalid input params to retrieve points from file')
            return []
        points = []
        try:
            file_full_path = FilerReaderConfig.BASE_PATH_DL + filename + FilerReaderConfig.FILE_EXTENSION
            with open(file_full_path, 'r') as f:
                headers = f.readline()
                lineNum = 0
                for line in f:
                    lineNum+=1
                    columnData = line.split(',')
                    if (len(columnData) < 2):
                        continue
                    try:
                        date = columnData[0]
                        closing_price = columnData[1]
                        point = Point(date=date, closing_price=closing_price)
                        points.append(point)
                        logging.debug('Filename: ' + filename + ', date: ' + date + ' ,closing_price: ' + closing_price)
                    except:
                        logging.error('Failed to add point, row num: ' + lineNum)
        except:
            logging.error('Error in reading line from: ' + filename)


        logging.info('Returning ' + str(len(points)) + ' points from DL for fileName: ' + filename)
        return points

    @staticmethod
    def retrieve_points_from_api(ticker):
        if(not ticker):
            logging.error('Invalid input params to retrieve points from api')
            return []
        points = []

        try:
            url = ApiConfig.Stooq.URL_PREFIX + ticker + ApiConfig.Stooq.URL_SUFFIX
            httpData = requests.get(url)

            if(httpData.ok and httpData.content != None):
                decodedContent = httpData.content.decode('utf-8')
                lines = decodedContent.split('\n')
                len_lines = len(lines)
                if(len_lines > 1):
                    #First item is column headers, so skip it
                    for i in range(1, len_lines):
                        columnData = lines[i].split(',')
                        if(len(columnData) < 6):
                            continue
                        try:
                            date = columnData[0]
                            closing_price = columnData[4]
                            volume = columnData[5]

                            point = Point(date=date, closing_price=closing_price, volume=volume)
                            points.append(point)
                            logging.debug('Ticker: ' + ticker + ', date: ' + date + ' ,closing_price: ' + closing_price + ' ,volume: ' + volume)
                        except:
                            logging.error('Failed to add point, row num: ' + i)
        except:
            logging.error('Error in http get request: ' + url)

        logging.info('Returning ' + str(len(points)) + ' points from API for ticker: ' + ticker)
        return points

    @staticmethod
    def retrieve_points(ticker):
        if(not ticker):
            return []

        ticker = ticker.lower()
        if(ticker.endswith(".dl")):
            file_name = ticker[:-3]
            logging.debug("DL file_name: " + file_name)
            return DataUtility.retrieve_points_from_file(file_name)

        return DataUtility.retrieve_points_from_api(ticker)