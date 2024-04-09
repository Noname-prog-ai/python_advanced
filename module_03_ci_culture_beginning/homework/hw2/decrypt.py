import sys
import unittest

def decrypt(encryption: str) -> str:
    result: list = []
    dots: int = 0
    for symbol in encryption:
        if symbol != '.':
            result.append(symbol)
            dots = 0
            continue

        dots += 1
        if dots == 2 and result:
            result.pop()
            dots = 0

    return ''.join(result)

class TestDecrypt(unittest.TestCase):
    def test_decrypt(self):
        self.assertTrue(decrypt("абра-кадабра.") == "абра-кадабра")
        self.assertTrue(decrypt("абраа..-кадабра") == "абра-кадабра")
        self.assertTrue(decrypt("абраа..-.кадабра") == "абра-кадабра")
        self.assertTrue(decrypt("абра--..кадабра") == "абра-кадабра")
        self.assertTrue(decrypt("абрау...-кадабра") == "абра-кадабра")
        self.assertTrue(decrypt("абра........") == "")
        self.assertTrue(decrypt("абр......a.") == "a")
        self.assertTrue(decrypt("1..2.3") == "23")
        self.assertTrue(decrypt(".") == "")
        self.assertTrue(decrypt("1.......................") == "")

if __name__ == '__main__':
    data: str = sys.stdin.read()
    decryption: str = decrypt(data)
    print(decryption)
