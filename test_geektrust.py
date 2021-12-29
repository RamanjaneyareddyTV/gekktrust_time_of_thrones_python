import unittest
import Cipher


class TestGeekTrust(unittest.TestCase):

    def setUp(self) -> None:
        self.message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def test_decipher(self):
        
        emblem_decipher = {
            "Gorilla": "TUVWXYZABCDEFGHIJKLMNOPQRS",
            "Panda": "VWXYZABCDEFGHIJKLMNOPQRSTU",
            "Octopus": "TUVWXYZABCDEFGHIJKLMNOPQRS",
            "Mammoth": "TUVWXYZABCDEFGHIJKLMNOPQRS",
            "Owl": "XYZABCDEFGHIJKLMNOPQRSTUVW",
            "Dragon": "UVWXYZABCDEFGHIJKLMNOPQRST",
            "Ox": "YZABCDEFGHIJKLMNOPQRSTUVWX",
            "A": "ZABCDEFGHIJKLMNOPQRSTUVWXY",
            "Bull": "WXYZABCDEFGHIJKLMNOPQRSTUV",
            "Pheasant": "STUVWXYZABCDEFGHIJKLMNOPQR",
            "Alligator": "RSTUVWXYZABCDEFGHIJKLMNOPQ",
            "Chimpanzee": "QRSTUVWXYZABCDEFGHIJKLMNOP",
        }
        for emblem_ in emblem_decipher.keys():
            self.assertEqual(Cipher.decipher(
                self.message, emblem_), emblem_decipher[emblem_])


if __name__ == "__main__":
    unittest.main()