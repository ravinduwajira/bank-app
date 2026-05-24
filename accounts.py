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
    acc = registry.get(account_id)
    if acc and acc.get("frozen"):
        print(f"Account {account_id} is frozen.")
        return None
    return acc