# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# web: http://pythonbangla.com
# license: MIT License
# Bank: Parent Class of all Banks

from bs4 import BeautifulSoup
from constants import *

class Bank:
    def __init__(self, url):
        self._url = url
        self._data = ''
        self._rates_data = {}   
        self._published_date = None

    def retrieve_webpage(self):
        pass # override in child class

    def get_scraped_raw_data(self):
        return self._data
    
    def set_scraped_raw_data(self, data):
        self._data = data

    def convert_data_to_bs4(self):
        self._soup = BeautifulSoup(self._data, "html.parser")
   
    def scrap_webpage_data(self):
        pass # override in child class


    def __str__(self):
        output = ''
        if len(self._rates_data) > 0:
            output += '-----------------------------\n'
            output += f'{BANKS[self.__class__.__name__.lower()]}\n'
            output += '-----------------------------\n'
            
        return output

    def create_html_file(self):
        pass # override in child class

    def debug(self):
        print(self._data)

# Every new bank should define a process function
def process(command):
    pass