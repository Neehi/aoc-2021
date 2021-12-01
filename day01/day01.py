import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  measurements = [int(line.strip()) for line in file]

def part_one():
  return sum(a < b for a, b in zip(measurements, measurements[1:]))

def part_two():
  return sum(sum(measurements[i:i+3]) < sum(measurements[i+1:i+4]) for i in range(len(measurements) - 3))

if __name__ == "__main__":
  print('Part One: %d' % part_one())
  print('Part Two: %d' % part_two())
