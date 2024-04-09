from datetime import datetime
import unittest

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

class TestMaxNumberApp(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()
        self.base_url = "/hello-world/"

    def _get_weekday(self):
        current_day = datetime.today().weekday()
        return greetings[current_day]

    def test_can_get_correct_weekday(self):
        username = "some"
        weekday = self._get_weekday()
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)