"""
Prework:
* Read sections 1-5 of the text on Recursion: https://bradfieldcs.com/algos/recursion/introduction/
"""


def recursive_sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] + recursive_sum(numbers[1:])

# print(recursive_sum([1,2,3,4]))

char_for_int = '01'
def convert_base(number, base):
    """
    Converts a number in base 10 to base 2 (binary)
    """
    if number < base:
        return char_for_int[number]
    
    else:
        return convert_base(number // base, base) + char_for_int[number % base]
    
# print(convert_base(5, 2))

# Given a lattice of height h and width w, how many unique shortest paths exist from the top left corner to the bottom right corner?
# for h=w=2, there are 6 unique paths.

def num_shortest_paths(h, w):
    if h == 1 or w == 1:
        # base case: only one path
        return 1
    
    else:
        return num_shortest_paths(h-1, w) + num_shortest_paths(h, w-1)

print(num_shortest_paths(3, 3))