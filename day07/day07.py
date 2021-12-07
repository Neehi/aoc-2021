import os
from collections import Counter

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  positions = Counter([int(x) for x in file.read().split(',')])

def part_one():
  return min(sum(abs(x - pos) * count for x, count in positions.items()) for pos in positions.keys())

def part_two():
  # Sum of integers in sequence = n(u0 + un-1) / 2
  return min(sum((abs(x - pos) * (1 + abs(x - pos)) // 2) * count for x, count in positions.items()) for pos in positions.keys())

print('Part One: %d' % part_one())
print('Part Two: %d' % part_two())
