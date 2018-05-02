def get_tree_height(n, line):
    if n == 1:
        return 1

    strings = line.split()
    items = list(map(lambda x: int(x), strings))
    root = items.index(-1)
    return get_subtree_height(items, 1, root)


def get_subtree_height(items, curr_height, leaf):
    subtree = [i for i, x in enumerate(items) if x == leaf]
    if len(subtree) == 0:
        return curr_height
    heights = []
    for l in subtree:
        heights.append(get_subtree_height(items, curr_height + 1, l))
    return max(heights)


'''
Those lines are needed to pass solution to stepic.org test engine
Commented for running local unit tests
'''
# input()
# line = input()
# print(get_tree_height(line))
