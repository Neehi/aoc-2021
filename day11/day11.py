import os
from itertools import count

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  data = {(i, j): int(n) for j, line in enumerate(file.readlines()) for i, n in enumerate(line.strip())}

flashes = 0
steps = 0

for step in count(1):
  visited = []

  for pos in data:
      data[pos] += 1
      if data[pos] > 9:
        visited.append(pos)
        data[pos] = 0

  while visited:
    pos = visited.pop()
    for dx, dy in [(-1, -1), (0, -1), (+1, -1), (-1, 0), (+1, 0),(-1, +1), (0, +1), (+1, +1), ]:
      pos_ = (pos[0] + dx, pos[1] + dy)
      if pos_ in data and data[pos_] != 0:
        data[pos_] += 1
        if data[pos_] > 9:
          visited.append(pos_)
          data[pos_] = 0

  flashed = list(data.values()).count(0)

  if step <= 100:
    flashes += flashed

  if flashed == len(data):
    steps = step
    break

print('Part One: %d' % flashes)
print('Part Two: %d' % steps)
