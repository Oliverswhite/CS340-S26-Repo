import unittest
from discount_applier import apply_discount

class TestDiscountApplier(unittest.TestCase):
    def test_fifty_percent_discount(self):
        self.assertEqual(apply_discount(100, 0.5), 50.0)

if __name__ == '__main__':
    unittest.main()