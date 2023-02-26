import re
import pandas as pd


class Capture:
    KEY = 'message'

    def __init__(self, log_path: str):
        self.log_frame = pd.DataFrame
        self.data_frame = pd.DataFrame

        self.init_log_file(log_path)

    # beta
    def init_log_file(self, log_path: str):
        """
        :param log_path:
        :return:
        """
        lst_log = []
        with open(log_path, encoding='utf-8') as log_etl:
            for line in log_etl:
                if 'Time Cost' in line:
                    lst_log.append(line.strip())
        self.log_frame = pd.DataFrame({self.KEY: lst_log})
        self.log_frame.head()

    def get_pattern_data(self, ):
        """

        :return:
        """
        content = self.log_frame[self.KEY].str
        for line in content:
            pass


# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

regex = r"(?<=Time Cost: )[\d\.]+(?=s)"
