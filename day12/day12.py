import os
from collections import defaultdict

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  data = [line.strip() for line in file.readlines()]

caves = defaultdict(list)
for line in data:
  a, b = line.strip().split('-')
  caves[a].append(b)
  caves[b].append(a)

def find_paths(start, visited=set(), revisit_small=False):
  if start == "end":
    return 1
  return sum(
    find_paths(next, visited | {start}, revisit_small and (next not in visited or next.isupper()))
    for next in caves[start]
    if next not in visited or next.isupper() or revisit_small and next != "start"
  )

print('Part One: %d' % find_paths("start"))
print('Part Two: %d' % find_paths("start", revisit_small=True))
