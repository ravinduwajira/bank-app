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
def compare_snapshot(snap, account_id):
    current = registry[account_id]
    print(f"\n--- Snapshot Comparison ---")
    print(f"Snapshot balance: {snap['balance']}")
    print(f"Current balance: {current['balance']}")
    if id(snap) == id(current):
        print("WARNING: snapshot IS the live object — not independent!")
    else:
        print("Snapshot is independent (deepcopy confirmed).")
def audit_report():
    print("\n=== Audit Report ===")
    for acc_id, acc in registry.items():
        print(f"{acc_id}: {acc['owner']} | Balance: {acc['balance']}")
