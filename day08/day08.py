import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  data = file.readlines()

def part_one(data):
  return sum(len(value) in (2, 3, 4, 7, ) for line in data for value in line.split(' | ')[1].split())

def part_two(data):
  x = 0
  for line in data:
    a, b = line.split(' | ')
    patterns, outputs = [set(pattern) for pattern in a.split()], [set(output) for output in b.split()]
    d = {n: pattern for pattern in patterns for n, x in zip([1,4,7,8], [2,4,3,7]) if len(pattern) == x}
    d.update({(9 if d[4].issubset(pattern) else 0 if d[7].issubset(pattern) else 6): pattern for pattern in patterns if len(pattern) == 6})
    d.update({(3 if d[7].issubset(pattern) else 5 if pattern.issubset(d[6]) else 2): pattern for pattern in patterns if len(pattern) == 5})
    x += int(''.join(str(digit) for output in outputs for digit, pattern in d.items() if pattern == output))
  return x

print('Part One: %d' % part_one(data))
print('Part Two: %d' % part_two(data))
