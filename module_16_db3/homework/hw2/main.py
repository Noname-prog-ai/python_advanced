import sqlite3


sql_script_1 = """
SELECT c.full_name, m.full_name, purchase_amount, 'date'
FROM 'order'
INNER JOIN customer c ON c.customer_id = "order'.customer_id
INNER JOIN manager m ON m.manager_id = 'order'.manager_id
"""

sql_script_2 = """
SELECT c.full_name
FROM customer c
LEFT JOIN 'order' o ON c.customer_id = o.customer_id
WHERE o.customer_id IS NULL
ORDER BY full_name
"""

sql_script_3 = """
SELECT order_no, m.full_name, c.full_name
FROM 'order'
INNER JOIN customer c ON c.customer_id = 'order'.customer_id
INNER JOIN manager m ON m.manager_id = 'order'.manager_id
WHERE m.city != c.city
"""

sql_script_4 = """
SELECT order_no, m.full_name, c.full_name
FROM 'order'
INNER JOIN customer c ON c.customer_id = 'order'.customer_id
WHERE "order".manager_id IS NULL
"""


def main():
    with sqlite3.connect('../hw.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        res = cursor.execute(sql_script_4).fetchall()
        print(res)

if __name__ == '__main__':
    main()