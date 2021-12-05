import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  report = [line.strip() for line in file]

def get_most_common(data, position):
  return int(sum(bits[position] == '1' for bits in data) >= len(data) // 2)

def part_one():
  gamma_rate = sum(get_most_common(report, n) << (len(report[0]) - 1 - n) for n in range(len(report[0])))
  epsilon_rate = (2 ** len(report[0]) - 1) - gamma_rate
  return gamma_rate * epsilon_rate

def part_two():

  def _find_rating(data, most_common):
    x = 0
    while len(data) > 1:
      value = get_most_common(data, x) ^ most_common
      data = [bits for bits in data if int(bits[x]) == value]
      x += 1
    return int(data[0], base=2)

  oxygen_generator_rating = _find_rating(report, True)  # mcv
  co2_scrubber_rating = _find_rating(report, False)  # lcv
  return oxygen_generator_rating * co2_scrubber_rating

print('Part One: %d' % part_one())
print('Part Two: %d' % part_two())
