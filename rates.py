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

    for i, command in enumerate(sys.argv):
        command = command.lower()
        if i == 0: pass # no need fast name
        elif i == 1: 
            # 2nd parameter should be bank name
            bank = command.lower()
            bank = bank if bank in BANKS else None
        else:
            # 3rd and 4th paramet process here
            if command in COMMANDS: browser = True
            elif '=' in command:
                curr_amount = command.split("=")
                curr = curr_amount[0]
                amount = float(curr_amount[1])

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
