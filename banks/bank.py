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
        self.bank_id = self.__class__.__name__.lower()
        self._url = url
        self._data = ''
        self._rates_data = {}   
        self._published_date = None
        self._from_currency_name = None 
        self._from_currency_amount = None
        self._converted_local_currency_amount = None

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

    def get_converted_amount_as_str(self):
        if self._from_currency_name != None and self._converted_local_currency_amount != None:
                return f'{self._from_currency_name} {self._from_currency_amount} = {LOCAL_CURRENCY} {self._converted_local_currency_amount}'
        return None

    def __str__(self):
        output = ''
        if len(self._rates_data) > 0:
            output += '-----------------------------\n'
            output += f'{BANKS[self.bank_id]}\n'
            output += '-----------------------------\n'
            
            converted_amount = self.get_converted_amount_as_str()
            if converted_amount is not None:
                output += converted_amount + '\n'
            output += '.............................\n'
        return output

    def convert_amount_to_local_currency(self, currency_name, amount):
        if currency_name in self._rates_data:
            self._from_currency_name = currency_name.upper()
            self._from_currency_amount = amount
            self._converted_local_currency_amount = float(self._rates_data[currency_name]) * amount
            self._converted_local_currency_amount = round(self._converted_local_currency_amount, 2)

    def get_output_as_html(self):
        rates_data = ''
        converted_str = self.get_converted_amount_as_str()
        if converted_str != None:
            rates_data += f'<strong>{converted_str}</strong><br><br>'

        if len(self._rates_data) > 0:
            rates_data += '<table border="1">'
            for curr, val in self._rates_data.items():
                rates_data += f'<tr><td>{curr.upper()} 1</td><td>BDT {val}</td></tr>'
            rates_data += '</table>'

        published_date = ''
        if self._published_date != None:
            published_date = f'{self._published_date}'

        output = f'''
<html>
    <head>
        <title>{BANKS[self.bank_id]}</title>
    </head>
    <body>
        <h2>{BANKS[self.bank_id]}</h2>
        {rates_data}
        <br>
        {published_date}
        <br>
        Source: <a href='{BANK_URLS[self.bank_id]}' target='_blank'>{BANKS[self.bank_id]}</a>
    </body>
</html>
'''
        return output

    def debug(self):
        print(self._data)

# Every new bank should define a process function
def process(command):
    pass