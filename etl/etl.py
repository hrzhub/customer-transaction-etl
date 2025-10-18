import csv
from etl.db import engine, SessionLocal
from etl.validators import validate_row
import sqlalchemy
from sqlalchemy import text
import os

DATA_FILE = os.getenv("DATA_FILE", "data/sample_transactions.csv")

def upsert_customer(session, customer_id, name, email):
    session.execute(text("""
    INSERT INTO customers (customer_id, name, email)
    VALUES (:customer_id, :name, :email)
    ON DUPLICATE KEY UPDATE name=VALUES(name), email=VALUES(email)
    """), {"customer_id": customer_id, "name": name, "email": email})

def upsert_account(session, account_id, customer_id, account_type="checking"):
    session.execute(text("""
    INSERT INTO accounts (account_id, customer_id, account_type)
    VALUES (:account_id, :customer_id, :account_type)
    ON DUPLICATE KEY UPDATE account_type=VALUES(account_type)
    """), {"account_id": account_id, "customer_id": customer_id, "account_type": account_type})

def insert_transaction(session, txn):
    session.execute(text("""
    INSERT IGNORE INTO transactions (txn_id, account_id, amount, currency, txn_time, status)
    VALUES (:txn_id, :account_id, :amount, :currency, :txn_time, :status)
    """), txn)

def run():
    session = SessionLocal()
    with open(DATA_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            errors = validate_row(row)
            if errors:
                print(f"Skipping row {row.get('txn_id')}: {errors}")
                continue
            upsert_customer(session, row["customer_id"], row.get("name"), row.get("email"))
            upsert_account(session, row["account_id"], row["customer_id"], row.get("account_type","checking"))
            txn = {
                "txn_id": row["txn_id"],
                "account_id": row["account_id"],
                "amount": float(row["amount"]),
                "currency": row.get("currency","MYR"),
                "txn_time": row["txn_time"],
                "status": row.get("status","completed")
            }
            insert_transaction(session, txn)
        session.commit()
    session.close()

if __name__ == "__main__":
    run()
