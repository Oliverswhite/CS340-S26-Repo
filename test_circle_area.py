import unittest
from circle_area import calculate_area

class TestCircleArea(unittest.TestCase):
    def test_radius_two(self):
        self.assertAlmostEqual(calculate_area(2), 12.56)

if __name__ == '__main__':
    unittest.main()