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

print('Part One: %d' % part_one())
