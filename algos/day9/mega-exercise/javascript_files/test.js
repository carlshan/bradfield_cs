var assert = require('assert');
var search = require('./search');

// Constants
let START = S = 's';
let GOAL = G = 'x';
let NORMAL = N = ' ';
let MOUNTAIN = M = '^';
let RIVER = R = '-';

let COSTS = {
    START: 0,
    GOAL: 1,
    NORMAL: 1,
    MOUNTAIN: Infinity,
    RIVER: 2
};

// For the given grid and search result, print a visualization
function visualize(algorithm, grid, goal, explored) {
  // Extract the path taken
  let path = {};
  let node = goal
  let cost = 0
  while (node in explored) {
    path[node] = true;
    cost += COSTS[grid[node[0]][node[1]]]
    node = explored[node]
  }
    
  // Prepare a visual form of grid, with path overlaid
  let rows = [];
  for (let i = 0; i < grid.length; i++) {
    let row = [];
    for (let j = 0; j < grid[i].length; j++) {
      if ([i, j] in path) {
        row.push(grid[i][j] + '\u0359');
      } else {
        row.push(grid[i][j]);
      }
    }
    rows.push(row.join(' '));
  }
  let visualization = rows.join('\n');

  console.log(`
-----------------------
${algorithm}
Nodes explored: ${Object.keys(explored).length}
Path cost: ${cost}
${goal in explored ? 'Goal reached!' : 'Goal NOT reached'}
${visualization}
`);
}

// When running from the command line, compare every algorithm against
// one of the tests.
let choice = process.argv[2];

if (choice !== 'little' && choice !== 'big' && choice !== 'random') {
  console.log('Usage: node test.js (little|big|random)');
  process.exit();
}

let start = [0, 0]
let grid, goal;
if (choice === 'little') {
  grid = [
    [S, N, N, N],
    [N, M, M, M],
    [N, R, R, R],
    [N, N, N, G]
  ];
  goal = [3, 3];
} else if (choice === 'big') {
  grid = [
    [S, R, R, R, M, G],
    [N, R, R, R, M, N],
    [N, M, R, R, R, N],
    [N, N, N, N, R, N],
    [N, R, N, N, N, N],
    [N, R, N, N, N, N]
  ];
  goal = [0, 5];
} else if (choice === 'random') {
  let rows = 10, cols = 10;
  goal = [Math.floor(Math.random() * rows), Math.floor(Math.random() * cols)];
  let types = [NORMAL, MOUNTAIN, RIVER];
  grid = [];
  for (let i = 0; i < rows; i++) {
    let row = [];
    for (let j = 0; j < cols; j++) {
      row.push(types[Math.floor(Math.random() * types.length)]);
    }
    grid.push(row);
  }
  grid[start[0]][start[1]] = START;
  grid[goal[0]][goal[1]] = GOAL;
}
    
// Run each algorithm and visualize the result
visualize('BFS', grid, goal, search.bfs(grid, start, goal));
visualize('DFS', grid, goal, search.dfs(grid, start, goal));
visualize('Dijkstra’s algorithm', grid, goal, search.ucs(grid, start, goal));
visualize('A* search', grid, goal, search.a_star(grid, start, goal));
