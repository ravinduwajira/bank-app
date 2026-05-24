# accounts.py — Account Registry
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
    return registry.get(account_id) # returns a REFERENCE, not a copy
