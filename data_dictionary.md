# Data Dictionary

## customers.csv
- customer_id: Unique customer identifier
- branch: Primary branch location
- segment: Customer segment
- age: Customer age
- state: Customer state
- credit_score: Synthetic credit score
- join_date: Customer onboarding date
- risk_band: Low, Medium, or High
- churn_flag: 1 if simulated churn risk/customer churn, else 0

## accounts.csv
- account_id: Unique account identifier
- customer_id: Linked customer
- product: Checking, Savings, or Credit Card
- balance: Account balance. Credit card balances may be negative.
- status: Active or Dormant

## transactions.csv
- transaction_id: Unique transaction identifier
- account_id: Linked account
- customer_id: Linked customer
- transaction_date: Transaction date
- transaction_type: Deposit, Withdrawal, Transfer, Purchase, Payment, or Fee
- channel: Mobile, Branch, ATM, Online, or Call Center
- amount: Transaction amount

## loans.csv
- loan_id: Unique loan identifier
- customer_id: Linked customer
- loan_product: Personal Loan, Mortgage, or Auto Loan
- principal: Loan principal
- interest_rate: Loan interest rate
- monthly_payment: Estimated monthly payment
- loan_status: Current, Late, or Default
- days_past_due: Days past due