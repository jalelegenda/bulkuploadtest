"""create testing csv file"""
import sys
from dffcdb import DbBot
from utility import UserInputValidator, Generator, Writer


class App:
    """Determines output data based on input"""
    def __init__(self):
        self.__db_bot = DbBot()
        self.__user_options = {}
        self.__validator = UserInputValidator(self.__user_options, self.__db_bot)
        self.__generator = Generator(self.__user_options)
        self.__writer = Writer()


    def run(self):
        """Program entry point"""
        print("This script will help create a test CSV file for bulk upload testing...")
        print("")

        print("Select command composition of the file:")
        print("1. Random")
        print("2. Only ADD")
        print("3. Only ASSIGN")
        print("4. Only REMOVE\n")
        print("Enter:")
        self.__validator.process("commands", 1, 4)

        print("Enter account IDs to use, "+\
              "(leave empty to end; if no ID is entered a random ID will be used):")
        self.__validator.process("accounts")

        print("Select the plate repeating pattern:")
        print("1. Only random plates")
        print("2. Less than 1000 plates")
        print("3. Less than 100 plates")
        print("4. Less than 10 plates")
        print("Enter:")
        self.__validator.process("plates", 1, 4)

        path = "." if (len(sys.argv) < 2) else sys.argv[1]

        output = self.__generator.generate_output()
        self.__writer.write(output, path)

APP = App()
APP.run()
