-- Top categories
SELECT product_category_name,
       SUM(price + freight_value) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY product_category_name
ORDER BY revenue DESC;

-- Monthly sales
SELECT DATE_TRUNC('month', order_purchase_timestamp) AS month,
       SUM(price + freight_value) AS revenue
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY month
ORDER BY month;
