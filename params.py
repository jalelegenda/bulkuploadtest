"""configuration variables for csv generating script"""
from enum import Enum

class Command(Enum):
    """TollCRM commands"""
    ADD = 2
    ASSIGN = 3
    REMOVE = 4


CONNECTION_FORMAT = "DRIVER={driver};SERVER={server};"+\
                    "DATABASE={database};UID={username};PWD={password}"

CONNECTION_PARAMS = {
    "driver": "{SQL Server Native Client 11.0}",
    "server": "DF-DEV-SQL02",
    "database": "ITS_CSC",
    "username": "sa",
    "password": "abc123."
}

#Connection string:
#DRIVER={SQL Server Native Client 11.0};SERVER=DF-DEV-SQL02;DATABASE=ITS_CSC;UID=sa;PWD=abc123.
CONNECTION_STRING = CONNECTION_FORMAT.format(**CONNECTION_PARAMS)


CSV_HEADER =    "Action,AccountNumber,VehicleRegistration,Make,Model,"+\
                "Colour,CountryOfRegistration,DartfordClass,GroupName"


PLATES_NUM = {
    1: 2500,
    2: 1000,
    3: 100,
    4: 10
}
