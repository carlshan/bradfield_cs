"""
Practicing using DP to solve algorithmic problems with a recursive structure.
Using questions from: https://atcoder.jp/contests/dp/tasks/dp_a

Other resources:
1. Slides on DP: https://web.stanford.edu/class/cs97si/04-dynamic-programming.pdf
2. Progressively hard questions: https://web.stanford.edu/class/cs97si/assn4.html
3. 31-page chapter from textbook: https://people.eecs.berkeley.edu/~vazirani/algorithms/chap6.pdf
"""

"""
PROBLEM 1:

There are N stones, numbered 1, 2, ... , N.

For each i, the height of stone i is h_i.

There is a frog who is initially on Stone 1. He will repeat the following action some number
of times to reach stone N:

* if the frog is currently on stone i, jump to either stone i + 1 or stone i + 2.
    * here, a cost of |h_i - h_j| is incurred, where j is the stone the frog lands on.

Given N and an array of heights, find the _minimum_ possible total cost incurred before 
the frog reaches stone N.

Constraints:
* 2 <= N <= 10^5
* 1 <= h_i <= 10^4
"""

test1_N = 4
test1_heights = [10, 30, 40, 20]
test1_answer = 30

test2_N = 2
test2_heights = [10, 10]
test2_answer = 0

test3_N = 6
test3_heights = [30, 10, 60, 10, 60, 50]
test3_answer = 40

# Let's apply each step:
"""
# Step 1: Define the sub-problems 

Let C_n = the minimum cost of getting to stone N with heights {h_1, ..., h_N}

# Step 2: Find the recurrance pattern.
Well, if the frog jumped over one, then the C_n = | h_i - h_{i+1} | + C_{n-1} with the remaining heights
And if the frog jumped over two, then it would be: C_n = | h_i - h_{i+1} | + C_{n-2}

The minimum between these two is the jump the frog should make.

# Step 3: Find and solve the base cases.

If N = 2, then C_n = | h_i - h_2 | <- can only make one jump
If N = 1, then C_n = 0 <- do not need to jump


"""

N = input() 
heights = input()

N = int(N)
heights = list(map(int, heights.split(' ')))


def solve_problem_recursive(N, heights):
    memory = {}

    def minimum_cost(N, heights):
        """
            This is the immediate recursive solution I have in my head without
            thinking about any DP.

            I memoize to increase runtime as well.
        """
        mem_key = str(N) + str(heights)
        if mem_key in memory: return memory[mem_key]
        if N == 1:
            return 0
        elif N == 2:
            return abs(heights[0] - heights[1])

        jump_one_cost = abs(heights[0] - heights[1]) + minimum_cost(N-1, heights[1:])
        jump_two_cost = abs(heights[0] - heights[2]) + minimum_cost(N-2, heights[2:])

        best_cost = min(jump_one_cost, jump_two_cost)
        memory[mem_key] = best_cost
        return best_cost
    
    return minimum_cost(N, heights)


def solve_problem_dp(N, heights):
    """
        I came to this solution after noodling for a little bit with a pen and paper.
        The key insight was to create an array holding costs, and to use that to 
        calculate future costs.

        The best cost of jumping to stone i =
            min(
                 best cost jumping from 1 stone before
                , best cost jumping from 2 stones before
                )
        And each of those costs resolve into the recursive definitions I discovered in applying the 3 step
        strategies:

        Well, if the frog jumped over one, then the C_n = | h_i - h_{i+1} | + C_{n-1} with the remaining heights
        And if the frog jumped over two, then it would be: C_n = | h_i - h_{i+1} | + C_{n-2}

        The minimum between these two is the jump the frog should make.
    
        I think the key insight here is to not think from "ending up on the last stone" but rather
        thinking "linearly" and jumping and always making "the best move" and keeping track
        of the best possible cost of ending up on the current stone.
    """
    if N == 1:
        return 0
    elif N == 2:
        return abs(heights[0] - heights[1])
    costs = [0] * len(heights)
    costs[1] = abs(heights[0] - heights[1])

    for i in range(2, len(heights)):
        cost_jump1 = abs(heights[i] - heights[i-1]) + costs[i-1]
        cost_jump2 = abs(heights[i] - heights[i-2]) + costs[i-2] 
        best_cost = min(cost_jump1, cost_jump2)
        costs[i] = best_cost
    
    return costs[-1]


print(solve_problem_dp(N, heights))
