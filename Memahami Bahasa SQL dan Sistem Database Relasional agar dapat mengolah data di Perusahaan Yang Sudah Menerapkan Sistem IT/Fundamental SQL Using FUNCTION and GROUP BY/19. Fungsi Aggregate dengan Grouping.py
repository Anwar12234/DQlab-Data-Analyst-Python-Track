SELECT
    province,
    COUNT(DISTINCT order_id) AS total_unique_order,
    SUM(item_price) AS revenue
FROM
    sales_retail_2019
GROUP BY
    province;
