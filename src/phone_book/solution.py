class PhoneBook:
    p_book = dict()
    _not_found = "not found"

    def add_number(self, number, name):
        self.p_book[number] = name

    def del_number(self, number):
        if number in self.p_book:
            del self.p_book[number]

    def find_name(self, number):
        if number in self.p_book:
            return self.p_book[number]
        return self._not_found





'''
Those lines are needed to pass solution to stepic.org test engine
Commented for running local unit tests
'''
n = input()
p_book = PhoneBook()
for i in range(int(n)):
    cmd = input().split()
    if cmd[0] == "add":
        p_book.add_number(cmd[1], cmd[2])
    elif cmd[0] == "find":
        print(p_book.find_name(cmd[1]))
    elif cmd[0] == "del":
        p_book.del_number(cmd[1])
    else:
        print("WTF")

