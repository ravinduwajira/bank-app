# accounts.py — Account Registry
from datetime import datetime
registry = {} # master dict: account_id -> account dict

def create_account(account_id, owner, balance=0):
    account = {
        "id": account_id,
        "owner": owner,
        "balance": balance,
        "history": []
    }
    registry[account_id] = account
    print(f"Account {account_id} created for {owner}.")
    return account

def get_account(account_id):
    acc = registry.get(account_id)
    if acc:
        acc["last_accessed"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return acc
