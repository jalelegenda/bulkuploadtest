"""Utility classes the app uses"""

import random
import string
import sys
from params import Command, PLATES_NUM

class UserInputValidator:
    """Provides utility functions validating user input for numeric menus"""

    def __init__(self, user_options, dbc):
        self.__user_options = user_options
        self.__dbc = dbc

    def __process_accounts(self):
        """Secure existing account selection"""
        counter = 1
        accounts = []
        while True:
            print("Account %d.:\t" % counter, end="")
            user_input = sys.stdin.readline().strip()
            if user_input not in string.digits:
                print("Only numbers accepted, try again...")
            elif user_input == "":
                print("Accounts saved...")
                self.__user_options.update({"accounts": accounts})
                return 0
            else:
                if not self.__dbc.account_exists(user_input):
                    print("That account does not exist, try again...")
                else:
                    accounts.append(user_input)
                    counter += 1


    def process(self, key, min_rng=0, max_rng=0):
        """Limit user input to digits within min and max range
        and save user choices"""
        if key == "accounts":
            self.__process_accounts()
            return 0
        while True:
            user_input = sys.stdin.readline().strip()
            if user_input not in string.digits:
                print("Only numbers accepted, try again...")
                continue
            if int(user_input) >= min_rng and\
            int(user_input) <= max_rng:
                self.__user_options.update({key : str(user_input)})
                return
            print("Let's try that again (numbers %d to %d):\t"\
            % (int(min_rng), int(max_rng)), end="")


class Generator:
    """Generates rows to be written to file"""

    def __init__(self, user_options):
        self.__user_options = user_options

    def __generate_command(self):
        """Generate TollCRM command"""
        index = (random.choice(string.digits)for _ in range(2, 4))
        return Command(index).name

    def __generate_plates(self, limit):
        """Generate a random plate number with two letters and 3 numbers"""
        plates = []
        for i in range(1, limit):
            #plate is a string starting with 2 random letters and ending in 3 random numbers
            plate = ''.join(random.choice(string.ascii_lowercase)for _ in range(2))\
            .join(random.choice(string.digits)for _ in range(3))
            if plate in plates:
                i -= 1
                continue
            plates.append(plate)
        return plates

    def __generate_group(self):
        """Generate a random group name"""
        groups = ["", "Drinks", "Food", "Clothes", "Transportation", "Hardware", "Furniture"]
        group = groups[random.randrange(0, len(groups)-1)]
        return group

    def __construct_row(self, command, accountnum, platenum, groupname):
        """Generate entry for writing to file"""
        line = command + ","\
        + accountnum + ","\
        + platenum + ",,,,,,,"\
        + groupname\
        + "\n"
        return line

    def generate_output(self):
        """Generates list with 2500 rows"""
        plates = self.__generate_plates(PLATES_NUM[self.__user_options["plates"]])
        accounts = self.__user_options["accounts"]
        output = []

        for _ in range(1, 2500):
            command = self.__generate_command() if self.__user_options["commands"]\
            not in Command else Command(self.__user_options).name

            accnts_last = len(accounts)-1
            accountnum = accounts[random.randrange(0, accnts_last)]

            plates_last = len(plates)-1
            plate = plates[random.randrange(0, plates_last)]

            #possible additions
            #make = self.__generate_make()
            #model = self.__generate_model()
            #color = self.__generate_color()

            groupname = self.__generate_group()

            row = self.__construct_row(command, accountnum, plate, groupname)
            output.append(row + "\n")

            return output

class Writer:
    """Class that writes output to file"""

    def write(self, output, path):
        """Write to actual file"""
        with open(path + "/bulk_test.csv", "w+") as file_handle:
            file_handle.write(output)
