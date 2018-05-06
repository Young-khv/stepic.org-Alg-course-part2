from collections import deque


def handle_packages(size, packages):
    queue = deque([], size)
    result = []
    for p in packages:
        if not queue:
            add_package_result(p, queue, result, p[0])
        else:
            if p[0] >= queue[-1] or len(queue) < size:
                if p[0] >= queue[0]:
                    add_package_result(p, queue, result,  p[0])
                else:
                    add_package_result(p, queue, result, queue[0])
            else:
                result.append(-1)
    return result


def add_package_result(package, queue, result, delay):
    queue.appendleft(package[1] + delay)
    result.append(max(package[0], delay))


'''
Those lines are needed to pass solution to stepic.org test engine
Commented for running local unit tests
'''
# size, n = input().split()
# packages = []
# for i in range(int(n)):
#     line = input().split()
#     packages.append([int(line[0]), int(line[1])])
#
# result = handle_packages(int(size), packages)
for r in result:
    print(r)
