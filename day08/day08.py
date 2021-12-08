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

    # 1, 4, 7, 8
    d = {n: pattern for pattern in patterns for n, x in zip([1,4,7,8], [2,4,3,7]) if len(pattern) == x}

    # 3 is only 5 letter pattern that contains 7
    d[3] = [pattern for pattern in patterns if len(pattern) == 5 and pattern & d[7] == d[7]][0]

    # 9 is only 6 letter pattern that contains 3
    d[9] = [pattern for pattern in patterns if len(pattern) == 6 and pattern & d[3] == d[3]][0]

    # 6 is only 6 letter pattern that doesn't contain 7
    d[6] = [pattern for pattern in patterns if len(pattern) == 6 and pattern & d[7] != d[7]][0]

    # 5 is only 5 letter pattern contained by 6
    d[5] = [pattern for pattern in patterns if len(pattern) == 5 and pattern & d[6] == pattern][0]

    # 2 is remaining 5 letter
    d[2] = [pattern for pattern in patterns if len(pattern) == 5 and pattern not in d.values()][0]

    # 0 is remaining 6 letter
    d[0] = [pattern for pattern in patterns if len(pattern) == 6 and pattern not in d.values()][0]

    # ...
    x += int(''.join(str(digit) for output in outputs for digit, pattern in d.items() if pattern == output))

  return x

print('Part One: %d' % part_one(data))
print('Part Two: %d' % part_two(data))
