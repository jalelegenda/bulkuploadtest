"""Account related queries"""

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

GET_ACCOUNT_NUM =\
'''
SELECT AccountNumber FROM
[ITS_CSC].[Customer].[Account]
WHERE AccountId = {}
'''

GET_LAST_ACCOUNT_NUM =\
'''
SELECT TOP 1 AccountNumber FROM
[ITS_CSC].[Customer].[Account]
ORDER BY 1 DESC
'''