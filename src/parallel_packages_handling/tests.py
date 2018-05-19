from unittest import TestCase
import solution


class ParallelPackagesHandlingTests(TestCase):
    def test_for_2_processors(self):
        n = 2
        items = '1 2 3 4 5'
        expected = [
            (0, 0),
            (1, 0),
            (0, 1),
            (1, 2),
            (0, 4)
        ]
        result = solution.calculate_packages_handling_start(n, items)
        self.assertEqual(expected, result)

    def test_for_4_processors(self):
        n = 4
        items = '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1'
        expected = [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (0, 1),
            (1, 1),
            (2, 1),
            (3, 1),
            (0, 2),
            (1, 2),
            (2, 2),
            (3, 2),
            (0, 3),
            (1, 3),
            (2, 3),
            (3, 3),
            (0, 4),
            (1, 4),
            (2, 4),
            (3, 4)
        ]
        result = solution.calculate_packages_handling_start(n, items)
        self.assertEqual(expected, result)
