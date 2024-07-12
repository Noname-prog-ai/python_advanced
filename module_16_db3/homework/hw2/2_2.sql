SELECT c.full_name
FROM customer c
LEFT JOIN 'order' o ON c.customer_id = o.customer_id
WHERE o.customer_id IS NULL
ORDER BY full_name