import sqlite3

conn = sqlite3.connect('hw_3_database.db')
cur = conn.cursor()

for table_name in ['table_1', 'table_2', 'table_3']:
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    records_count = cur.fetchone()[0]
    print(f"Таблица {table_name} содержит {records_count} записей.")

cur.execute("SELECT COUNT(DISTINCT id) FROM table_1")
unique_records_count_table_1 = cur.fetchone()[0]
print(f"В таблице table_1 есть {unique_records_count_table_1} уникальных записей.")

cur.execute("SELECT COUNT(*) FROM table_1 INNER JOIN table_2 ON table_1.id = table_2.id")
common_records_table_1_2_count = cur.fetchone()[0]
print(f"Встречается {common_records_table_1_2_count} записей из таблицы table_1 в таблице table_2.")

cur.execute("SELECT COUNT(*) FROM table_1 "
            "INNER JOIN table_2 ON table_1.id = table_2.id "
            "INNER JOIN table_3 ON table_1.id = table_3.id")
common_records_table_1_2_3_count = cur.fetchone()[0]
print(f"Встречается {common_records_table_1_2_3_count} записей из таблицы table_1 в таблицах table_2 и table_3.")

cur.close()
conn.close()