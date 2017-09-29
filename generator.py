"""create testing csv file"""
from enum import Enum
import random
import string
import sys
import config
from dbbot import DbBot


DB_BOT = DbBot()
OUTPUT = []
USER_OPTIONS = {}

class Command(Enum):
    """TollCRM commands"""
    ADD = 2
    ASSIGN = 3
    REMOVE = 4

class UtilityBot:
    """Provides utility functions validating user input for numeric menus"""

    @staticmethod
    def get_commands(min_rng, max_rng):
        """Limit user input to digits within min and max range"""
        """and return selected commands"""
        while True:
            user_input = sys.stdin.readline().strip()
            if int(user_input) > min_rng and\
            int(user_input) < max_rng:
                USER_OPTIONS.update({"commands" : str(user_input)})
                break
            print("Let's try that again love (options %d to %d):\t"\
            % int(min_rng), int(max_rng), end="")

    @staticmethod
    def __generate_commands(user_input):
        """Generates commands based on user input"""
        commands = 
        if user_input is 1:
            for

    @staticmethod
    def get_accounts():
        """Secure existing account selection"""
        counter = 1
        while True:
            print("Account {}:\t".format(str(counter)))
            try:
                user_input = int(sys.stdin.readline())
                acct_ids.append(self.generate_account(user_input))
                continue
            except ValueError:
                print("Please try again, only numbers accepted:\t", end="")
                continue
            #If no account id is entered return last account id
            #entered in database
            if not acct_ids and str.strip(user_input) == "":
                acct_ids.append(DB_BOT.get_last_account_id())
                counter += 1
                return acct_ids
            #User marked input finished
            elif acct_ids and str.strip(user_input) == "":
                return acct_ids
            #Check if account exists
            else:
                if DB_BOT.account_exists(user_input):
                    acct_ids.append(user_input)
                    counter += 1
                else:
                    print("That account doesn't exist")
                continue
        return acct_ids

    @staticmethod
    def get_plates():
        


class ConfigurationBot:
    """Collects and holds configuration info provided by the user"""
    def __init__(self):
        print("Select command composition of the file:")
        print("1. Random")
        print("2. Only ADD")
        print("3. Only ASSIGN")
        print("4. Only REMOVE\n")
        print("Enter:\t", end="")
        UtilityBot.get_commands_input(1, 4)

        print("Enter account IDs to use"\
        +"(leave empty to end; if no ID is entered a random ID will be used):\t", end="")
        UtilityBot.get_accounts_input()

        print("Select the plate repeating pattern:")
        print("1. Only random plates")
        print("2. Less than 1000 plates")
        print("3. Less than 100 plates")
        print("4. Less than 10 plates")
        print("Enter:\t", end="")
        UtilityBot.get_plates_input()


class WriterBot:
    """Writes data to CSV file"""
