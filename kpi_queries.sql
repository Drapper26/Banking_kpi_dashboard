-- Banking KPI Dashboard SQL Layer
-- Portfolio focus: Financial Services / FinTech Analytics

-- 1. Executive KPI Summary
SELECT
    COUNT(DISTINCT c.customer_id) AS total_customers,
    ROUND(SUM(CASE WHEN a.balance > 0 THEN a.balance ELSE 0 END), 2) AS total_deposits,
    ROUND(SUM(l.principal), 2) AS total_loan_principal,
    ROUND(100.0 * SUM(CASE WHEN l.loan_status = 'Default' THEN 1 ELSE 0 END) / COUNT(l.loan_id), 2) AS default_rate_pct,
    ROUND(100.0 * SUM(CASE WHEN c.churn_flag = 1 THEN 1 ELSE 0 END) / COUNT(DISTINCT c.customer_id), 2) AS churn_rate_pct
FROM customers c
LEFT JOIN accounts a ON c.customer_id = a.customer_id
LEFT JOIN loans l ON c.customer_id = l.customer_id;

-- 2. Deposits by Branch
SELECT
    c.branch,
    ROUND(SUM(CASE WHEN a.balance > 0 THEN a.balance ELSE 0 END), 2) AS deposits
FROM accounts a
JOIN customers c ON a.customer_id = c.customer_id
GROUP BY c.branch
ORDER BY deposits DESC;

-- 3. Loan Risk by Risk Band
SELECT
    c.risk_band,
    COUNT(l.loan_id) AS loan_count,
    ROUND(SUM(l.principal), 2) AS total_principal,
    ROUND(100.0 * SUM(CASE WHEN l.loan_status = 'Default' THEN 1 ELSE 0 END) / COUNT(l.loan_id), 2) AS default_rate_pct
FROM loans l
JOIN customers c ON l.customer_id = c.customer_id
GROUP BY c.risk_band
ORDER BY default_rate_pct DESC;

-- 4. Channel Transaction Mix
SELECT
    channel,
    COUNT(*) AS transaction_count,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM transactions), 2) AS transaction_share_pct
FROM transactions
GROUP BY channel
ORDER BY transaction_count DESC;

-- 5. Monthly Transaction Trend
SELECT
    strftime('%Y-%m', transaction_date) AS month,
    COUNT(*) AS transaction_volume,
    ROUND(SUM(amount), 2) AS net_transaction_amount
FROM transactions
GROUP BY strftime('%Y-%m', transaction_date)
ORDER BY month;