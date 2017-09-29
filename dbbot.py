"""Database handling doc"""
import pyodbc
import params

class DbBot:
    """Class for handling db related operations"""


    def __init__(self):
        self.__conn = pyodbc.connect(params.CONNECTION_STRING)
        self.__db_cursor = self.__conn.cursor()


    def account_exists(self, acc_id):
        """Get accounts specified in list"""
        self.__db_cursor.execute(GET_ACCOUNT_ID.format(acc_id))
        return self.__db_cursor.fetchone()



    def get_last_account_id(self):
        """Get last account entered from DB"""
        self.__db_cursor.execute(GET_LAST_ACCOUNT_ID)
        row = self.__db_cursor.fetchone()
        return row.AccountId


#SQL queries
GET_ACCOUNT_ID =\
'''
SELECT AccountId FROM
[ITS_CSC].[Customer].[Account]
WHERE AccountId = {}
'''

GET_LAST_ACCOUNT_ID =\
'''
SELECT TOP 1 AccountId FROM
[ITS_CSC].[Customer].[Account]
ORDER BY 1 DESC
'''
