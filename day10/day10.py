import os
from functools import reduce

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  data = [line.strip() for line in file.readlines()]

closures = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores_1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores_2 = {'(': 1, '[': 2, '{': 3, '<': 4}

def part_one():
  breaks = []
  for line in data:
    stack = []
    for c in line:
      if c in closures.keys():
        stack.append(c)
      elif c != closures[stack.pop()]:
        breaks.append(c)
        break
  return sum(scores_1[x] for x in breaks)

def part_two():
  scores = []
  for line in data:
    stack = []
    corrupted = False
    for c in line:
      if c in closures.keys():
        stack.append(c)
      elif c != closures[stack.pop()]:
        corrupted = True
    if not corrupted:
      score = 0
      for x in reversed(stack):
        score = score * 5 + scores_2[x]
      scores.append(score)
  scores.sort()
  return(scores[len(scores) // 2])

print('Part One: %d' % part_one())
print('Part Two: %d' % part_two())
