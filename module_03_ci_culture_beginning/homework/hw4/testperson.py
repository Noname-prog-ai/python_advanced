import datetime
import unittest

from module_03_ci_culture_beginning.homework.hw4.person import Person

class TestPersonMethods(unittest.TestCase):

    def setUp(self):
        self.person = Person("John", 1990, "123 Street")

    def test_get_age(self):
        self.assertEqual(self.person.get_age(), datetime.datetime.now().year - 1990)

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), "John")

    def test_set_name(self):
        self.person.set_name("Joe")
        self.assertEqual(self.person.get_name(), "Joe")

    def test_set_address(self):
        self.person.set_address("456 Avenue")
        self.assertEqual(self.person.get_address(), "456 Avenue")

    def test_is_homeless(self):
        homeless_person = Person("Jane", 1985)
        self.assertTrue(homeless_person.is_homeless())
        self.assertFalse(self.person.is_homeless())