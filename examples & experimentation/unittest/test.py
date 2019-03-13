import unittest
from geometry import rectangle_area
from geometry import rectangle_omkrets
from geometry import rectangle_ratio

class Svit(unittest.TestCase):
    def test_rektangel(self):
        self.assertEqual(rectangle_area(2.0, 3.0), 6.0)
        self.assertEqual(rectangle_area(0.0, 3.0), 0.0)
        self.assertEqual(rectangle_area(-2.0, 3.0), 6.0)

        self.assertEqual(rectangle_omkrets(2.0, 3.0), 10)
        self.assertEqual(rectangle_omkrets(0.0, 3.0), 6)
        self.assertEqual(rectangle_omkrets(-2.0, 3.0), 10)

        self.assertEqual(rectangle_ratio(2.0, 4.0), 0.5)
        self.assertEqual(rectangle_ratio(-2.0, -4.0), 0.5)
        self.assertEqual(rectangle_ratio(0.0, 4.0), 0.0)


if __name__ == '__main__':
    unittest.main()