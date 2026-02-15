import unittest
from file_path_builder import build_path

class TestFilePathBuilder(unittest.TestCase):
    def test_path_with_slash(self):
        self.assertEqual(build_path("/home/user/", "doc.txt"), "/home/user/doc.txt")

if __name__ == '__main__':
    unittest.main()