""" test_circle
Run unittest on circle.py
"""

import unittest
from math import pi
from circle import area, circ


class TestSuite(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5), pi * 5 ** 2)
        self.assertEqual(area(-6), pi * 6 ** 2)
        self.assertEqual(area(15.2), pi * 15.2 ** 2)

    def test_circumference(self):
        self.assertEqual(circ(5), 2 * pi * 5)
        self.assertEqual(circ(-5), 2 * pi * 2)
        self.assertEqual(circ(5.5), 2 * pi * 5.5)


if __name__ == "__main__":
    unittest.main()
