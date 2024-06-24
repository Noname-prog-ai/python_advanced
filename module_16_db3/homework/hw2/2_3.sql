SELECT order_no, m.full_name, c.full_name
FROM 'order'
INNER JOIN customer c ON c.customer_id = 'order'.customer_id
INNER JOIN manager m ON m.manager_id = 'order'.manager_id
WHERE m.city != c.city