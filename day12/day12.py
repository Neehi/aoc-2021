import os
from collections import defaultdict, Counter

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  data = [line.strip() for line in file.readlines()]

caves = defaultdict(list)
for line in data:
  a, b = line.strip().split('-')
  for a, b in [(a, b), (b, a)]:
    if a != "end" and b != "start":
      caves[a].append(b)

def find_paths(start, visited=Counter(), revisit_small=False):
  if start == "end":
    return 1
  v = visited + Counter([start] if start.islower() else [])
  return sum(
    find_paths(next, v, revisit_small)
    for next in caves[start]
    if next not in v or revisit_small and v.most_common(1)[0][1] < 2
  )

print('Part One: %d' % find_paths("start"))
print('Part Two: %d' % find_paths("start", revisit_small=True))
