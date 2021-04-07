import unittest
from leet_code_grind import insert_interval


class MyTestCase(unittest.TestCase):
    def test_basic_fn(self):
        interval = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        new_interval = [4, 8]
        ans = [[1, 2], [3, 10], [12, 16]]
        output = insert_interval.insert(None, interval, new_interval)
        self.assertEqual(ans, output)

    def test_basic_fn1(self):
        interval = [[1, 3], [6, 9]]
        new_interval = [2, 5]
        ans = [[1, 5], [6, 9]]
        output = insert_interval.insert(None, interval, new_interval)
        self.assertEqual(ans, output)

    def test_basic_fn2(self):
        interval = []
        new_interval = [5, 7]
        ans = [[5, 7]]
        output = insert_interval.insert(None, interval, new_interval)
        self.assertEqual(ans, output)

    def test_basic_fn3(self):
        interval = [[1, 5]]
        new_interval = [2, 7]
        ans = [[1, 7]]
        output = insert_interval.insert(None, interval, new_interval)
        self.assertEqual(ans, output)

    def test_failed_fn(self):
        interval = [[1, 5]]
        new_interval = [6, 8]
        ans = [[1, 5], [6, 8]]
        output = insert_interval.insert(None, interval, new_interval)
        self.assertEqual(ans, output)

    def test_failed_fn1(self):
        interval = [[1, 5]]
        new_interval = [0, 0]
        ans = [[0, 0], [1, 5]]
        output = insert_interval.insert(None, interval, new_interval)
        self.assertEqual(ans, output)


if __name__ == '__main__':
    unittest.main()
