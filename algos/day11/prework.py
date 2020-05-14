"""
Prework is to essentially work through many Dynamic Programming exercises.

I'm going to do a number of problems tagged as Dynamic Programming on Leetcode: https://leetcode.com/tag/dynamic-programming/

"""

# 746 Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
def solve_climbing_stairs(costs):
    """
    On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

    Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor,
    and you can either start from the step with index 0, or the step with index 1.

    Example 1:
    Input: cost = [10, 15, 20]
    Output: 15
    Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

    Example 2:
    Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    Output: 6
    Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

    Note:
    cost will have a length in the range [2, 1000].
    Every cost[i] will be an integer in the range [0, 999].
    """
    min_costs = [0] * len(costs)
    min_costs[0] = costs[0] # I don't understand these two lines.
    min_costs[1] = costs[1]

    for i in range(2, len(costs)):
        min_costs[i] = costs[i] + min(min_costs[i - 1], min_costs[i - 2])

    return min(min_costs[-2:])


print(solve_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))



# 1025. Divisor Game
# https://leetcode.com/problems/divisor-game/
def solve_divisor_game(N):
    """
    Alice and Bob take turns playing a game, with Alice starting first.

    Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

    Choosing any x with 0 < x < N and N % x == 0.
    Replacing the number N on the chalkboard with N - x.
    Also, if a player cannot make a move, they lose the game.

    Return True if and only if Alice wins the game, assuming both players play optimally.

    Examples:
    >> solve_divisor_game(2)
    True

    >> solve_divisor_game(3)
    False
    """
    if N == 2:
        return True
    if N == 3:
        return False
