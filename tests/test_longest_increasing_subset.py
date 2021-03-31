import unittest
from leet_code_grind import longest_increasing_subset


class MyTestCase(unittest.TestCase):
    def test_basic_fn(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        ans = 4
        self.assertEqual(longest_increasing_subset.lengthOfLIS(None, nums),
                         ans)

    def test_basic_fn1(self):
        nums = [0, 1, 0, 3, 2, 3]
        ans = 4
        self.assertEqual(longest_increasing_subset.lengthOfLIS(None, nums),
                         ans)

    def test_basic_fn2(self):
        nums = [10, 5, 8, 3, 9, 4, 12, 11]
        ans = 4
        self.assertEqual(longest_increasing_subset.lengthOfLIS(None, nums),
                         ans)


if __name__ == '__main__':
    unittest.main()
