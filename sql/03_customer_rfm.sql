-- RFM dos clientes

WITH reference_date AS (
    SELECT MAX(invoice_date)::date AS max_date
    FROM sales
),
customer_rfm AS (
    SELECT
        customer_id,
        MAX(invoice_date)::date AS last_purchase,
        COUNT(DISTINCT invoice_no) AS frequency,
        SUM(revenue) AS monetary
    FROM sales
    WHERE customer_id IS NOT NULL
    GROUP BY customer_id
)
SELECT
    customer_id,
    last_purchase,
    frequency,
    monetary,
    reference_date.max_date - customer_rfm.last_purchase AS recency
FROM customer_rfm
CROSS JOIN reference_date
ORDER BY monetary DESC
LIMIT 20;


-- Segmentação dos clientes

WITH reference_date AS (
    SELECT MAX(invoice_date)::date AS max_date
    FROM sales
),
customer_rfm AS (
    SELECT
        customer_id,
        MAX(invoice_date)::date AS last_purchase,
        COUNT(DISTINCT invoice_no) AS frequency,
        SUM(revenue) AS monetary
    FROM sales
    WHERE customer_id IS NOT NULL
    GROUP BY customer_id
),
rfm AS (
    SELECT
        customer_id,
        frequency,
        monetary,
        reference_date.max_date - customer_rfm.last_purchase AS recency
    FROM customer_rfm
    CROSS JOIN reference_date
)
SELECT
    customer_id,
    recency,
    frequency,
    monetary,
    CASE
        WHEN recency <= 30 THEN 'Recente'
        WHEN recency <= 90 THEN 'Ativo'
        WHEN recency <= 180 THEN 'Em risco'
        ELSE 'Inativo'
    END AS customer_segment
FROM rfm
ORDER BY monetary DESC;