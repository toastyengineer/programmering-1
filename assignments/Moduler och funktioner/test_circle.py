""" test_circle
Run unittest on circle.py
"""
import unittest
from math import pi
from circle import area, circ


class TestSuite(unittest.TestCase):
    """ Tests for each of the functions in circle.py """
    def test_area(self):
        """testing parameters for area function"""
        self.assertEqual(area(5), pi * 5 ** 2)
        self.assertEqual(area(-6), pi * 6 ** 2)
        self.assertEqual(area(15.2), pi * 15.2 ** 2)
        self.assertEqual(area("hello"), "Error: TypeError")

    def test_circumference(self):
        """testing parameters for circ function"""
        self.assertEqual(circ(5), 2 * pi * 5)
        self.assertEqual(circ(-5), 2 * pi * 5)
        self.assertEqual(circ(5.5), 2 * pi * 5.5)
        self.assertEqual(circ("hello"), "Error: TypeError")


if __name__ == "__main__":
    unittest.main()
