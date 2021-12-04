import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  data = file.read().strip().split("\n\n")

class Board:
  def __init__(self, board):
    lines = [[int(x) for x in line.split()] for line in board.splitlines()]
    self._rows = [set(line) for line in lines]
    self._cols = [set(line) for line in zip(*lines)]
    self._marked_numbers = set()
    self._score = None

  @property
  def has_won(self):
    return self._score is not None

  @property
  def score(self):
    return self._score

  def update(self, number):
    if self._score:
      return
    self._marked_numbers.add(number)
    if (any(row <= self._marked_numbers for row in self._rows) or
        any(col <= self._marked_numbers for col in self._cols)):
      self._score = sum(sum(row - self._marked_numbers) for row in self._rows) * number

def setup_game():
  numbers = [int(x) for x in data[0].split(',')]
  boards = [Board(grid) for grid in data[1:]]
  return numbers, boards

def part_one():
  numbers, boards = setup_game()
  for number in numbers:
    for board in boards:
      if board.has_won:
        continue
      board.update(number)
      if board.has_won:
        return board.score

def part_two():
  numbers, boards = setup_game()
  scores = []
  for number in numbers:
    for board in boards:
      if board.has_won:
        continue
      board.update(number)
      if board.has_won:
        scores.append(board.score)
        if len(scores) == len(boards):
          return scores[-1]

if __name__ == "__main__":
  print('Part One: %d' % part_one())
  print('Part Two: %d' % part_two())
