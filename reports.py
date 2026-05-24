# reports.py — Reporting Module
from accounts import registry
def account_summary(account_id):
    acc = registry[account_id]
    print(f"\n--- Account Summary ---")
    print(f"Owner: {acc['owner']}")
    print(f"Balance: {acc['balance']}")
    print(f"History: {acc['history']}")
def snapshot(account_id):
    acc = registry[account_id]
    snap = acc # ← BUG: still a reference, not a copy
    return snap
def audit_report():
    print("\n=== Audit Report ===")
    for acc_id, acc in registry.items():
        print(f"{acc_id}: {acc['owner']} | Balance: {acc['balance']}")
