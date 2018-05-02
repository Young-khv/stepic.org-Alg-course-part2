_brackets = {
    '}': '{',
    ']': '[',
    ')': '('
}

_success_result = 'Success'


def check_sequence(line):
    stack = []
    open_brackets_indexes = []
    for idx, item in enumerate(line):
        if item not in ['{', '}', '[', ']', '(', ')']:
            continue
        if item in _brackets:
            if len(stack) == 0:
                return idx + 1
            else:
                last_added = stack.pop()
                if last_added != _brackets[item]:
                    return idx + 1
                else:
                    open_brackets_indexes.pop()
        else:
            stack.append(item)
            open_brackets_indexes.append(idx + 1)

    if len(stack) == 0:
        return _success_result
    else:
        return open_brackets_indexes.pop()


'''
This line is needed to pass solution to stepic.org test engine
Commented for running local unit tests
'''
#print(check_sequence(input()))
