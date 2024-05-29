import sqlite3


def check_if_vaccine_has_spoiled(
        cursor: sqlite3.Cursor,
        truck_number: str
) -> bool:
    cursor.execute("SELECT count(*) FROM table_truck_with_vaccine WHERE truck_number = ? AND (SELECT count(*) FROM table_truck_with_vaccine WHERE truck_number = ? AND temperature < -16 OR temperature > -20) >= 3", (truck_number, truck_number))
    result = cursor.fetchone()[0]
    return result > 0


if __name__ == '__main__':
    truck_number: str = input('Введите номер грузовика: ')
    with sqlite3.connect('../homework.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        spoiled: bool = check_if_vaccine_has_spoiled(cursor, truck_number)
        print('Испортилась' if spoiled else 'Не испортилась')
        conn.commit()
