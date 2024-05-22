import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('hw_4_database.db')
cursor = conn.cursor()

# 1. Определить сколько человек с острова N находятся за чертой бедности
cursor.execute("SELECT COUNT(*) FROM salaries WHERE salary < 5000")
poverty_count = cursor.fetchone()[0]
print(f"Число людей за чертой бедности: {poverty_count}")

# 2. Посчитать среднюю зарплату по острову N
cursor.execute("SELECT AVG(salary) FROM salaries")
avg_salary = cursor.fetchone()[0]
print(f"Средняя зарплата на острове: {avg_salary}")

# 3. Посчитать медианную зарплату по острову
cursor.execute("SELECT salary FROM salaries ORDER BY salary")
rows = cursor.fetchall()
count = len(rows)
if count % 2 == 0:
    median_salary = (rows[count//2-1][0] + rows[count//2][0]) / 2
else:
    median_salary = rows[count//2][0]
print(f"Медианная зарплата на острове: {median_salary}")

# 4. Посчитать число социального неравенства F
cursor.execute("SELECT CAST(SUM(salary) AS FLOAT), CAST(SUM(salary) AS FLOAT) - CAST(SUM(salary)/10 AS FLOAT) FROM salaries")
row = cursor.fetchone()
T = row[0]
K = row[1]
inequality_ratio = (T-K)/K * 100
print(f"Число социального неравенства F: {inequality_ratio:.2f}%")

# Закрытие соединения с БД
conn.close()