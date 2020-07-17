// I: MXN of ints 1 and 0
// 0: int, # of islands
// C:
// E: null matrix, no islands

var numIslands = (grid) => {
  if (grid.length === 0) {
      return 0
  }
  const m = grid.length;
  const n = grid[0].length;
  const isValid = (x,y) => {
    return x > -1 && y > -1 && x < m && y < n;
  }

  let res = 0;

  const bfs = (s, t) => {
    if (grid[s][t] === "1") {
      grid[s][t] = "2";
      if (isValid(s+1, t)) {
        bfs(s + 1, t);
      }
      if (isValid(s-1, t)) {
        bfs(s - 1, t);
      }
      if (isValid(s, t + 1)) {
        bfs(s, t + 1);
      }
      if (isValid(s, t - 1)) {
        bfs(s, t - 1);
      }

    }

  }

  for (let i = 0; i < m; i += 1) {
    for (let j = 0; j < n; j += 1) {
      if (grid[i][j] === "1") {
        res += 1;
        bfs(i, j);
      }
    }
  }

  return res;


};