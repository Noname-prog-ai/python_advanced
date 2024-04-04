"""
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""

from flask import Flask


app = Flask(__name__)
storage = {}

@app.route('/add/<date>/<int:number>', methods=['GET'])
def add_expense(date, number):
    year = date[:4]
    month = date[4:6]

    if year not in storage:
        storage[year] = {}
        storage[year][month] = 0
    elif month not in storage[year]:
        storage[year][month] = 0

    storage[year][month] += number

    return "Expense added successfully"

@app.route('/calculate/<int:year>', methods=['GET'])
def calculate_year(year):
    if str(year) not in storage:
        return "No expenses for the year"

    total_expense = sum(storage[str(year)].values())

    return f"Total expenses for {year}: {total_expense}"

@app.route('/calculate/<int:year>/<int:month>', methods=['GET'])
def calculate_month(year, month):
    if str(year) not in storage or str(month) not in storage[str(year)]:
        return "No expenses for the specific month"

    total_expense_month = storage[str(year)][str(month)]

    return f"Total expenses for {month}/{year}: {total_expense_month}"

if __name__ == "__main__":
    app.run()
