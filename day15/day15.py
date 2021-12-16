import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  data = file.read().strip()

data = [list(map(int, line)) for line in data.split('\n')]

def bfs(tile_size=1):
  grid = [
    [(data[y][x] + tx + ty - 1) % 9 + 1 for tx in range(tile_size) for x in range(len(data[0]))]
    for ty in range(tile_size) for y in range(len(data))
  ]

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

print('Part One: %d' % bfs(1))
print('Part Two: %d' % bfs(5))
