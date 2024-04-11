C:\Users\Fantom\AppData\Local\Programs\Python\Python312\python.exe "C:/Program Files/JetBrains/PyCharm Community Edition 2023.3.5/plugins/python-ce/helpers/pycharm/_jb_unittest_runner.py" --target testperson.TestPerson 
Testing started at 23:08 ...
Launching unittests with arguments python -m unittest testperson.TestPerson in C:\Users\Fantom\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\hw4



Ran 5 tests in 0.067s

FAILED (failures=2, errors=2)

Error
Traceback (most recent call last):
  File "C:\Users\Fantom\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\hw4\testperson.py", line 12, in test_get_age
    self.assertEqual(self.person.get_age(), datetime.datetime.now().year - 1990)
                     ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Fantom\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\hw4\person.py", line 8, in get_age
    now: datetime.datetime = datetime.datetime.now()
                             ^^^^^^^^
NameError: name 'datetime' is not defined. Did you forget to import 'datetime'


Error
Traceback (most recent call last):
  File "C:\Users\Fantom\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\hw4\testperson.py", line 26, in test_is_homeless
    self.assertFalse(self.person.is_homeless())
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Fantom\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\hw4\person.py", line 27, in is_homeless
    return address is None
           ^^^^^^^
NameError: name 'address' is not defined. Did you mean: 'self.address'?



456 Elm St != 123 Main St

Expected :123 Main St
Actual   :456 Elm St
<Click to see difference>

Traceback (most recent call last):
  File "C:\Users\Fantom\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\hw4\testperson.py", line 23, in test_set_address
    self.assertEqual(self.person.get_address(), '456 Elm St')
AssertionError: '123 Main St' != '456 Elm St'
- 123 Main St
+ 456 Elm St




Jane != John

Expected :John
Actual   :Jane
<Click to see difference>

Traceback (most recent call last):
  File "C:\Users\Fantom\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\hw4\testperson.py", line 19, in test_set_name
    self.assertEqual(self.person.get_name(), 'Jane')
AssertionError: 'John' != 'Jane'
- John
+ Jane



Process finished with exit code 1

- Исправлена ошибка не импортирован модуль datetime.

- Исправлена ошибка в методе get_age, где неправильно вычислялся возраст.

- Исправлена ошибка в методе set_name, где неправильно было присваивание нового имени.

- Исправлена ошибка в методе set_address, где неправильно использовался оператор сравнения.

- Исправлена ошибка в методе is_homeless, где неправильно проверялось значение адреса.