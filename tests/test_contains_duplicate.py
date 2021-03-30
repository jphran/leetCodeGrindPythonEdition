import unittest
from leet_code_grind import contains_duplicate


class MyTestCase(unittest.TestCase):
    def test_basic_fn(self):
        nums = [1, 2, 3, 1]
        self.assertTrue(contains_duplicate.contains_duplicate(nums))

    def test_basic_fn1(self):
        nums = [1, 2, 3, 4]
        self.assertFalse(contains_duplicate.contains_duplicate(nums))

    def test_basic_fn2(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertTrue(contains_duplicate.contains_duplicate(nums))


if __name__ == '__main__':
    unittest.main()
