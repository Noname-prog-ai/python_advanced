import sqlite3


def update_work_schedule(cursor: sqlite3.Cursor) -> None:
    cursor.execute('CREATE TABLE IF NOT EXISTS new_friendship_schedule '
                   '(day TEXT, employees TEXT)')

    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()

    # Формируем новое расписание
    for employee in employees:
        day = employee['day_preference']
        if day == 'среда':
            continue
        if day == 'пятница':
            continue

        cursor.execute('INSERT INTO new_friendship_schedule (day, employees) VALUES (?, ?)',
                       (day, employee['name']))


if __name__ == '__main':
    with sqlite3.connect('../homework.db') as conn:
        cursor = conn.cursor()
        update_work_schedule(cursor)
        conn.commit()