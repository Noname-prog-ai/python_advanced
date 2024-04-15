import unittest
from remote_execution import run_python_code_in_subprocess

class TestCodeExecution(unittest.TestCase):

    def test_code_execution_timeout(self):
        result = run_python_code_in_subprocess("while True: pass", 1)
        self.assertEqual(result, "execution timed out")

    def test_code_execution_success(self):
        result = run_python_code_in_subprocess("print('Hello, World!')", 1)
        self.assertEqual(result, "Hello, World!\n")

    def test_invalid_input(self):
        result = run_python_code_in_subprocess("print('Hello, World!')", "invalid")
        self.assertEqual(result, "invalid input")

if __name__ == '__main__':
    unittest.main()
