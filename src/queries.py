def get_countries():
    return """
    SELECT DISTINCT country
    FROM sales
    ORDER BY country;
    """


def get_kpis(country=None):

    if country is None:

        return """
        SELECT
            SUM(revenue) AS total_revenue,
            SUM(quantity) AS total_quantity,
            COUNT(DISTINCT invoice_no) AS total_orders
        FROM sales;
        """

    return """
    SELECT
        SUM(revenue) AS total_revenue,
        SUM(quantity) AS total_quantity,
        COUNT(DISTINCT invoice_no) AS total_orders
    FROM sales
    WHERE country = %(country)s;
    """


def get_monthly_sales(country=None):

    if country is None:

        return """
        SELECT
            period,
            SUM(revenue) AS total_revenue
        FROM sales
        GROUP BY period
        ORDER BY period;
        """

    return """
    SELECT
        period,
        SUM(revenue) AS total_revenue
    FROM sales
    WHERE country = %(country)s
    GROUP BY period
    ORDER BY period;
    """


def get_top_products(country=None):

    if country is None:

        return """
        SELECT
            description,
            SUM(quantity) AS total_quantity,
            SUM(revenue) AS total_revenue
        FROM sales
        WHERE description IS NOT NULL
        GROUP BY description
        ORDER BY total_revenue DESC
        LIMIT 10;
        """

    return """
    SELECT
        description,
        SUM(quantity) AS total_quantity,
        SUM(revenue) AS total_revenue
    FROM sales
    WHERE country = %(country)s
    AND description IS NOT NULL
    GROUP BY description
    ORDER BY total_revenue DESC
    LIMIT 10;
    """


def get_customer_rfm(country=None):

    if country is None:

        return """
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
        FROM rfm;
        """

    return """
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
        WHERE country = %(country)s
        AND customer_id IS NOT NULL
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
    FROM rfm;
    """