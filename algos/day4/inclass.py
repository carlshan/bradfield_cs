
"""
Create factorial recursively in two different methods
"""

def factorial1(n):
    if n <= 2: return 1
    else: return n * factorial1(n-1)

# n * (n-1) * ... * 1

def factorial2(n, N):
    if n <= N:
        return n * factorial2(n+1, N)
    else:
        return 1

# print(factorial2(1, 5))

def fact4(n, N, p):
    if n > N:
        return p
    else:
        return fact4(n + 1, N, n * p)

# print(fact4(1, 5, 1))

# Tail recursion: accumulate result and recursive case is just one recursive call, no need to modify it (e.g., *n)
# Tail recursion optimizations: not use the callstack and instead turns it into an iterative problem


# Problem 2
# input: alphabet (e.g., "ABCDE")
# output: all 2 letter combinations ousing that alphabet

def all_twos(alphabet):
    result = []
    for l1 in alphabet:
        for l2 in alphabet:
            result.append(l1 + l2)

    return result

# print(all_twos("ABCDE"))

# Part 2: 
# output: 3 letter words
def all_threes(alphabet):
    result = []
    for l1 in alphabet:
        for l2 in alphabet:
            for l3 in alphabet:
                result.append(l1 + l2 + l3)
    
    return result

# Part 3:
# take in word length as a parameter
def combinations_n(alphabet, length):
    if length == 0:
        return [""]
    
    # recursive case
    # for every letter:
    # create every combination of length - 1, insert it into every position 
    # letter, length - 1
    result = []
    combinations = combinations_n(alphabet, length - 1)

    for letter in alphabet:
        for c in combinations:
            result.append(letter + c)

    return result

result = combinations_n("ABC", 4)
print(result)
print(len(result))