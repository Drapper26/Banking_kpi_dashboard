import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Banking KPI Dashboard", layout="wide")

st.title("Banking KPI Dashboard")
st.caption("Financial Services Analytics Portfolio Project | SQL + KPI Design + Streamlit")

conn = sqlite3.connect("../data/banking_kpi.db")

customers = pd.read_sql("SELECT * FROM customers", conn)
accounts = pd.read_sql("SELECT * FROM accounts", conn)
transactions = pd.read_sql("SELECT * FROM transactions", conn)
loans = pd.read_sql("SELECT * FROM loans", conn)

transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"])
transactions["month"] = transactions["transaction_date"].dt.to_period("M").astype(str)

total_customers = customers["customer_id"].nunique()
total_deposits = accounts.loc[accounts["balance"] > 0, "balance"].sum()
loan_book = loans["principal"].sum()
default_rate = (loans["loan_status"].eq("Default").mean() * 100)
churn_rate = (customers["churn_flag"].mean() * 100)
txn_volume = len(transactions)

c1, c2, c3, c4, c5, c6 = st.columns(6)
c1.metric("Customers", f"{total_customers:,}")
c2.metric("Deposits", f"${total_deposits/1_000_000:.2f}M")
c3.metric("Loan Book", f"${loan_book/1_000_000:.2f}M")
c4.metric("Default Rate", f"{default_rate:.2f}%")
c5.metric("Churn Rate", f"{churn_rate:.2f}%")
c6.metric("Transactions", f"{txn_volume:,}")

branch_deposits = accounts.merge(customers[["customer_id","branch"]], on="customer_id")
branch_deposits = branch_deposits[branch_deposits["balance"] > 0].groupby("branch", as_index=False)["balance"].sum()

channel_mix = transactions.groupby("channel", as_index=False)["transaction_id"].count().rename(columns={"transaction_id":"transactions"})

risk_default = loans.merge(customers[["customer_id","risk_band"]], on="customer_id")
risk_default = risk_default.groupby("risk_band", as_index=False).agg(
    loan_count=("loan_id","count"),
    default_rate=("loan_status", lambda s: (s == "Default").mean() * 100)
)

monthly_trend = transactions.groupby("month", as_index=False).agg(
    transaction_volume=("transaction_id","count"),
    net_transaction_amount=("amount","sum")
)

left, right = st.columns(2)
with left:
    st.subheader("Deposits by Branch")
    st.plotly_chart(px.bar(branch_deposits, x="branch", y="balance"), use_container_width=True)

with right:
    st.subheader("Transaction Channel Mix")
    st.plotly_chart(px.pie(channel_mix, names="channel", values="transactions"), use_container_width=True)

left2, right2 = st.columns(2)
with left2:
    st.subheader("Default Rate by Risk Band")
    st.plotly_chart(px.bar(risk_default, x="risk_band", y="default_rate", hover_data=["loan_count"]), use_container_width=True)

with right2:
    st.subheader("Monthly Transaction Volume")
    st.plotly_chart(px.line(monthly_trend, x="month", y="transaction_volume"), use_container_width=True)

st.subheader("Executive Summary")
st.write("""
This dashboard gives banking leaders a high-level view of deposits, loan exposure,
default risk, customer churn, and transaction channel adoption. It demonstrates SQL querying,
KPI design, banking-domain analytics, and dashboard storytelling.
""")