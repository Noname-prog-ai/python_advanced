import unittest

def decrypt(encryption: str) -> str:
    result: list = []
    dots: int = 0
    for symbol in encryption:
        if symbol != '.':
            result.append(symbol)
            dots = 0
            continue

    return ''.join(decrypted)

class TestDecrypt(unittest.TestCase):

    def test_decrypt_dot_skips_next_character(self):
        self.assertEqual(decrypt('a.b.c'), 'abc')

    def test_decrypt_dash_removes_last_character(self):
        self.assertEqual(decrypt('abc-'), 'ab')

    def test_decrypt_multiple_dash_removes_multiple_characters(self):
        self.assertEqual(decrypt('abc-d-e-f-'), 'abc')

    def test_decrypt_dot_and_dash_together(self):
        self.assertEqual(decrypt('a.b-c.'), 'ac')

    def test_decrypt_empty_input_returns_empty_string(self):
        self.assertEqual(decrypt(''), '')

if __name__ == "__main__":
    unittest.main()
