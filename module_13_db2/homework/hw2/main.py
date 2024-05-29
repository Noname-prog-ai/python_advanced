import sqlite3
import csv


def delete_wrong_fees(
        cursor: sqlite3.Cursor,
        wrong_fees_file: str
) -> None:
    with open(wrong_fees_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            date, car_number = row
            # Удаление записей из таблицы `table_fees`
            cursor.execute("DELETE FROM table_fees WHERE date = ? AND car_number = ?", (date, car_number))


if __name__ == "__main__":
    with sqlite3.connect("../homework.db") as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        delete_wrong_fees(cursor, "../wrong_fees.csv")
        conn.commit()
