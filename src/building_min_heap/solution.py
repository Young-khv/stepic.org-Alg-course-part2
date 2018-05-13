import math


class MinHeap:
    def __init__(self, list):
        self.swap_count = 0
        self.swaps = []
        self.size = len(list)
        self.items = list
        self.build_min_heap()

    def build_min_heap(self):
        n = int(math.floor((self.size / 2) - 1))
        for i in range(n, -1, -1):
            self.sift_down(i)

    def get_parent_idx(self, idx):
        return int(math.floor((idx - 1) / 2))

    def get_left_child_idx(self, idx):
        i = (2 * idx) + 1
        return i if i < self.size else None

    def get_right_child_idx(self, idx):
        i = (2 * idx) + 2
        return i if i < self.size else None

    def swap(self, idx_1, idx_2):
        self.swap_count += 1
        self.swaps.append("%s %d" % (idx_1, idx_2))
        tmp = self.items[idx_1]
        self.items[idx_1] = self.items[idx_2]
        self.items[idx_2] = tmp

    def sift_up(self, idx):
        while idx > 0 and self.items[self.get_parent_idx(idx)] > self.items[idx]:
            self.swap(idx, self.get_parent_idx(idx))
            idx = self.get_parent_idx(idx)

    def sift_down(self, idx):
        max_idx = idx
        l = self.get_left_child_idx(idx)
        if l is not None and self.items[l] < self.items[idx]:
            max_idx = l
        r = self.get_right_child_idx(idx)
        if r is not None and self.items[r] < self.items[max_idx]:
            max_idx = r
        if idx != max_idx:
            self.swap(idx, max_idx)
            self.sift_down(max_idx)


'''
This lines are needed to pass solution to stepic.org test engine
Commented for running local unit tests
'''
# n = input()
# strings = input().split()
# items = list(map(lambda x: int(x), strings))
# heap = MinHeap(items)
# print(heap.swap_count)
# for s in heap.swaps:
#     print(s)
