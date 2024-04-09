from flask import Flask
import requests

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

@app.route('/test-invalid-date/<date>/<int:number>', methods=['GET'])
def test_invalid_date(date, number):
    if len(date) != 8:  # Check if date length is correct
        return "invalid date format"

    try:
        int(date)  # Check if date can be converted to integer
    except ValueError:
        return "invalid date format"

    return "valid date format"

@app.route('/init', methods=['GET'])
def init():
    storage['2022'] = {
        '01': 100,
        '02': 200,
        '03': 150
    }
    storage['2023'] = {
        '01': 120,
        '02': 180,
        '03': 220
    }

    return "storage initialized"

url = 'http://localhost:5000/add/20220101/50'
response = requests.get(url)
print(response.text)

url = 'http://localhost:5000/calculate/2022'
response = requests.get(url)
print(response.text)

url = 'http://localhost:5000/test-invalid-date/202201/50'
response = requests.get(url)
print(response.text)



if __name__ == "__main__":
    app.run()