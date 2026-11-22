-- Active: 1795368707894@@127.0.0.1@3306
-- Active: 1795368770825@@127.0.0.1@3306
--How many orders are there in total, and how many per status?
--SELECT COUNT(*) AS total_orders FROM orders;

--SELECT status, COUNT(*) AS orders
--FROM orders
--GROUP BY status
--ORDER BY orders DESC;


--The 10 most expensive products, with their category name (product, category, price).
--SELECT products.name as product, categories.name as category, products.price
--FROM products
--JOIN categories ON products.category_id = categories.id
--ORDER BY products.price DESC
--LIMIT 10;


--All products whose name contains "Laptop".
--SELECT id, name, price
--FROM products
--WHERE name LIKE '%Laptop%';


--How many customers are there per country, highest first?
--SELECT country, Count(*) as costumers
--FROM customers
--GROUP BY country
--ORDER BY costumers DESC;


--Which customers have never placed an order?
--SELECT customers.id, customers.first_name, customers.last_name
--FROM customers
--LEFT JOIN orders ON orders.customer_id = customers.id
--WHERE orders.id IS NULL;


--Which products have never been ordered?
--SELECT products.id, products.name
--FROM products
--LEFT JOIN order_items ON order_items.product_id = products.id
--WHERE order_items.id IS NULL;


--Revenue per category, highest first. This chains four tables.
--SELECT categories.name AS category,
--       ROUND(SUM(order_items.quantity * order_items.unit_price), 2) AS revenue
--FROM order_items
--JOIN orders     ON orders.id = order_items.order_id
--JOIN products   ON products.id = order_items.product_id
--JOIN categories ON categories.id = products.category_id
--WHERE orders.status != 'cancelled'
--GROUP BY categories.id
--ORDER BY revenue DESC;


--The 10 customers who spent the most, with first name, last name and total spent.
/* SELECT customers.first_name, customers.last_name, ROUND(SUM(order_items.quantity * order_items.unit_price), 2) AS total_spent
FROM customers
JOIN orders ON customers.id = orders.customer_id
JOIN order_items ON order_items.order_id = orders.id
WHERE orders.status != 'cancelled'
GROUP BY customers.id
ORDER BY total_spent DESC
LIMIT 10; */


--Number of orders per month in 2025, in calendar order.
/* SELECT strftime('%Y-%m', order_date) AS month, COUNT(*) AS orders
FROM orders
WHERE strftime('%Y', order_date) = '2025'
GROUP BY month
ORDER BY month; */


--Customers with at least 5 orders, showing name and number of orders.
/* SELECT customers.first_name, customers.last_name, COUNT(orders.id) AS order_count
FROM customers
JOIN orders ON orders.customer_id = customers.id
GROUP BY customer_id
HAVING COUNT(orders.id) >= 5
ORDER BY order_count DESC; */


--For every category, how many products have stock = 0?
SELECT categories.name, COUNT(products.id) AS out_of_stock
FROM categories
LEFT JOIN products ON products.category_id = categories.id
                  AND products.stock = 0
GROUP BY categories.id
ORDER BY out_of_stock DESC;
