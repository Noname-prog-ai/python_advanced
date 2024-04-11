import datetime
import unittest

from module_03_ci_culture_beginning.homework.hw4.person import Person

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person('John', 1990, '123 Main St')

    def test_get_age(self):
        self.assertEqual(self.person.get_age(), datetime.datetime.now().year - 1990)

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), 'John')

    def test_set_name(self):
        self.person.set_name('Jane')
        self.assertEqual(self.person.get_name(), 'Jane')

    def test_set_address(self):
        self.person.set_address('456 Elm St')
        self.assertEqual(self.person.get_address(), '456 Elm St')

    def test_is_homeless(self):
        self.assertFalse(self.person.is_homeless())
        self.person.set_address('')
        self.assertTrue(self.person.is_homeless())