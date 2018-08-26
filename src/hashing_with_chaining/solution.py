import collections


class CustomDict:
    _p = 1000000007
    _x = 263
    _x_pows = list([1])

    table = None

    def __init__(self, n):
        self.table = [None] * n

    def get_mod(self, num):
        return num % self._p

    def get_pow(self, idx):
        if len(self._x_pows) >= idx + 1:
            return self._x_pows[idx]

        result = self.get_mod(self._x) * self.get_mod(self._x_pows[idx - 1])
        self._x_pows.append(result)
        return result

    def get_hash(self, s):
        result = 0
        for idx, c in enumerate(s):
            result += self.get_mod(ord(c)) * self.get_mod(self.get_pow(idx))
        return self.get_mod(result) % len(self.table)

    def add_val(self, s):
        h = self.get_hash(s)
        if self.table[h] is None:
            self.table[h] = collections.deque([s])
        else:
            self.table[h].appendleft(s)

    def del_val(self, s):
        h = self.get_hash(s)
        if self.table[h] is not None and s in self.table[h]:
            self.table[h].remove(s)

    def find_val(self, s):
        h = self.get_hash(s)
        if self.table[h] is not None and s in self.table[h]:
            return "yes"
        return "no"

    def check_list(self, i):
        if self.table[i] is not None and len(self.table[i]) > 0:
            return " ".join(self.table[i])
        return ""

'''
Those lines are needed to pass solution to stepic.org test engine
Commented for running local unit tests
'''
n = int(input())
operations = int(input())
h = CustomDict(n)
for i in range(operations):
    cmd = input().split()
    if cmd[0] == "add":
        h.add_val(cmd[1])
    elif cmd[0] == "find":
        print(h.find_val(cmd[1]))
    elif cmd[0] == "del":
        h.del_val(cmd[1])
    elif cmd[0] == "check":
        print(h.check_list(int(cmd[1])))
    else:
        print("WTF")

