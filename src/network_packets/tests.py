import unittest
import solution


class NetworkPacketsTests(unittest.TestCase):
    def test_should_handle_single_package(self):
        packages = [
            [0, 1],
            [0, 1]
        ]
        result = solution.handle_packages(1, packages)
        expected = [0, -1]
        self.assertEqual(expected, result)

    def test_should_handle_both_packages(self):
        packages = [
            [0, 1],
            [0, 1]
        ]
        result = solution.handle_packages(2, packages)
        expected = [0, 1]
        self.assertEqual(expected, result)

    def test_crossed_packages(self):
        packages = [
            [0, 5],
            [2, 7]
        ]
        result = solution.handle_packages(2, packages)
        expected = [0, 5]
        self.assertEqual(expected, result)

    def test_big_number_of_packages_1(self):
        packages = [
            [16, 0],
            [29, 3],
            [44, 6],
            [58, 0],
            [72, 2],
            [88, 8],
            [95, 7],
            [108, 6],
            [123, 9],
            [139, 6],
            [152, 6],
            [157, 3],
            [169, 3],
            [183, 1],
            [192, 0],
            [202, 8],
            [213, 8],
            [229, 3],
            [232, 3],
            [236, 3],
            [239, 4],
            [247, 8],
            [251, 2],
            [267, 7],
            [275, 7],
        ]
        result = solution.handle_packages(1, packages)
        expected = [
            16,
            29,
            44,
            58,
            72,
            88,
            -1,
            108,
            123,
            139,
            152,
            -1,
            169,
            183,
            192,
            202,
            213,
            229,
            232,
            236,
            239,
            247,
            -1,
            267,
            275
        ]
        self.assertEqual(expected, result)

    def test_big_number_of_packages_2(self):
        packages = [
            [6, 23],
            [15, 44],
            [24, 28],
            [25, 15],
            [33, 7],
            [47, 41],
            [58, 25],
            [65, 5],
            [70, 14],
            [79, 8],
            [93, 43],
            [103, 11],
            [110, 25],
            [123, 27],
            [138, 40],
            [144, 19],
            [159, 2],
            [167, 23],
            [179, 43],
            [182, 31],
            [186, 7],
            [198, 16],
            [208, 41],
            [222, 23],
            [235, 26]
        ]
        result = solution.handle_packages(11, packages)
        expected = [
            6,
            29,
            73,
            101,
            116,
            123,
            164,
            189,
            194,
            208,
            216,
            259,
            270,
            295,
            322,
            362,
            -1,
            381,
            -1,
            -1,
            -1,
            404,
            420,
            461,
            484
        ]
        self.assertEqual(expected, result)

    def test_big_number_of_packages_3(self):
        packages = [
            [10, 37],
            [20, 45],
            [29, 24],
            [31, 17],
            [38, 43],
            [49, 30],
            [59, 12],
            [72, 28],
            [82, 45],
            [91, 10],
            [107, 46],
            [113, 4],
            [128, 16],
            [139, 1],
            [149, 41],
            [163, 0],
            [172, 22],
            [185, 1],
            [191, 17],
            [201, 3],
            [209, 11],
            [223, 30],
            [236, 17],
            [252, 42],
            [262, 0]
        ]
        result = solution.handle_packages(13, packages)
        expected = [
            10,
            47,
            92,
            116,
            133,
            176,
            206,
            218,
            246,
            291,
            301,
            347,
            351,
            367,
            368,
            409,
            409,
            431,
            -1,
            -1,
            432,
            443,
            -1,
            473,
            -1
        ]
        self.assertEqual(expected, result)
