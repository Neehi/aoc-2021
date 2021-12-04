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

def is_winner(board, drawn):
  return (any(row <= drawn for row in board['rows']) or
          any(col <= drawn for col in board['cols']))

def part_one():
  drawn = set()
  for number in numbers:
    drawn.add(number)
    for board in boards:
      if is_winner(board, drawn):
        return sum(sum(row - drawn) for row in board['rows']) * number

def part_two():
  drawn = set()
  winners = set()
  for number in numbers:
    drawn.add(number)
    for idx, board in enumerate(boards):
      if idx in winners:
        continue
      if is_winner(board, drawn):
        winners.add(idx)
        if len(winners) == len(boards):
          return sum(sum(row - drawn) for row in board['rows']) * number

if __name__ == "__main__":
  print('Part One: %d' % part_one())
  print('Part Two: %d' % part_two())
