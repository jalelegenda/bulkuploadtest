"""Module for testing db related operations"""

from dffcdb import DbBot

ACCT_NUM = 1000000012

def test_account_exists_ret():
    """Test account_exists"""
    db_bot = DbBot()
    account = db_bot.account_exists(ACCT_NUM)
    assert account is not None

def test_account_exists_val():
    """Test account_exists"""
    db_bot = DbBot()
    account = db_bot.account_exists(ACCT_NUM)
    assert account.AccountId == ACCT_NUM
