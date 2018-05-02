import unittest
import solution


class TreeHeightTests(unittest.TestCase):
    def test_should_return_3(self):
        line = '4 -1 4 1 1'
        n = 5
        result = solution.get_tree_height(n, line)
        self.assertEqual(result, 3)

    def test_should_return_4(self):
        line = '9 7 5 5 2 9 9 9 2 -1'
        n = 10
        result = solution.get_tree_height(n, line)
        self.assertEqual(result, 4)

