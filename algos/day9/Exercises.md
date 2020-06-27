# Exercises for Weighted and Unweighted Graphs
Compiled by: Carl Shan
Contributions from: The Bradfield School of Computer Science

## Exercises

1. [Leetcode: Network Delay Time](https://leetcode.com/problems/network-delay-time/description/)
   * [9 min walkthrough solution](https://www.youtube.com/watch?v=pjITHX3JwH0)
2. [Leetcode: Number of Islands](https://leetcode.com/problems/number-of-islands/)
3. Given two jugs, one with a maximum capacity of `A` liters of water and another with a maximum capacity of `B`, return the number of steps necessary to fill exactly `target` liters of water. For example, if Jug A could fill 3, Jug B could fill 5 and the target is for one of them to end up containing 4 liters of water, the minimum number of steps is `6`.
4. Solve the mega-exercise below.

## Mega-Exercise
This exercise pulls everything we've learned together into one fun mega-exercise.

It was created by instructors at the [Bradfield School of Computer Science](http://bradfieldcs.com/).

Read on below to understand the exercise. Some starter files for both Javascript and Python have been created in the folder `mega-exercise`.

In this exercise you’ll implement several versions of graph search in a simple maze, represented by a 2D grid. The grid has 3 kinds of squares: normal, river and mountain. Normal squares can be traversed at a cost of 1, rivers can be traversed at a cost of 2, and mountain squares can’t be traversed (they have “infinite cost”).

Finally, there are two special values which occur exactly once each, and are always “normal” squares: the start and goal. Consider one such maze:

```
grid_world = [
    [S, N, N, N],
    [N, M, M, M],
    [N, R, R, R],
    [N, N, N, G]
]
```
Here, `S` = `start`, `G` = `goal`, `N` = `normal`, `R` = `river` and `M` = `mountain`.

This maze is 4x4, and the “shortest path” is to go down 3 times, then right 3 times, avoiding the river in the 3rd row.

The goal of this exercise is to build and compare simple implementations of BFS, DFS, Dijkstra’s Algorithm and A* over such grids.

## Getting Started
The below example uses Python as illustration, but testing files in Javascript have also been provided.

You may implement your search functions however you wish, but for the visualization to function correctly, your return value must be in the form of a dictionary where the keys are (row, col) tuples, and the values are also (row, col) tuples such that the keys represent a grid square, and the values represent the square from which the value was reached. For example, in this simple grid world:

`[['S', ' ', 'G']]`

The explored list would contain three entries:

```python
explored = {
  (0, 0): None,  # The starting location has no parent location
  (0, 1): (0, 0), # The location (0,1) was reached from the location (0,0)
  (0, 2): (0, 1)  # The goal (0,2) was reached from the middle square (0,1)
}
```

As a guide, our reference solution produces the following output for a random 10x10 world.

```
-----------------------
BFS
Nodes explored: 54
Path cost: 25
Goal reached!

s͙  ͙ -͙  ͙ -͙ -͙ - ^ - ^
- - - ^ ^ -͙ -͙
  - ^ ^ ^ ^  ͙     ^
^ ^ ^ -     -͙   - -
-       ^ -͙ -͙   - ^
    - - -͙  ͙   ^ ^ ^
-   x͙  ͙  ͙ - -   -
  ^ -   ^ ^ -   ^ -
  ^ ^     - - ^ ^ ^
^ -   -   ^ -   ^


-----------------------
DFS
Nodes explored: 27
Path cost: 39
Goal reached!

s͙   -͙  ͙ -͙ -͙ -͙ ^ - ^
-͙ -͙ -͙ ^ ^ - -͙  ͙  ͙
  - ^ ^ ^ ^      ͙ ^
^ ^ ^ -͙  ͙  ͙ -͙   -͙ -
-      ͙ ^ - -͙  ͙ -͙ ^
    -͙ -͙ -     ^ ^ ^
-   x͙     - -   -
  ^ -   ^ ^ -   ^ -
  ^ ^     - - ^ ^ ^
^ -   -   ^ -   ^


-----------------------
Dijkstra’s algorithm
Nodes explored: 53
Path cost: 24
Goal reached!

s͙  ͙ -͙  ͙ -͙ -͙ -͙ ^ - ^
- - - ^ ^ - -͙
  - ^ ^ ^ ^  ͙     ^
^ ^ ^ -͙  ͙  ͙ -͙   - -
-    ͙  ͙ ^ - -   - ^
    -͙ - -     ^ ^ ^
-   x͙     - -   -
  ^ -   ^ ^ -   ^ -
  ^ ^     - - ^ ^ ^
^ -   -   ^ -   ^


-----------------------
A* search
Nodes explored: 37
Path cost: 24
Goal reached!

s͙  ͙ -͙  ͙ -͙ -͙ -͙ ^ - ^
- - - ^ ^ - -͙
  - ^ ^ ^ ^  ͙     ^
^ ^ ^ -͙  ͙  ͙ -͙   - -
-    ͙  ͙ ^ - -   - ^
    -͙ - -     ^ ^ ^
-   x͙     - -   -
  ^ -   ^ ^ -   ^ -
  ^ ^     - - ^ ^ ^
^ -   -   ^ -   ^
```

Three different options have been provided for testing: a `little` world, a `big` world and `random` world. These options can be invoked at the command line when running the appropriate testing file.

They can be run with:

`python3 test.py {little|big|random}`

If you are using Javascript, you can simply use `node`:

`node test.js {little|big|small}`

We suggest testing your solutions on the little and big worlds first, then seeing if you observe anything interesting from running on random worlds!