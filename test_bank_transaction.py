import unittest
from bank_transaction import withdraw

class TestBankTransaction(unittest.TestCase):
    def test_valid_withdrawal(self):
        self.assertEqual(withdraw(100, 40), 60)

    def test_insufficient_funds(self):
        with self.assertRaises(ValueError):
            withdraw(50, 100)

if __name__ == '__main__':
    unittest.main()