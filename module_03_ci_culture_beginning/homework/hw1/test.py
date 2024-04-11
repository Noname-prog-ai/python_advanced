from datetime import datetime, timedelta
import unittest
from freezegun import freeze_time

from module_03_ci_culture_beginning.homework.hw1.hello_word_with_day import app

greetings = (
    'хорошего понедельника',
    'хорошего вторника',
    'хорошей среды',
    'хорошего четверга',
    'хорошей пятницы',
    'хорошей субботы',
    'хорошего воскресенья'
)

class TestHelloWorldApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = "/hello-world/"

    @staticmethod
    def now_with_offset(offset: int, now: datetime = datetime.now()) -> datetime:
        return now + timedelta(days=offset)

    def test_can_get_correct_username_with_weekday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertIn(username, response_text)

    def test_can_get_correct_weekday(self):
        username = "username"
        for i in range(0, 7):
            date = self.now_with_offset(i)
            weekday = date.weekday()
            with self.subTest(i=i), freeze_time(date):
                response = self.app.get(self.base_url + username)
                response_text = response.data.decode()
                self.assertIn(greetings[weekday], response_text)