from unittest import TestCase
import solution


class CorrectBracketSequenceTests(TestCase):
    def test_should_return_success_for_correct_empty_sequence(self):
        seq = '(){[]}'
        result = solution.check_sequence(seq)
        self.assertEqual(result, solution._success_result)

    def test_should_return_success_for_correct_not_empty_sequence(self):
        seq = 'foo(bar);'
        result = solution.check_sequence(seq)
        self.assertEqual(result, solution._success_result)

    def test_should_return_idx_2_for_incorrect_empty_sequence(self):
        seq = '(}){[]}'
        result = solution.check_sequence(seq)
        self.assertEqual(result, 2)

    def test_should_return_idx_10_for_incorrect_sequence(self):
        seq = 'foo(bar[i);'
        result = solution.check_sequence(seq)
        self.assertEqual(result, 10)

    def test_should_return_idx_3_for_incorrect_sequence(self):
        seq = '([)'
        result = solution.check_sequence(seq)
        self.solution(result, 3)

    def test_should_return_idx_1_for_incorrect_sequence(self):
        seq = '('
        result = solution.check_sequence(seq)
        self.assertEqual(result, 1)

    def test_should_return_idx_3_for_incorrect_sequence(self):
        seq = '{{{**[][][]'
        result = solution.check_sequence(seq)
        self.assertEqual(result, 3)
