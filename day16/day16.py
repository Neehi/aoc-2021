import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  data = file.read().strip()

transmission = bin(int(data, 16))[2:].zfill(len(data) * 4)

def process_number(packet, num_bits):
  return int(packet[:num_bits], base=2), packet[num_bits:]

def process_literal(packet):
  literal = ""
  while True:
    prefix = packet[0]
    literal += packet[1:5]
    packet = packet[5:]
    if prefix == "0":
      break
  return int(literal, base=2), packet

def process_packet(packet):
  # Version
  V, packet = process_number(packet, 3)
  version_sum = V

  # Type
  T, packet = process_number(packet, 3)

  # Literal
  if T == 4:
    _, packet = process_literal(packet)  # Can be ignored?

  # Subpackets
  elif packet[0] == "0":
    len_subpackets, packet = process_number(packet[1:], 15)
    to_process = packet[:len_subpackets]
    while len(to_process):
      v, to_process = process_packet(to_process)
      version_sum += v
    packet = packet[len_subpackets:]

  else:
    num_subpackets, packet = process_number(packet[1:], 11)
    for _ in range(num_subpackets):
      v, packet = process_packet(packet)
      version_sum += v

  return version_sum, packet

print('Part One: %d' % process_packet(transmission)[0])
