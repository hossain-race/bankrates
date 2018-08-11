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
    curr = None 
    amount = None 
    browser = None

    if num_commands >= 2:
        bank = sys.argv[1].lower()
        bank = bank if bank in BANKS else None

    if num_commands >= 3:
        # for example usd=100
        curr_amount = sys.argv[2].lower().split("=")
        curr = curr_amount[0]
        amount = float(curr_amount[1])

    if num_commands >= 4:
        # browser
        cmd = sys.argv[3].lower()
        if cmd in COMMANDS: browser = True

    if bank != None:
        call_process_bank(bank, curr, amount, browser)
    else:
        print("Invalid Commands")

def call_process_bank(name, curr=None, amount=None, browser=None):
    if name == 'ibbl': 
        ibbl.process('ibbl', curr=curr, amount=amount, browser=browser)   

if __name__ == '__main__':
    helper.verify_https_issue()
    main()
