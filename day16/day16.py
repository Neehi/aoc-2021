import os

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
    return V, packet

  # Subpackets
  version_sum = V

  if packet[0] == "0":  # Packet of size n
    len_subpackets, packet = int(packet[1:16], base=2), packet[16:]
    to_process = packet[:len_subpackets]
    while len(to_process):
      v, to_process = process_packet(to_process)
      version_sum += v
    packet = packet[len_subpackets:]

  else:  # n packets
    num_subpackets, packet = int(packet[1:12], base=2), packet[12:]
    for _ in range(num_subpackets):
      v, packet = process_packet(packet)
      version_sum += v

  return version_sum, packet

print('Part One: %d' % process_packet(transmission)[0])
