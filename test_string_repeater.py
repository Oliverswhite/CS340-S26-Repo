import unittest
from string_repeater import repeat_string

class TestStringRepeater(unittest.TestCase):
    def test_repeat_positive(self):
        self.assertEqual(repeat_string("ha", 3), "hahaha")

    def test_repeat_zero(self):
        self.assertEqual(repeat_string("ha", 0), "")

if __name__ == '__main__':
    unittest.main()