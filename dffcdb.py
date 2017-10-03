"""Database handling doc"""

import pyodbc
import params
from queries import account

class DbBot:
    """Class for handling db related operations"""


    def __init__(self):
        self.__conn = pyodbc.connect(params.CONNECTION_STRING)
        self.__db_cursor = self.__conn.cursor()


    def account_exists(self, acc_num):
        """Get accounts specified in list"""
        self.__db_cursor.execute(account.GET_ACCOUNT_NUM.format(str(acc_num)))
        return self.__db_cursor.fetchone()


    def get_last_account_num(self):
        """Get last account entered from DB"""
        self.__db_cursor.execute(account.GET_LAST_ACCOUNT_NUM)
        row = self.__db_cursor.fetchone()
        return row.AccountNumber
