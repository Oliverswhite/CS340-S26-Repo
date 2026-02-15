import unittest
from shopping_cart import calculate_total

class TestShoppingCart(unittest.TestCase):
    def test_single_item(self):
        self.assertEqual(calculate_total([15.0]), 15.0)

    def test_empty_cart(self):
        self.assertEqual(calculate_total([]), 0)

if __name__ == '__main__':
    unittest.main()