import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  measurements = [int(line.strip()) for line in file]

def count_increases(data):
  return sum(a < b for a, b in zip(data, data[1:]))

def part_one():
  return count_increases(measurements)

def part_two():
  return count_increases([sum(three_nums) for three_nums in zip(measurements, measurements[1:], measurements[2:])])

if __name__ == "__main__":
  print('Part One: %d' % part_one())
  print('Part Two: %d' % part_two())
