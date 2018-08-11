# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# web: http://pythonbangla.com
# license: MIT License
# IBBL

from urllib.request import urlopen 
from bs4 import BeautifulSoup
from constants import BANKS
import re

class IBBL:
    def __init__(self, url, verbose=False):
        self._url = url
        self._verbose = verbose
        self._data = ''
        self._rates_data = {}   
        self._published_date = None


    def retrieve_webpage(self):
        try:
            html = urlopen(self._url)
        except Exception as e:
            print (e)
        else:
            self._data = html.read()
            if len(self._data) > 0:
                if self._verbose:
                    print ("Retrieved successfully") 

    def get_scraped_raw_data(self):
        return self._data
    
    def set_scraped_raw_data(self, data):
        self._data = data

    def convert_data_to_bs4(self):
        self._soup = BeautifulSoup(self._data, "html.parser")
   
    def scrap_webpage_data(self):
        currencies_tr = self._soup.find_all(['tr'])
             
        for tr in currencies_tr:
            tds = tr.find_all(['td'])
            if len(tds) == 2:
                curr = tds[0].string 
                rate = tds[1].span.string 

                if curr != None:
                    self._rates_data[curr.lower()] = rate
                    # print(curr, rate)
            elif len(tds) == 1:
                if tds[0].span != None:
                    self._published_date = tds[0].span.string
                    txtre = re.compile(r'\s+')
                    self._published_date = txtre.sub(' ', self._published_date)

        # if self._published_date != None:
            # print(self._published_date)


    def __str__(self):
        output = ''
        if len(self._rates_data) > 0:
            output += '-----------------------------\n'
            output += f'{BANKS[self.__class__.__name__.lower()]}\n'
            output += '-----------------------------\n'
            for curr, rate in self._rates_data.items():
                output += f'{curr.upper()} 1 = BDT {rate}\n'
            if self._published_date != None:
                output += self._published_date + '\n'
        return output

    def create_html_file(self):
        pass

    def debug(self):
        print(self._data)