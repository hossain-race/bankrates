# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/banglaprogramming
# License: MIT License

# Main Program

from constants import *
from ibbl import IBBL

def main():
    ibbl = IBBL(url=BANK_URLS['ibbl'])
    ibbl.retrieve_webpage()
    ibbl.debug()

# https verify issue solution
# https://bit.ly/2KKXIQD
def verify_https_issue():
    import os, ssl
    
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
        ssl._create_default_https_context =             ssl._create_unverified_context

if __name__ == '__main__':
    verify_https_issue()
    main()
