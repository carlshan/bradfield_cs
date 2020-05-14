

## Exercism

# Homework is to go to exercism.io and solve a number of problems, while following the problem-solving process discussed in Polya and in class.

# Problem 1: Knapsack Problem
"""
In this exercise, let's try to solve a classic problem.

Bob is a thief. After months of careful planning, he finally manages to crack the security systems of a high-class apartment.

In front of him are many items, each with a value (v) and weight (w). Bob, of course, wants to maximize the total value he can get;
he would gladly take all of the items if he could. However, to his horror, he realizes that the knapsack he carries with him can only hold so much weight (W).

Given a knapsack with a specific carrying capacity (W), help Bob determine the maximum value he can get from the items in the house. Note that Bob can take only one of each item.

All values given will be strictly positive. Items will be represented as a list of pairs, wi and vi, where the first element wi is the weight of the ith item and vi is the value for that item.

For example:

Items: [ { "weight": 5, "value": 10 }, { "weight": 4, "value": 40 }, { "weight": 6, "value": 30 }, { "weight": 4, "value": 50 } ]

Knapsack Limit: 10

For the above, the first item has weight 5 and value 10, the second item has weight 4 and value 40, and so on.

In this example, Bob should take the second and fourth item to maximize his value, which, in this case, is 90. He cannot get more than 90 as his knapsack has a weight limit of 10.
"""


# Step 1: Understanding the problem:
# > Input = list of dictionaries, each with two keys: weight and value.
# > Output = list of dictionaries such that the sum of the values for 'weight' keys is under the limit and the sum of the values for the 'value' key is the maximum value given the limit.
# > Actually after rereading the problem the output is just the maximum value he can take.

# Step 2: Using different problem-solving approaches
"""
Strategy 1:
* create a list of all values that can be generated by combinations of items (This would be O(n!) unfortunately)
* sort the list from big to small
* now go through this list from big to small and:
    * cross off each combination if the weight exceeds the limit
* stop at the first combination where the weight does not exceed the limit

Other ideas after doodling:
* Calculate the value per weight ratio and take the highest N ones until you exceed the weight limit. I might try this strategy next.
* This smells like a constrainted optimization problem


Strategy 2:
* Calculate the value per weight ratio for all items
* sort by this ratio
* but this runs into the problem when it's actually optimal to take something that has a smaller ratio (e.g,. if the limit was 100 [{"weight": 50, "value": 50}, {"weight": 100, "value": 90}] -- it would be optimal to take the 100 weight one even though it's ratio is lower)

Strategy 3:
Another idea after coming up with Strategy 2:
* there's a recursive / branching solution here: between all options, take the first one and calculate value of remaining



Another idea as I was staring at my notebook:

I could graph (weight, value) coordinates and treat them as vectors. I am trying to maximize value subject to weight sums < limit. I probably could use some strategies
from geometry / vector spaces here (? maybe?).
Add the coordinates / vectors together?
"""

# Strategy No. 3
# I'm going to start by implementing this strategy
import copy

# Reflection:
# This was my first attempt at a recursive solution.
# It took me a little bit of time to realize I had to add the `if weight_limit - item_weight >= 0` condition in the for-loop.
# I also believe this is a O(N!) (yikes!) solution. It doesn't even finish running on 15 items (15! is ~1.3tn)
# My next thoughts are to cache results to speed things up.
def maximum_value_loop(weight_limit, items):
    """
        Returns maximum value given the items

        Algorithm:
            Base cases:
                0. The weight is <= 0, in which case no maximum value can be taken
                1. There is only one item. Then check if it's possible to take it and if so that is the maximum value. Else it's 0.
                2. If there are no items, in which case the maximum value is also 0.
            Recursive case:
                For each item, put it in your bag and see what the maximum value of the remaining items / weight limit are now.
    """

    if weight_limit <= 0:
        return 0

    if len(items) == 0:
        return 0

    if len(items) == 1:
        item = items[0]
        if item['weight'] <= weight_limit:
            return item['value']
        else:
            return 0

    values = [0]

    for item in items:
        item_value = item['value']
        item_weight = item['weight']

        if weight_limit - item_weight >= 0: # checks if we can keep the current item
            copied_items = copy.deepcopy(items)
            copied_items.remove(item)
            # Recursively find the solution if we packed the current item and then all items except the current
            total_value = item_value + maximum_value(weight_limit - item_weight, copied_items)
        else: # this path is a dead end, so move onto the next iteration of the loop
            continue

        values.append(total_value)

    maximum = max(values)
    return maximum


# Day 2:
# I had a few ideas during my morning shower:
# (1) memoize/cache to speed up the previous day's results
# (2) do some sorting/pruning early on in the problem to speed up results
# (3) I recently read Avik Das' description on Dynamic Programming (found on Reddit's r/algorithms) here: https://avikdas.com/2019/04/15/a-graphical-introduction-to-dynamic-programming.html
# After reading it, I want to try grokking the concepts contained within and actually employ it.
# Specifically, it feels like there are deep structural connections between the knapsack problem
# with both the bank robber problem, as well as the change making problem described in the blog post.

"""
Here's some formalism to introduce into the problem to try and make it more concrete:

First, let's sort all items by descending (ascending?) value.

Example:

Items ---  $40 - 5 lbs, $30 - 3 lbs, $20 - 1 lbs, $19 - 3 lbs
Index ---      3      ,     2      ,     1      ,     0

Let k(lim, i) be the maximum value that can be carried with a weight limit of `lim` and considering all items up to the ith item.
So k(5, 2) means to only consider items at positions 0, 1 and 2 with a weight limit of 5.

Then k(lim, i) = max (
    # Option 1: Take the ith item and now consider remaining items
    k(lim - weight_i, i - 1) + value_i

    ,

    # Option 2: Ignore the ith item and only consider remaining items
    k(lim, i-1)
)
"""

def maximum_value(lim, items):
    """
        Returns maximum value.
        Assumes items are sorted by value descending.
    """

    cache = {}
    items.sort(key=lambda item: item['value'], reverse=False) # sorts items in ascending order by value

    def subproblem(lim, i):

        if len(items) == 0:
            return 0

        if lim <= 0:
            return 0

        if (lim, i) in cache: return cache[(lim, i)]

        item = items[i]
        item_weight = item['weight']
        item_value = item['value']

        # Option 1: we take the ith item

        if item_weight > lim: value_take = 0
        else:
            if i == 0: #  no more items to take
                value_take = item_value
            else:
                value_take = item_value + subproblem(lim - item_weight, i - 1)

        # Option 2: we don't take the ith item
        if i == 0: # no more remaining items
            value_leave = 0
        else:
            value_leave = subproblem(lim, i - 1)

        optimal = max(value_take, value_leave)
        cache[(lim, i)] = optimal

        return optimal

    maximum_value = subproblem(lim, len(items) - 1)
    return maximum_value

# Reflections after working on the above solution.
# I ran this and I legitimately jumped out of my chair when it passed all the tests.
# I honestly cannot believe that it ran successfully.
# I tested it on the complex cases in test_knapsack.py and it solved it in just a couple hundred milliseconds, whereas I'm pretty sure I needed to leave my computer on for days to get the answer with the first solution.
#
# So why is it so much faster?
# 1. No more for-loops. Just rely on recursion to "loop".
# 2. Also, I implement memoizing/caching now (but that's a more minor minor reason)
# 3. I also sorted items but I don't think that makes any practical difference whatsoever.

# I ended up combining all of the 3 things I mentioned wanting to try into one solution.
# My sense is that the time complexity of this algorithm is 2^n, where n is the length of the items, as each recursive call has to make two more recursive calls, growing exponentially.