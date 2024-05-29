import sqlite3


def ivan_sovin_the_most_effective(
        cursor: sqlite3.Cursor,
        name: str,
) -> None:
    cursor.execute('SELECT name, salary FROM table_effective_manager WHERE name = ?', (name,))
    record = cursor.fetchone()

    if record:
        employee_name, employee_salary = record
        cursor.execute('SELECT salary FROM table_effective_manager WHERE name = "Иван Совин"')
        ivan_salary = cursor.fetchone()[0]

        if employee_salary * 1.1 > ivan_salary:
            cursor.execute('DELETE FROM table_effective_manager WHERE name = ?', (employee_name,))
            print(f'{employee_name} уволен')
        else:
            new_salary = round(employee_salary * 1.1, 2)
            cursor.execute('UPDATE table_effective_manager SET salary = ? WHERE name = ?', (new_salary, employee_name))
            print(f'{employee_name} получил повышение, новая з/п: {new_salary}')
    else:
        print(f'Сотрудник {name} не найден')

if __name__ == '__main__':
    name: str = input('Введите имя сотрудника: ')
    with sqlite3.connect('../homework.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        ivan_sovin_the_most_effective(cursor, name)
        conn.commit()
