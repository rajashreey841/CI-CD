import unittest
from main import add,subtract,multiply,divide

class Testmain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3,2),5)

    def test_subtract(self):
        self.assertEqual(subtract(3,2),1)

    def test_multiply(self):
        self.assertEqual(multiply(3,2),6)

    def test_divide(self):
        self.assertEqual(divide(6,2),3)
        with self.assertRaises(ValueError):
            divide(3,0)

if __name__ == "__main__":
    unittest.main()
