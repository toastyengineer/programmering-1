"""
Run unittest on calc2.py
"""

import unittest
from calc2 import addition, subtraction, multiplication, division, average


class TestSuite(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(5, 2), 7)
        self.assertEqual(addition(-3, 4), 1)
        self.assertEqual(addition(1.5, 3.5), 5)

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 3), 2)
        self.assertEqual(subtraction(-5, -10), 5)
        self.assertEqual(subtraction(5.5, -2.5), 8)

    def test_multiplication(self):
        self.assertEqual(multiplication(5, 4), 20)
        self.assertEqual(multiplication(-3, -3), 9)
        self.assertEqual(multiplication(2.5, -5), -12.5)

    def test_division(self):
        self.assertEqual(division(10, 4), 2.5)
        self.assertEqual(division(-10, 2), -5)
        self.assertEqual(division(5, 0), "Error")

    def test_average(self):
        self.assertEqual(average(4, 5), 4.5)
        self.assertEqual(average(-5, 5), 0)
        self.assertEqual(average(-5, -10), -7.5)


if __name__ == "__main__":
    unittest.main()
