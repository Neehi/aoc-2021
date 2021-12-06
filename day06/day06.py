import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  data = [int(x) for x in file.read().split(',')]

def simulate_lanternfish(data, days):
  fish = [data.count(x) for x in range(9)]
  for _ in range(days):
    fish.append(fish.pop(0))
    fish[6] += fish[8]
  return sum(fish)

print('Part One: %d' % simulate_lanternfish(data, 80))
print('Part Two: %d' % simulate_lanternfish(data, 256))
