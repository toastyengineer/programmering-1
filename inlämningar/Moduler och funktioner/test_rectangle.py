""" test_rectangle
Run unittest on rectangle.py
"""

import unittest
from rectangle import area, circ


class TestSuite(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5, 2), 10)
        self.assertEqual(area(-3, 4), 12)
        self.assertEqual(area(1.5, 3.5), 5.25)
        self.assertEqual(area("hello", 3), "Error: TypeError")

    def test_circ(self):
        self.assertEqual(circ(5, 3), 16)
        self.assertEqual(circ(-5, -10), 30)
        self.assertEqual(circ(5.5, -2.5), 16)
        self.assertEqual(circ(6, "hello"), "Error: TypeError")


if __name__ == "__main__":
    unittest.main()
