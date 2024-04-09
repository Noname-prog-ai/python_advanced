import unittest
import datetime

class Person:
    def __init__(self, name, year_of_birth, address=''):
        self.name = name
        self.yob = year_of_birth
        self.address = address

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.yob

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def is_homeless(self):
        '''
        returns true if address is not set, false in other case
        '''
        return self.address == ''

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

if __name__ == '__main__':
    unittest.main()