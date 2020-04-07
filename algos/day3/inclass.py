# Given a string that contains a filepath, with special characters '.' and '..'
# implement a function that resolves this string to the appropriate filepath without the '.' and '..' characters
# '.' -> current
# '..' -> parent

# Use a stack
# pop if '..'
# Using a doubly-linked list

from prework import Stack

def resolve_path(path):

    tokens = path.split('/')
    # handle edge case of '/../']
    if path.replace('/', '') == '..':
        return '/'

    # Else use a Stack
    s = Stack()

    for token in tokens:
        if token == '..':
            s.pop()
        elif token != '.':
            s.push(token)
        else:
            continue

    # The rest of this just prints the correct string
    result = []

    while not s.is_empty():
        result.append(s.pop())

    return '/'.join(result[::-1])

print(resolve_path('/a/b/c/../.'))
print(resolve_path('/../'))