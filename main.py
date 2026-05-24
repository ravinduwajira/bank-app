# main.py — Entry point
from accounts import create_account, registry
from transactions import deposit, withdraw, transfer
from reports import account_summary, snapshot, audit_report
create_account("ACC001", "Nimal Perera", 1000)
create_account("ACC002", "Amali Silva", 500)
create_account("ACC003", "Kamal Fernando", 750)
