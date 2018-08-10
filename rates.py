# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/banglaprogramming
# License: MIT License

# Main Program

from constants import *
from ibbl import IBBL
from helper import verify_https_issue

def main():
    ibbl = IBBL(url=BANK_URLS['ibbl'])
    ibbl.retrieve_webpage()
    ibbl.debug()

if __name__ == '__main__':
    verify_https_issue()
    main()
