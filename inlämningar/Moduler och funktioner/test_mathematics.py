""" test_mathematics
Run unittest on mathematics.py
"""

import unittest
from mathematics import add, sub, mul, div


class TestSuite(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(5, 2), 7)
        self.assertEqual(add(-3, 4), 1)
        self.assertEqual(add(1.5, 3.5), 5)
        self.assertEqual(add("hello", 0), "Error: TypeError")
        self.assertEqual(add(5, "hello"), "Error: TypeError")

    def test_subtraction(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(-5, -10), 5)
        self.assertEqual(sub(5.5, -2.5), 8)
        self.assertEqual(sub("hello", 0), "Error: TypeError")
        self.assertEqual(sub(5, "hello"), "Error: TypeError")

    def test_multiplication(self):
        self.assertEqual(mul(5, 4), 20)
        self.assertEqual(mul(-3, -3), 9)
        self.assertEqual(mul(2.5, -5), -12.5)
        self.assertEqual(mul("hello", 0), "Error: TypeError")
        self.assertEqual(mul(5, "hello"), "Error: TypeError")

    def test_division(self):
        self.assertEqual(div(10, 4), 2.5)
        self.assertEqual(div(-10, 2), -5)
        self.assertEqual(div(5, 0), "Error: ZeroDivisionError")
        self.assertEqual(div("hello", 0), "Error: TypeError")
        self.assertEqual(div(5, "hello"), "Error: TypeError")


if __name__ == "__main__":
    unittest.main()
