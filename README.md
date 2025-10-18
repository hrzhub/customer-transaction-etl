# Customer Transactions ETL + API

A simple ETL pipeline that ingests CSV transaction data, validates and loads into MySQL, and exposes basic analytics via a Flask API.

## Quickstart (local)

1. `git clone <repo>`
2. `cp .env.example .env` and edit if needed
3. `docker-compose up -d` (starts MySQL)
4. `docker exec -it <db_container> bash` then `mysql -u root -p` and run `sql/schema.sql`
5. `python -m venv venv && source venv/bin/activate`
6. `pip install -r api/requirements.txt` (requirements file should include Flask, SQLAlchemy, pymysql)
7. `python etl/etl.py`
8. `python api/app.py` and visit `http://localhost:5000/metrics/daily-volume`

## What to show in interviews

- Table schema and normalization decisions
- How the ETL handles duplicates and type errors
- Simple performance thought: indexes on txn_time, txn_id
- How you'd move MySQL to AWS RDS and run ETL in a Lambda / ECS task (explain, or add scripts later)

## Next steps (optional)

- Add unit tests for validators
- Add Dockerfile for Flask app and docker-compose service
- Implement Airflow DAG for the ETL
