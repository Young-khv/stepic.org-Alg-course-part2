from unittest import TestCase
from solution import MinHeap


class MinHeapTests(TestCase):
    def test_number_of_swaps_1(self):
        arr = [7, 6, 5, 4, 3, 2]
        heap = MinHeap(arr)
        self.assertEqual(4, heap.swap_count)

    def test_swaps_1(self):
        arr = [7, 6, 5, 4, 3, 2]
        heap = MinHeap(arr)
        expected_swaps = [
            '2 5',
            '1 4',
            '0 2',
            '2 5'
        ]
        self.assertEqual(expected_swaps, heap.swaps)

    def test_number_of_swaps_2(self):
        arr = [5, 4, 3, 2, 1]
        heap = MinHeap(arr)
        self.assertEqual(3, heap.swap_count)

    def test_swaps_2(self):
        arr = [5, 4, 3, 2, 1]
        heap = MinHeap(arr)
        expected_swaps = [
            '1 4',
            '0 1',
            '1 3'
        ]
        self.assertEqual(expected_swaps, heap.swaps)

    def test_heap_without_swaps(self):
        arr = [1, 2, 3, 4, 5]
        heap = MinHeap(arr)
        self.assertEqual(0, heap.swap_count)
