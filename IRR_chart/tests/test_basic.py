import unittest

class BasicTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
