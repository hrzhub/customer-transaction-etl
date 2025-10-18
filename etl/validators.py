import datetime

def validate_row(row: dict):
    # row keys: txn_id, account_id, customer_id, name, email, amount, currency, txn_time, status
    errors = []
    if not row.get("txn_id"):
        errors.append("missing txn_id")
    try:
        float(row.get("amount", ""))
    except:
        errors.append("invalid amount")
    try:
        # Accept ISO or common formats
        datetime.datetime.fromisoformat(row.get("txn_time"))
    except Exception:
        errors.append("invalid txn_time")
    return errors
