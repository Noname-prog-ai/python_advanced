SELECT c.full_name, m.full_name, purchase_amount, 'date'
FROM 'order'
INNER JOIN customer c ON c.customer_id = "order'.customer_id
INNER JOIN manager m ON m.manager_id = 'order'.manager_id