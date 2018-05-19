from queue import PriorityQueue


class Process:
    def __init__(self, start, duration):
        self.start = start
        self.duration = duration
        self.end = start + duration

    def __gt__(self, other):
        return self.start > other.start


def calculate_packages_handling_start(n, items_line):
    queue = PriorityQueue()
    result = []
    items = list(map(lambda x: int(x), items_line.split()))
    for pr_idx, duration in enumerate(items[:n]):
        pr = Process(0, duration)
        queue.put((pr, pr_idx))
    for duration in items[n:]:
        item = queue.get()
        pr_idx = item[1]
        prev_pr = item[0]
        result.append((pr_idx, prev_pr.start))
        pr = Process(prev_pr.end, duration)
        queue.put((pr, pr_idx))
    while not queue.empty():
        item = queue.get()
        result.append((item[1], item[0].start))
    return result

'''
This line is needed to pass solution to stepic.org test engine
Commented for running local unit tests
'''
#print(check_sequence(input()))
