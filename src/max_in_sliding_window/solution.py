from collections import deque


class StackWithMax:
    maxs = []

    def push(self, item):
        if len(self.maxs) == 0:
            self.maxs.append(item)
        else:
            self.maxs.append(max(item, self.maxs[-1]))

    def pop(self):
        return self.maxs.pop()

    def max(self):
        return self.maxs[-1]


class Queue:
    in_stack = deque()
    out_stack = StackWithMax()
    in_max = -999999

    def reset_in_max(self):
        self.in_max = -999999

    def enqueue(self, item):
        self.in_max = max(item, self.in_max)
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack.maxs:
            while self.in_stack:
                self.out_stack.push(self.in_stack.pop())
            self.reset_in_max()
            return self.out_stack.pop()
        if not self.in_stack:
            return self.out_stack.pop()

        if self.in_max > self.out_stack.max():
            self.out_stack.pop()
            return self.in_max
        return self.out_stack.pop()


def get_maxs_for_windows(line_items, w_size):
    strings = line_items.split()
    items = list(map(lambda x: int(x), strings))
    result = []
    queue = Queue()
    for i in range(w_size):
        queue.enqueue(items[i])
    result.append(queue.dequeue())

    for i in items[w_size:]:
        queue.enqueue(i)
        result.append(queue.dequeue())
    return result


'''
Those lines are needed to pass solution to stepic.org test engine
Commented for running local unit tests
'''
# n = input()
# line = input()
# size = int(input())
# result = get_maxs_for_windows(line, size)
# print(' '.join('{}'.format(r) for r in result))
