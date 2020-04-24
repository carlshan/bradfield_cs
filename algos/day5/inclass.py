"""
I was not able to attend this class, but I watched the recording the next night.

Induction:
* Instead of recursing to the base case, check that it works for the recursive case
* Then also check for the base case
"""

def int_sq_root(n):
    # n is a perfect square
    # return the square root without calling the sqroot library function
    for i in range(1, n // 2):
        attempt = i * i # this will lead to an overflow of some kind for large n
        if attempt == n:
            return i


def int_sq_root2(n):
    midpoint = n // 2
    prev = 1
    while True:
        print(midpoint)
        attempt = midpoint * midpoint
        if attempt == n:
            break
        elif attempt >= n:
            prev = midpoint
            midpoint = midpoint // 2
        else:
            half = (prev - midpoint) // 2
            prev = midpoint
            midpoint = midpoint + half
    return midpoint

# print(int_sq_root2(25))

def int_sq_root3(n):
    lo = 1
    hi = n

    # handling edge case
    if n <= 1:
        return 1

    while hi - lo > 1: # while they are right next to each other
        mid = (hi + lo) // 2
        if mid * mid >= n:
            hi = mid
        else:
            lo = mid

    return hi

print(int_sq_root3(100))

# First occurrence of a value

def first_occurr(array, n):
    # question: array[i] >= n ?
    lo = 0
    hi = len(array) - 1

    while hi - lo > 1:
        mid = (hi + lo) // 2
        if array[mid] >= n:
            hi = mid
        else:
            lo = mid

    if array[hi] != n:
        return -1

    return hi

l = [1,2,3,5,8,8,8,9, 10]
print(first_occurr(l, 1))