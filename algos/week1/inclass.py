"""
Given a number n, how many ways can you find a series that sums to n if all elements of that series has to be the number 1 or 2

A series is unique if it contains a unique set of 1s and 2s.

Example:
n = 0
There are 1 ways

n = 1 
There is 1 way (1)

n = 2
There are 2 ways (1 + 1) or (2)

n = 3
There are 3 ways (1 + 1 + 1) or (2 + 1) or (1 + 2)

n = 4
There are 5 ways (1 + 1 + 1 + 1) or (1 + 2 + 1) or (1 + 1 + 2) or (2 + 2) or (2 + 1 + 1)

-- Put down a 1 and then add n=3
-- Put down a 2 and then add n=2

Should be equal to 3 + 2 = 5 solutions

n = 5
Maybe 8 ways?

Problem solving approaches (meta):
1. Find a pattern by hand
2. Draw and then just try stuff until I notice something
3. Reduce to a similar problem 
4. Try small cases

"""



# Recursively:
# the number of ways you can build up to n is equal to you can build up to (n - 1) plus the number of ways you can build up to (n - 2) 
# this sounds like the staircase problem.
# But this assumes that it's the unique set of numbers that matters rather than the order of numbers.

# There are branches:
# Branch #1. Put down a blue tile (=1) 
# Branch #2. Put down a red tile (=2) 
# and recursively run this same algorithm on the remaining tiles for both branches
# Sum up the results.

# 

def sum_to_n(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    
    else: 
        return sum_to_n(n-1) + sum_to_n(n-2)

print(sum_to_n(6))

