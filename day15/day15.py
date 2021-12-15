import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  data = file.read().strip()

grid = [list(map(int, line)) for line in data.split('\n')]

def bfs(grid):
  costs = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
  costs[0][0] = 0

  stack = [(0, 0)]
  while stack:
    x, y = stack.pop(0)
    for nx, ny in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
      if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
        cost = costs[y][x] + grid[ny][nx]
        if cost < costs[ny][nx]:
          costs[ny][nx] = cost
          stack.append((nx, ny))

  return costs[-1][-1]

print('Part One: %d' % bfs(grid))
