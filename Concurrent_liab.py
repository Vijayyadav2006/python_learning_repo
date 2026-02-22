from concurrent.futures import ThreadPoolExecutor
import random

Account_holder=["Aman","Jay","Vijay","Prajay","victory","samael","luci"]


def bank_balance(i):
    account_no=random.randint(10**11,10**12-1)
    account_bal=random.randint(1000,100000)
    print(f"{i} User account No:{account_no} is Available Balance ${account_bal} ")

with ThreadPoolExecutor(max_workers=len(Account_holder)) as executor:
    Bank= executor.map(bank_balance,Account_holder)
