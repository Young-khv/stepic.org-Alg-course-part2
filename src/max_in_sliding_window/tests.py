import unittest
import solution


class MaxInSlidingWindowTests(unittest.TestCase):
    def test_for_eight_items_and_win_length_four(self):
        line = '2 7 3 1 5 2 6 2'
        w_size = 4
        expected = [7, 7, 5, 6, 6]
        result = solution.get_maxs_for_windows(line, w_size)
        self.assertEqual(expected, result)

    def test_for_15_items_and_win_length_7(self):
        line = '73 65 24 14 44 20 65 97 27 6 42 1 6 41 16 '
        w_size = 7
        expected = [73, 97, 97, 97, 97, 97, 97, 97, 42]
        result = solution.get_maxs_for_windows(line, w_size)
        self.assertEqual(expected, result)
