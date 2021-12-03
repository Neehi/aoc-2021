import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  report = [line.strip() for line in file]

def count_bits(data):
  return [sum(x) for x in zip(*[[int(bit) for bit in list(bits)] for bits in data])]

def part_one():
  bit_counts = count_bits(report)
  gamma_rate = int("".join([str(int(n > len(report) // 2)) for n in bit_counts]), base=2)
  epsilon_rate = (2 ** len(bit_counts) - 1) - gamma_rate
  return gamma_rate * epsilon_rate

def part_two():
  # oxygen generator (mcv)
  og_list = report
  x = 0
  while len(og_list) > 1:
    bit_counts = count_bits(og_list)
    og_list = [value for value in og_list if int(value[x]) == int(bit_counts[x] >= len(og_list) - bit_counts[x])]
    x += 1
  oxygen_generator_rating = int(og_list[0], base=2)

  # co2 scrubber (lcv)
  co2_list = report
  x = 0
  while len(co2_list) > 1:
    bit_counts = count_bits(co2_list)
    co2_list = [value for value in co2_list if int(value[x]) != int(bit_counts[x] >= len(co2_list) - bit_counts[x])]
    x += 1
  co2_scrubber_rating = int(co2_list[0], base=2)

  return oxygen_generator_rating * co2_scrubber_rating

if __name__ == "__main__":
  print('Part One: %d' % part_one())
  print('Part Two: %d' % part_two())
