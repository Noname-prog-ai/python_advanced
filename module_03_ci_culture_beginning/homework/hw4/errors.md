C:\Users\Fantom\AppData\Local\Programs\Python\Python312\python.exe "C:/Program Files/JetBrains/PyCharm Community Edition 2023.3.5/plugins/python-ce/helpers/pycharm/_jb_unittest_runner.py" --target testperson.TestPersonMethods.test_is_homeless 
Testing started at 19:47 ...
Launching unittests with arguments python -m unittest testperson.TestPersonMethods.test_is_homeless in C:\Users\Fantom\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\hw4



Ran 1 test in 0.005s

FAILED (errors=1)

Error
Traceback (most recent call last):
  File "C:\Users\Fantom\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\hw4\testperson.py", line 27, in test_is_homeless
    self.assertTrue(homeless_person.is_homeless())
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Fantom\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\hw4\person.py", line 27, in is_homeless
    return address is None
           ^^^^^^^
NameError: name 'address' is not defined. Did you mean: 'self.address'?


Process finished with exit code 1


Исправление:
import datetime

class Person:
    def __init__(self, name: str, year_of_birth: int, address: str = '') -> None:
        self.name = name
        self.yob = year_of_birth
        self.address = address

    def get_age(self) -> int:
        now = datetime.datetime.now()
        return self.yob - now.year

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def set_address(self, address: str) -> None:
        self.address = address

    def get_address(self) -> str:
        return self.address

    def is_homeless(self) -> bool:
        '''
        returns True if address is not set, false in other case
        '''
        return self.address is None
