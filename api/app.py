from flask import Flask, jsonify, request
from etl.db import engine
import sqlalchemy

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/metrics/daily-volume")
def daily_volume():
    sql = """
    SELECT DATE(txn_time) as day, SUM(amount) as total
    FROM transactions
    GROUP BY DATE(txn_time)
    ORDER BY day DESC
    LIMIT 30;
    """
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.text(sql)).fetchall()
    return jsonify([{"day": str(r[0]), "total": float(r[1])} for r in result])

@app.route("/top-customers")
def top_customers():
    limit = int(request.args.get("limit", 10))
    sql = f"""
    SELECT c.customer_id, c.name, SUM(t.amount) total
    FROM customers c
    JOIN accounts a ON c.customer_id = a.customer_id
    JOIN transactions t ON a.account_id = t.account_id
    GROUP BY c.customer_id, c.name
    ORDER BY total DESC
    LIMIT :limit;
    """
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.text(sql), {"limit": limit}).fetchall()
    return jsonify([{"customer_id": r[0], "name": r[1], "total": float(r[2])} for r in result])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
