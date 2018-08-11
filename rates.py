# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# web: http://pythonbangla.com
# license: MIT License

# Main Program

import sys
from constants import *
from banks import ibbl
import helper

def main():
    num_commands = len(sys.argv)
    bank = None

    if num_commands >= 2:
        bank = sys.argv[1].lower()
        bank = bank if bank in BANKS else None

    if bank != None:
        call_process_bank(bank)
    else:
        print("Invalid Commands")

def call_process_bank(name):
    if name == 'ibbl': ibbl.process('ibbl')   

if __name__ == '__main__':
    helper.verify_https_issue()
    main()
