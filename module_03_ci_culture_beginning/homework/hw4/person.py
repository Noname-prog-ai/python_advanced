import unittest
import datetime

class Person:
    def __init__(self, name: str, year_of_birth: int, address: str = '') -> None:
        self.name: str = name
        self.yob: int = year_of_birth
        self.address: str = address

    def get_age(self) -> int:
        now: datetime.datetime = datetime.datetime.now()
        return self.yob - now.year

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = self.name

    def set_address(self, address: str) -> None:
        self.address = address

    def get_address(self) -> str:
        return self.address

    def is_homeless(self) -> bool:
        '''
        returns True if address is not set, false in other case
        '''
        return address is None


class TestPersonClass(unittest.TestCase):

    def setUp(self):
        self.person = Person('alice', 1990, '123 street')

    def test_get_age(self):
        self.assertEqual(self.person.get_age(), 32) # assuming current year is 2022

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), 'alice')

    def test_set_name(self):
        self.person.set_name('bob')
        self.assertEqual(self.person.get_name(), 'bob')

    def test_set_address(self):
        self.person.set_address('456 avenue')
        self.assertEqual(self.person.get_address(), '456 avenue')

    def test_is_homeless(self):
        self.assertFalse(self.person.is_homeless()) # assuming address is set

if __name__ == '__main':
    unittest.main()