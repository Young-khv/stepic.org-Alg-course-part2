class StackWithMax:
    maxs = [None] * 10000000

    m_idx = 0

    def maxs_append(self, item):
        self.maxs[self.m_idx] = item
        self.m_idx += 1

    def push(self, item):
        if self.m_idx == 0:
            self.maxs_append(item)
        else:
            self.maxs_append(max(item, self.maxs[self.m_idx - 1]))

    def pop(self):
        self.m_idx -= 1

    def max(self):
        return self.maxs[self.m_idx - 1]


'''
Those lines are needed to pass solution to stepic.org test engine
Commented for running local unit tests
'''
# n = int(input())
# stack = StackWithMax()
# for i in range(n):
#     line = input()
#     if line == 'max':
#         print(stack.max())
#     elif line == 'pop':
#         stack.pop()
#     else:
#         stack.push(int(line[5:]))
