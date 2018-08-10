# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# web: http://pythonbangla.com
# license: MIT License
# IBBL

from urllib.request import urlopen 
from bs4 import BeautifulSoup

class IBBL:
    def __init__(self, url, verbose=False):
        self._url = url
        self._verbose = verbose
        self._data = ''


    def retrieve_webpage(self):
        try:
            html = urlopen(self._url)
        except Exception as e:
            print (e)
        else:
            self._data = html.read()
            if len(self._data) > 0 and self._verbose:
                print ("Retrieved successfully") 

    def scrap_webpage_data(self):
        pass 

    def __str__(self):
        pass 

    def create_html_file(self):
        pass

    def debug(self):
        print(self._data)