# transactions.py — Transaction Engine
from accounts import get_account
OVERDRAFT_FEE = 25
def deposit(account_id, amount):
    acc = get_account(account_id) # acc is a reference to the same dict
    acc["balance"] += amount
    acc["history"].append(f"Deposit: +{amount}")
    print(f"Deposited {amount}. Balance: {acc['balance']}")
def withdraw(account_id, amount):
    acc = get_account(account_id)
    if acc["balance"] < amount:
        # Allow overdraft but charge a fee
        acc["balance"] -= (amount + OVERDRAFT_FEE)
        acc["history"].append(
            f"Withdrawal: -{amount} (overdraft fee: -{OVERDRAFT_FEE})"
        )
        print(f"Overdraft! Withdrew {amount} + fee {OVERDRAFT_FEE}. "
              f"Balance: {acc['balance']}")
        return
    acc["balance"] -= amount
    acc["history"].append(f"Withdrawal: -{amount}")
    print(f"Withdrew {amount}. Balance: {acc['balance']}")
def transfer(from_id, to_id, amount):
    src = get_account(from_id) # two references simultaneously
    dst = get_account(to_id)
    if src["balance"] < amount:
        print("Transfer failed: Insufficient funds.")
        return
    src["balance"] -= amount
    dst["balance"] += amount
    src["history"].append(f"Transfer out: -{amount} to {to_id}")
    dst["history"].append(f"Transfer in: +{amount} from {from_id}")
    print(f"Transferred {amount} from {from_id} to {to_id}.")
