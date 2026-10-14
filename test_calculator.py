
import unittest
from calculator import add, subtract, multiply


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)

    def test_subtract(self):
        self.assertEqual(subtract(20, 10), 10)

    def test_multiply(self):
        self.assertEqual(multiply(5, 4), 20)


if __name__ == "__main__":
    unittest.main()
