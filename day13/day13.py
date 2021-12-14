import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  dots, folds = file.read().strip().split('\n\n')

dots = set(tuple(map(int, line.split(','))) for line in dots.split('\n'))

folds = [tuple(fold.split()[-1].split('=')) for fold in folds.split('\n')]

def fold_paper(dots, max_folds=None):
  d = dots
  for axis, n in folds[:max_folds]:
    n = int(n)
    d = set(
      (x, n + n - y) if axis == 'y' and y > n
      else (n + n - x, y) if axis == 'x' and x > n
      else (x, y)
      for x, y in list(d)
    )
  return d

print('Part One: %d' % len(fold_paper(dots, 1)))

print('Part Two:')
d = fold_paper(dots)
X, Y = zip(*d)
for y in range(max(Y) + 1):
  print("".join(" #"[(x, y) in d] for x in range(max(X) + 1)))
