import os
from functools import reduce

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  commands = [line.strip() for line in file]

directions = {
  "forward": (1, 0),
  "down": (0, 1),
  "up": (0, -1),
}

def get_steps():
  steps = []
  for command in commands:
    direction, step = command.split()
    steps.append([n * int(step) for n in directions[direction]])
  return steps

def part_one():
  return reduce(lambda a, b: a * b, [sum(x) for x in zip(*get_steps())])

def part_two():
  x = y = aim = 0
  for step in get_steps():
    aim += step[1]
    x += step[0]
    y += step[0] * aim
  return x * y

print('Part One: %d' % part_one())
print('Part Two: %d' % part_two())
