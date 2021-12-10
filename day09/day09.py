import os
from functools import reduce

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  data = [list(map(int, line.strip())) for line in file.readlines()]

def part_one():
  return sum(
    1 + n
    for j in range(len(data))
    for i, n in enumerate(data[j])
    if (
      (j == 0 or n < data[j - 1][i]) and
      (i == 0 or n < data[j][i - 1]) and
      (j >= len(data) - 1 or n < data[j + 1][i]) and
      (i >= len(data[0]) - 1 or n < data[j][i + 1])
    )
  )

def part_two():
  basins = []
  seen = []
  stack = []
  for j in range(len(data)):
    for i, n in enumerate(data[j]):      
      if (i, j) not in seen and n != 9:
        x = 0
        seen.append((i, j))
        stack.append((i, j))
        while stack:
          i_, j_ = stack.pop()
          x += 1
          for neighbour in [(i_ - 1, j_), (i_ + 1, j_), (i_, j_ - 1), (i_, j_ + 1)]:
            if (
              neighbour not in seen and
              0 <= neighbour[0] < len(data[0]) and
              0 <= neighbour[1] < len(data) and
              data[neighbour[1]][neighbour[0]] != 9
            ):
              stack.append(neighbour)
              seen.append(neighbour)
        basins.append(x)
  basins.sort(reverse=True)
  return reduce(lambda a, b: a * b, basins[:3])

print('Part One: %d' % part_one())
print('Part Two: %d' % part_two())
