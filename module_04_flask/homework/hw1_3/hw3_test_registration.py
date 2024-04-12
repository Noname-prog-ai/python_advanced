"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from hw1_registration import app

class TestRegistrationEndpoint(unittest.TestCase):

    def test_username_validator(self):
        # Проверяем, что валидатор для имени пользователя работает правильно
        valid_usernames = ["john_doe", "jane.smith", "user123"]
        invalid_usernames = ["john doe", "jane$smith", "user..123"]

        for username in valid_usernames:
            response = app.test_client().post('/registration', data={'username': username})
            self.assertEqual(response.status_code, 200)

        for username in invalid_usernames:
            response = app.test_client().post('/registration', data={'username': username})
            self.assertEqual(response.status_code, 400)

    def test_email_validator(self):
        # Проверяем, что валидатор для email адреса работает правильно
        valid_emails = ["john.doe@example.com", "jane.smith123@example.co.uk", "user_123@mail.ru"]
        invalid_emails = ["john.doe@example", "jane.smith@.com", "user@mail@ru"]

        for email in valid_emails:
            response = app.test_client().post('/registration', data={'email': email})
            self.assertEqual(response.status_code, 200)

        for email in invalid_emails:
            response = app.test_client().post('/registration', data={'email': email})
            self.assertEqual(response.status_code, 400)

    def test_password_validator(self):
        # Проверяем, что валидатор для пароля работает правильно
        valid_passwords = ["StrongPassword123", "SecurePwd!234", "Pa$$w0rd"]
        invalid_passwords = ["weakpassword", "123456", "password"]

        for password in valid_passwords:
            response = app.test_client().post('/registration', data={'password': password})
            self.assertEqual(response.status_code, 200)

        for password in invalid_passwords:
            response = app.test_client().post('/registration', data={'password': password})
            self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
