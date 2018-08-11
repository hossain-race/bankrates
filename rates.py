# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# web: http://pythonbangla.com
# license: MIT License

# Main Program

from constants import *
from banks.ibbl import IBBL
from helper import *

def main():
    ibbl = IBBL(url=BANK_URLS['ibbl'])
    # ibbl.retrieve_webpage()
    # write_webpage_as_html(data=ibbl.get_scraped_raw_data())

    ibbl.set_scraped_raw_data(data=read_webpage_from_html())
    ibbl.convert_data_to_bs4()
    ibbl.scrap_webpage_data()

if __name__ == '__main__':
    verify_https_issue()
    main()
