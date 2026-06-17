# Banking KPI Dashboard

**Portfolio Positioning:** Data Intelligence Analyst specializing in Financial Services / FinTech Analytics.

This project is a complete banking analytics dashboard built using synthetic banking data, SQL, Python, SQLite, and an interactive HTML/Streamlit dashboard.

## Business Problem

Banking leadership needs a single view of customer growth, deposit performance, loan exposure, default risk, customer churn, and transaction channel behavior.

This dashboard answers:

- Which branches hold the highest deposit value?
- What is the total loan book exposure?
- Which customer risk bands have the highest default rate?
- How much transaction activity is coming from mobile, online, branch, ATM, and call center?
- What is the customer churn rate?
- How is transaction volume trending month over month?

## KPI Metrics

- Total Customers
- Total Deposits
- Total Loan Book
- Loan Default Rate
- Customer Churn Rate
- Transaction Volume
- Deposits by Branch
- Default Rate by Risk Band
- Channel Transaction Mix
- Monthly Transaction Trend

## Dataset

Synthetic banking data is included in `/data`:

- `customers.csv`
- `accounts.csv`
- `transactions.csv`
- `loans.csv`
- `banking_kpi.db`

## SQL Layer

Core KPI queries are stored in:

`/sql/kpi_queries.sql`

## How to View the Dashboard

### Option 1: Open the standalone dashboard

Open:

`banking_kpi_dashboard.html`

This works directly in a browser.

### Option 2: Run the Streamlit app

```bash
pip install -r requirements.txt
cd streamlit_app
streamlit run app.py
```

## Why This Project Matters

This project is designed to show hiring managers that the analyst can:

- Understand financial services KPIs
- Design business-relevant metrics
- Work with relational banking-style data
- Use SQL for KPI extraction
- Build executive dashboards
- Communicate insights clearly

## Resume Bullet

Built a banking KPI dashboard using SQL, Python, SQLite, and Streamlit to analyze deposits, loan exposure, default rates, customer churn, and transaction channel performance across 1,200 synthetic banking customers.


## SQL-First Analytics Layer

This project includes a full SQL analytics layer inside the `/sql` folder.

Key SQL files:

- `banking_analytics_full_sql.sql` — complete end-to-end SQL file with schema, KPI queries, analytical views, and dashboard-ready queries.
- `01_schema.sql` — database table structure.
- `02_executive_kpis.sql` — total customers, deposits, loan book, default rate, churn rate, and transaction volume.
- `03_branch_analysis.sql` — branch-level customer, deposit, loan, default, and churn performance.
- `04_customer_segment_analysis.sql` — segment-level customer and deposit analysis.
- `05_credit_risk_loan_analysis.sql` — loan product, credit risk, delinquency, and default analysis.
- `06_transaction_channel_analysis.sql` — transaction volume, value, and channel adoption.
- `07_churn_analysis.sql` — churn by risk band and age group.
- `08_analytical_views.sql` — reusable SQL views such as customer 360, branch KPIs, loan risk summary, and monthly channel trends.
- `09_dashboard_ready_queries.sql` — final queries designed to feed the dashboard layer.

This makes the project SQL-heavy and closer to a real financial analytics workflow.
