import os
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  x_min, x_max, y_min, y_max = map(int, re.findall(r"[-\d]+", file.read().strip()))

def part_one():
  # Using example:
  #   y_min = -10
  #   max_y = 45
  #   velocity = 9,8,7..-8,-9,-10
  # Solution:
  #   Only care about the +ve velocities as these give the height
  #   Can use consecutive numbers formula as the velocity decreases by 1 each step
  # Formula:
  #   n * (n + 1) / 2, where n = abs(y_min) + 1
  return (y_min + 1) * y_min // 2  # Assumes y_min is negative

def part_two():
  n = 0
  for vx in range(x_max + 1):
    for vy in range(-abs(y_min), abs(y_min)):
      x, y, dx, dy = 0, 0, vx, vy
      while x <= x_max and y > y_min:
        x += dx
        y += dy
        if x_min <= x <= x_max and y_min <= y <= y_max:
          n += 1
          break
        dx = max(0, dx - 1)
        dy -= 1
  return n

print('Part One: %d' % part_one())
print('Part Two: %d' % part_two())
