:\Users\Fantom\AppData\Local\Programs\Python\Python312\python.exe "C:/Program Files/JetBrains/PyCharm Community Edition 2023.3.5/plugins/python-ce/helpers/pycharm/_jb_unittest_runner.py" --target testperson.TestPerson.test_is_homeless 
Testing started at 20:37 ...
Launching unittests with arguments python -m unittest testperson.TestPerson.test_is_homeless in C:\Users\Fantom\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\hw4


Error
Traceback (most recent call last):
  File "C:\Users\Fantom\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\hw4\testperson.py", line 26, in test_is_homeless
    self.assertFalse(self.person.is_homeless())
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Fantom\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\hw4\person.py", line 27, in is_homeless
    return address is None
           ^^^^^^^
NameError: name 'address' is not defined. Did you mean: 'self.address'?



Ran 1 test in 0.021s

FAILED (errors=1)

Process finished with exit code 1

- Исправлена ошибка в методе get_age, где неправильно вычислялся возраст.

- Исправлена ошибка в методе set_name, где неправильно было присваивание нового имени.

- Исправлена ошибка в методе set_address, где неправильно использовался оператор сравнения.

- Исправлена ошибка в методе is_homeless, где неправильно проверялось значение адреса.