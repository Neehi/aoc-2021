import os
from collections import Counter

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  data = file.read().strip()

polymer, rules = data.split('\n\n')
pairs = Counter(a + b for a, b in zip(polymer, polymer[1:]))
rules = dict(rule.split(' -> ') for rule in rules.split('\n'))

def solve(steps):
  pairs_ = pairs
  for _ in range(steps):
    temp_ = Counter()
    for pair in pairs_:
      if pair in rules:
        temp_[pair[0] + rules[pair]] += pairs_[pair]
        temp_[rules[pair] + pair[1]] += pairs_[pair]
    pairs_ = temp_

  chars = Counter()
  for pair, n in pairs_.items():
    chars[pair[0]] += n
  chars[polymer[-1]] += 1

  return chars.most_common()[0][1] - chars.most_common()[-1][1]

print('Part One: %d' % solve(10))
print('Part Two: %d' % solve(40))
