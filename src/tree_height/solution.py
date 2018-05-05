heights = {-1: 1}


def get_tree_height(n, line):
    if n == 1:
        return 1

    strings = line.split()
    items = list(map(lambda x: int(x), strings))
    result = 1
    for l in items:
        leaf_height = get_height_for_leaf(items, l)
        if leaf_height > result:
            result = leaf_height

    return result


def get_height_for_leaf(items, leaf):
    if leaf in heights:
        return heights[leaf]
    height = get_height_for_leaf(items, items[leaf]) + 1
    heights[leaf] = height
    return height


'''
Those lines are needed to pass solution to stepic.org test engine
Commented for running local unit tests
'''
# n = input()
# line = input()
# print(get_tree_height(n, line))
