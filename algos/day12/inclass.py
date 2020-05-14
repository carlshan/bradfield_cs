from pprint import pprint
# Question 1: Number of paths in a lattice but with blockers
# Idea: regular method of 2D dynamic programming but check if if the square is blocked
# Input: 2D array

def num_paths(graph):
    if len(graph) == 0 or len(graph[0]) == 0:
        return 0
    nrows = len(graph)
    ncols = len(graph[0])

    paths_matrix = [[1] * (ncols + 1) for _ in range(0, nrows + 1)]

    #paths_matrix[0][0] = 1 # one way to get to the start, which is to start on it
    # Incomplete, need to handle cases on the walls where they are blocked by 1s in the graph
    for i, row in enumerate(paths_matrix):
        for j, _ in enumerate(row):
            if i == 0 or j == 0:
                continue
            above_count = paths_matrix[i - 1][j]
            above_valid = graph[i - 2][j - 1]
            left_count = paths_matrix[i][j - 1]
            left_valid = graph[i - 1][j - 2]
            if above_valid == 1:
                above_count = 0
            if left_valid == 1:
                left_count = 0
            paths_matrix[i][j] = left_count + above_count

    return paths_matrix, paths_matrix[-1][-1]

def num_paths2(graph):
    if len(graph) == 0 or len(graph[0]) == 0:
        return 0
    nrows = len(graph)
    ncols = len(graph[0])

    paths_matrix = [[0] * ncols] * nrows

    for row in range(nrows):
        if graph[row][0] == 1:
            break
        paths_matrix[row][0] = 1

    for col in range(ncols):
        if graph[0][col] == 1:
            break
        paths_matrix[0][col] = 1

    #paths_matrix[0][0] = 1 # one way to get to the start, which is to start on it
    # Incomplete, need to handle cases on the walls where they are blocked by 1s in the graph
    for i in range(1, nrows):
        for j in range(1, ncols):
            above_count = paths_matrix[i - 1][j]
            above_valid = graph[i - 1][j]
            left_count = paths_matrix[i][j - 1]
            left_valid = graph[i][j - 1]
            if above_valid == 1:
                above_count = 0
            if left_valid == 1:
                left_count = 0
            paths_matrix[i][j] = left_count + above_count

    return paths_matrix, paths_matrix[-1][-1]

graph = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
 ]
graph = [[0] * 10] * 10
graph = [[0] * 2] * 2
graph = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
 ]
#paths_matrix = num_paths2(graph)
#pprint(paths_matrix)


def num_paths_dp(height, width):
    memo = [[1] * (width + 1) for _ in range(0, height + 1)]
    for i, row in enumerate(memo):
        for j, _ in enumerate(row):
            if i == 0 or j == 0:
                continue
            memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
    return memo, memo[-1][-1]


# Longest Common Subsequence

def lcs(s1, s2):
    if s1 == '' or s2 == '':
        return 0
    if s1[0] == s2[0]:
        return 1 + lcs(s1[1:], s2[1:])
    else:
        return max(lcs(s1[1:], s2), lcs(s1, s2[1:]))

def lcs_dp(s1, s2):

    dp = [[0] * (len(s1) + 1)] * (len(s2) + 1)
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j-1])
    return dp[-1][-1]

print(lcs_dp('abc', 'abc'))
