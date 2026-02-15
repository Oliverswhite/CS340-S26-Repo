import unittest
from role_checker import can_access_dashboard

class TestRoleChecker(unittest.TestCase):
    def test_admin_access(self):
        self.assertTrue(can_access_dashboard("admin"))

if __name__ == '__main__':
    unittest.main()