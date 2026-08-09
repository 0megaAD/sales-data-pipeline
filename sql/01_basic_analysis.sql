-- Receita total
SELECT SUM(revenue) AS total_revenue
FROM sales;


-- Receita por país
SELECT
    country,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY country
ORDER BY total_revenue DESC;


-- Top 10 produtos
SELECT
    stock_code,
    description,
    SUM(quantity) AS total_quantity,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY stock_code, description
ORDER BY total_revenue DESC
LIMIT 10;