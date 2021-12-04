import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  data = file.read().strip().split("\n\n")

numbers = [int(x) for x in data[0].split(',')]

boards = []
for board in data[1:]:
  lines = [[int(x) for x in line.split()] for line in board.splitlines()]
  rows = [set(line) for line in lines]
  cols = [set(line) for line in zip(*lines)]
  boards.append({'rows': rows, 'cols': cols})

def part_one():
  drawn = set()
  for number in numbers:
    drawn.add(number)
    for board in boards:
      if (any(row <= drawn for row in board['rows']) or
          any(col <= drawn for col in board['cols'])):
        return sum(sum(row - drawn) for row in board['rows']) * number

if __name__ == "__main__":
  print('Part One: %d' % part_one())
