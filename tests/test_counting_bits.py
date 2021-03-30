import unittest
from leet_code_grind import counting_bits


class MyTestCase(unittest.TestCase):
    def test_basic_fn(self):
        num = 2
        ans = [0, 1, 1]
        self.assertEqual(counting_bits.count_bits(None, num), ans)

    def test_basic_fn1(self):
        num = 5
        ans = [0, 1, 1, 2, 1, 2]
        self.assertEqual(counting_bits.count_bits(None, num), ans)


if __name__ == '__main__':
    unittest.main()
