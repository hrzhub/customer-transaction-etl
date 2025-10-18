# Customer Transactions ETL Pipeline

A simple ETL pipeline that extracts customer transaction data from CSV, validates and transforms it using Python, and loads it into MySQL.
(Future enhancement: expose analytics endpoints via Flask API.)

## Quickstart (Local)

1. Clone the Repository

git clone https://github.com/hrzhub/customer-transaction-etl.git
cd /path/to/customer-transaction-etl

2. Setup Environment Variables

copy .env.example .env

Then update your MySQL credentials inside .env.

3. Create and Activate Virtual Environment

python -m venv venv
venv\Scripts\activate

4. Install Dependencies

pip install -r api/requirements.txt

5. Setup MySQL Schema

Open MySQL Workbench and run the SQL in:

sql/schema.sql

6. Execute the ETL Pipeline

python -m etl.etl

### Features

- ETL Pipeline: Extract (CSV) → Transform (validate, clean) → Load (MySQL)
- Data Validation: Ensures correct transaction formats and valid data types
- Modular Design: etl/ for pipeline logic, data/ for sources, sql/ for schema
- Configurable Environment: .env file for database credentials
