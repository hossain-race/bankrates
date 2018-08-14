# author: Mahmud Ahsan
# https://github.com/mahmudahsan/bankrates
# blog: http://thinkdiff.net
# web: http://pythonbangla.com
# license: MIT License
# Constants

# Global Variables
CACHE = 3 # minutes
LOCAL_CURRENCY = 'BDT' 

COMMANDS = (
    'browser',
)

BANKS = {
    'ibbl': "Islami Bank Bangladesh Ltd.",
}

CURRENCY = (
    'USD',
    'GBP',
    'EUR',
    'JPY',
    'CHF',
    'SGD',
    'AED',
    'SAR',
    'CAD',
)

BANK_URLS = {
    'ibbl': 'https://www.islamibankbd.com/curr_ex_rate.php',
}

DIRS = {
    'raw' : 'raw/' # storing raw html scraping data
}