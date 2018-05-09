import unittest
from solution import StackWithMax


class StackWithMaxTests(unittest.TestCase):
    def test_should_return_2_after_both_max_calls(self):
        stack = StackWithMax()
        stack.push(2)
        stack.push(1)
        self.assertEqual(2, stack.max())
        stack.pop()
        self.assertEqual(2, stack.max())

    def test_huge_items_set(self):
        n = 10000000
        stack = StackWithMax()
        for i in range(n):
            stack.push(i)
        self.assertEqual(n - 1, stack.max())
