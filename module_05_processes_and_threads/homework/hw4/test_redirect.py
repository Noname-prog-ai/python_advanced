import unittest
from redirect import Redirect

class TestRedirect(unittest.TestCase):

    def test_stdout_redirect(self):
        stdout_file = open('test_stdout.txt', 'w')
        with Redirect(stdout=stdout_file):
            print('Test stdout redirection')
        stdout_file.close()
        with open('test_stdout.txt', 'r') as f:
            self.assertEqual(f.readline().strip(), 'Test stdout redirection')

    def test_stderr_redirect(self):
        stderr_file = open('test_stderr.txt', 'w')
        with Redirect(stderr=stderr_file):
            try:
                raise Exception('Test stderr redirection')
            except Exception as ex:
                print(ex, file=sys.stderr)
        stderr_file.close()
        with open('test_stderr.txt', 'r') as f:
            self.assertEqual(f.readline().strip(), 'Test stderr redirection')

    def tearDown(self):
        try:
            os.remove('test_stdout.txt')
            os.remove('test_stderr.txt')
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()
    # with open('test_results.txt', 'a') as test_file_stream:
    #     runner = unittest.TextTestRunner(stream=test_file_stream)
    #     unittest.main(testRunner=runner)
