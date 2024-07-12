SELECT order_no, m.full_name, c.full_name
FROM 'order'
INNER JOIN customer c ON c.customer_id = 'order'.customer_id
WHERE "order".manager_id IS NULL