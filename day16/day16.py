import os
from functools import reduce

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  data = file.read().strip()

transmission = bin(int(data, 16))[2:].zfill(len(data) * 4)

def process_packet(packet):
  # Version
  V, packet = int(packet[:3], base=2), packet[3:]

  # Type
  T, packet = int(packet[:3], base=2), packet[3:]

  # Literal
  if T == 4:
    literal = ""
    while True:
      prefix = packet[0]
      literal += packet[1:5]
      packet = packet[5:]
      if prefix == "0":
        break
    return V, int(literal, base=2), packet

  # Subpackets
  version_sum = V
  subpacket_values = []

  if packet[0] == "0":  # Packet of size n
    len_subpackets, packet = int(packet[1:16], base=2), packet[16:]
    to_process = packet[:len_subpackets]
    while len(to_process):
      v, value, to_process = process_packet(to_process)
      version_sum += v
      subpacket_values.append(value)
    packet = packet[len_subpackets:]

  else:  # n packets
    num_subpackets, packet = int(packet[1:12], base=2), packet[12:]
    for _ in range(num_subpackets):
      v, value, packet = process_packet(packet)
      version_sum += v
      subpacket_values.append(value)

  # Calculations
  if T == 0:  # Sum
    value = sum(subpacket_values)
  elif T == 1:  # Product
    value = reduce(lambda a, b: a * b, subpacket_values)
  elif T == 2:  # Min
    value = min(subpacket_values)
  elif T == 3:  # Max
    value = max(subpacket_values)
  elif T == 5:  # [0] > [1]
    value = int(subpacket_values[0] > subpacket_values[1])
  elif T == 6:  # [0] < [1]
    value = int(subpacket_values[0] < subpacket_values[1])
  elif T == 7:  # [0] == [1]
    value = int(subpacket_values[0] == subpacket_values[1])

  return version_sum, value, packet

version_sum, value, _ = process_packet(transmission)

print('Part One: %d' % version_sum)
print('Part Two: %d' % value)
