import os
from collections import Counter

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  data = [[tuple(map(int, pair.split(','))) for pair in line.split('->')] for line in file]

def count_overlaps(data, diagonals):
  counter = Counter()
  for a, b in data:
    (x1, y1), (x2, y2) = a, b
    if x1 == x2:
      counter.update([(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)])
    elif y1 == y2:
      counter.update([(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)])
    elif diagonals:
      counter.update([
        (x, y) for x, y
        in zip(range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1), range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1))
      ])
  return sum(x > 1 for x in counter.values())

print("Part One: %d" % count_overlaps(data, False))
print("Part Two: %d" % count_overlaps(data, True))
