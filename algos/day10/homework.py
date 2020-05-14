"""
The homework is to essentially work through a large number of DP exercises.

"""

# 121. Best Time to Buy and Sell Stock I
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Given an input array of stock prices, find the best possible profit:

def max_profit_1(prices):
    max_profit = float('-inf')
    min_price = prices[0]

    for price in prices:
        """
            Keep track of the maximum profit seen so far.
            By also recording the min_price so far.
        """
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit

# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

# Ideas #
Day 1 => Buy
Day 2 => Sell or wait

Profit_i = maximum profit by considering i days of prices

Profit_i = max(
    Option 1: Sell => Profit_{i-1} + potential profit in the future
    Option 2: Wait => Profit_{i-1} + selling in the future
)

"""

def stock2(prices):
    profit = 0

    if len(prices) < 2: # handling edge cases
        return 0

    for i in range(1, len(prices)):
        profit += max(0, prices[i-1] - prices[i])

    return profit

# Problem 309: Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]


# Ideas #
1. What's the recurrence relationship?
Let Profit_n be the maximum profit possible given an array of stock prices [Price_1, ..., Price_n]

Profit_n = max(
    Option 1: Buy today and cooldown tomorrow => Profit_{n-1}
    Option 2: Sell today (if bought before) with at least one cooldown the day before => Profit_{n-2} + sell today
)

2. Base Cases:
* the price list is empty => 0
* the prices list is length 2 => max(buy-sell, 0)
* the prices list is length 3 => max(buy-sell-cooldown, buy-cooldown-sell, cooldown-buy-sell) => two options: buy or cooldown (always ends in a sell or cooldown)
* the prices list is length 4 => max(
                                    buy-sell-cooldown-cooldown,
                                    buy-cooldown-sell-cooldown,
                                    cooldown-buy-sell-cooldown,
                                    buy-cooldown-cooldown-sell,
                                    buy-sell-buy-sell
                                    )

* On any given day i < N, you have the following options:
    * Option 1: if sold >1 day ago, buy
    * Option 2: if bought >= 1 day ago, sell
    * Option 3: do nothing today and maximize profits on the subsequent days

"""

def solve_stock_problem(prices):
    buy, sell = [float('-inf')] * len(prices), [0] * len(prices)
    buy[0] = -prices[0]
    for i in range(1, len(prices)):
        option1 = sell[i - 2] - prices[i] # if we sold with cooldown between selling and buying again
        option2 = buy[i - 1] # take a rest
        buy[i] = max(option1, option2)

        option3 = sell[i - 1] # take a rest
        option4 = buy[i - 1] + prices[i] # we bought at i-1 and we will sell now
        sell[i] = max(option3, option4)

    return sell[-1]


def solve_stock_problem2(prices):
    """
    Optimizing for memory
    """
    if len(prices) < 2:
        return 0

    si1 = 0
    si2 = 0
    bi1 = -prices[0]

    for i in range(1, len(prices)):
        option1 = si2 - prices[i] # if we sold with cooldown between selling and buying again
        option2 = bi1 # take a rest
        bi = max(option1, option2)

        option3 = si1 # take a rest
        option4 = bi1 + prices[i] # we bought at i-1 and we will sell now
        si = max(option3, option4)

        bi1 = bi
        si2 = si1
        si1 = si

    return si


def solve_stock_problem_cooldown(prices):
    """
        Attempting a solution in class.

        Suggestions:
            * Small arrays


    >> solve_stock_problem_cooldown([1,2,3,0,2])
    3

    Things to try:
        * What are tiny inputs we can try with?
        * What are the subproblems?
            - Bought yesterday
            - Sold yesterday
            - Cooldown yesterday
        * How many subproblems are there?
            - 3 * len(prices)
        * How do we keep track of our last state?
            - Actions array
            - Encode the information in some way in the other arrays
        * How do we transition from one state to the other?
            - Bought -> sell or cooldown
            - Sold -> cooldown
            - Cooldown -> Buy or Cooldown
        * What's the base case, if we were to tackle this recursively?
            - Two prices: either buy and sell, or don't buy
            - Empty array or only 1 price = 0
        * What's the recursive case?
            - Max Profit on Day i = max(
                  buy on day i and propagate that to Max Profit on Day i + 1 assuming bought
                , cooldown on day i and propagate that to Max Profit on Day i + 1 assuming cooldown
                , sold on day i and propagate that to Max Profit on Day i + 1 assuming sold
            )
    """

    if len(prices) < 2:
        return 0

    n = len(prices)

    HOLDING = [0] * n
    SOLDING = [0] * n
    COLDING = [0] * n

    HOLDING[0] = -prices[0]
    SOLDING[0] = 0
    COLDING[0] = 0

    for i in range(1, n):
        # Need to own the stock by the end of the day
        HOLDING[i] = max(
            COLDING[i - 1] - prices[i], # sell, cooldown, buy
            HOLDING[i - 1] # continue holding
        )
        SOLDING[i] = HOLDING[i - 1] + prices[i] # sell
        COLDING[i] = max(
            COLDING[i - 1], # action on previous two steps was "cool, cool"
            SOLDING[i - 1]  # action on previous two stepps was "sell, cool"
        )

    print(HOLDING, SOLDING, COLDING)
    return max(HOLDING[n - 1],
                SOLDING[n - 1],
                COLDING[n - 1]
                )

solve_stock_problem_cooldown([1, 5, 2, 10, 12])