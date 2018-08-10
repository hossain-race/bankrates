# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# web: http://pythonbangla.com
# license: MIT License

# Main Program

from constants import *
from banks.ibbl import IBBL
from helper import verify_https_issue

def main():
    ibbl = IBBL(url=BANK_URLS['ibbl'])
    ibbl.retrieve_webpage()
    ibbl.debug()

if __name__ == '__main__':
    verify_https_issue()
    main()
