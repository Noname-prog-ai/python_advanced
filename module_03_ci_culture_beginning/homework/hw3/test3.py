import unittest

from module_03_ci_culture_beginning.homework.hw3.accounting2 import app

class TestApp(unittest.TestCase):
    def test_add_expense(self):
        with app.test_client() as client:
            response = client.get('/add/202204/50')
            self.assertEqual(response.data.decode('utf-8'), "expense added successfully")

    def test_calculate_year(self):
        with app.test_client() as client:
            response = client.get('/calculate/2022')
            self.assertEqual(response.data.decode('utf-8'), "total expenses for 2022: 450")

    def test_calculate_month(self):
        with app.test_client() as client:
            response = client.get('/calculate/2022/01')
            self.assertEqual(response.data.decode('utf-8'), "total expenses for 01/2022: 100")

    def test_invalid_date_format(self):
        with app.test_client() as client:
            response = client.get('/add/2022-04-06/50')
            self.assertEqual(response.status_code, 404)

    def test_no_expenses(self):
        global storage
        storage = {}
        with app.test_client() as client:
            response_year = client.get('/calculate/2022')
            response_month = client.get('/calculate/2022/03')
            self.assertEqual(response_year.data.decode('utf-8'), "no expenses for the year")
            self.assertEqual(response_month.data.decode('utf-8'), "no expenses for the specific month")