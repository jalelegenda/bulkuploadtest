"""configuration variables for csv generating script"""
CONNECTION_FORMAT = "DRIVER={driver};SERVER={server};"\
                    +"DATABASE={database};UID={username};PWD={password}"

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
