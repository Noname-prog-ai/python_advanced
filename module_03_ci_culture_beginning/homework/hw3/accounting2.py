import unittest
from flask import Flask

app = Flask(__name__)
storage = {}

# заполнение storage изначальными данными
storage["2022"] = {"01": 100, "02": 150, "03": 200}


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

    return "expense added successfully"


@app.route('/calculate/<int:year>', methods=['GET'])
def calculate_year(year):
    if str(year) not in storage:
        return "no expenses for the year"

    total_expense = sum(storage[str(year)].values())

    return f"total expenses for {year}: {total_expense}"


@app.route('/calculate/<int:year>/<int:month>', methods=['GET'])
def calculate_month(year, month):
    if str(year) not in storage or str(month) not in storage[str(year)]:
        return "no expenses for the specific month"

    total_expense_month = storage[str(year)][str(month)]

    return f"total expenses for {month}/{year}: {total_expense_month}"


if __name__ == "__main__":
    app.run()
