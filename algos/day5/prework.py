"""
Topic: Binary Search
Read: https://bradfieldcs.com/algos/searching/the-binary-search/
While reading, consider:

    1. Hashing and binary search both address the same problem: finding an item in a collection. What are some trade-offs between the two strategies? When might you want to pick one over the other?
    2. If sorting takes (at minimum) O(n log n) time, and binary search takes O(log n) time, under what circumstances might it worth it to sort a collection in order to perform binary search?

1. Some comparisons and contrasts between hashing and binary seaching:
   * With hashing, you can lookup objects that don't have some natural "ordering" like numbers do, whereas for binary search to work there needs to be some definition of an "order" so that you compare "greater" or "less than."
   * If the cost of sorting $N$ items is heavier than just hashing all items, you may just want to go with hashing.
   * Vice versa. If it is computationally expensive to hash certain items (maybe long strings?) then sorting may be better.
   * For binary search, once you've sorted you can use it for other purposes and build other data structures that may rely on sorted data.
   * If you sort in place, you don't use additional memory, unlike with hashing.
2. If we expect to amortize the cost of $O(nlog_{2}n)$ sort over many fast $O(log_{2}n)$ searches, we may be okay sorting the collection in order to perform binary search. Similarly if future tasks may require sorting the data.

Then, write some code that conducts binary search.
"""

def binary_search(numbers, start, stop, N):
    """
    Returns True if N is in numbers, start, stop,else False.

    Params:
        numbers: sorted array of integers ascending
        N: int
    """
    if stop == start:
        # Empty array
        return False

    midpoint = (stop - start) // 2
    if numbers[start + midpoint] == N:
        return True

    else:
        if N > numbers[start + midpoint]: # toss bottom half and search top half
            return binary_search(numbers=numbers, start=start + midpoint + 1, stop=stop, N=N)
        else: # toss top half and seach bottom half
            return binary_search(numbers=numbers, start=start, stop=start + midpoint, N=N)

numbers = [1, 2, 3, 4]
N = 4
start = 0
stop = len(numbers)
# Returns True
print(binary_search(numbers, start, stop, N))
print(binary_search(numbers, start, stop, 1))
print(binary_search(numbers, start, stop, 2))
print(binary_search(numbers, start, stop, 3))

# Returns False
print(binary_search(numbers, start, stop, 5))
print(binary_search(numbers, start, stop, 0))
print(binary_search([], start, 0, 3))