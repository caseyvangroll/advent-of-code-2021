from collections import namedtuple
from functools import reduce

Packet = namedtuple('Packet', 'version type value')

SUM = 0
PRODUCT = 1
MINIMUM = 2
MAXIMUM = 3
LITERAL = 4
GREATER_THAN = 5
LESS_THAN = 6
EQUAL_TO = 7


# Returns the literal packet at the head of the binary string, and the remaining binary string
def parse_literal(packet_version, binary_str):
    literal_val = ''
    while binary_str[0] != '0':
        literal_val += binary_str[1:5]
        binary_str = binary_str[5:]
    literal_val += binary_str[1:5]
    binary_str = binary_str[5:]

    literal_packet = Packet(version=packet_version, type=LITERAL, value=int(literal_val, 2))

    return literal_packet, binary_str


# Returns the operator packet at the head of the binary string, and the remaining binary string
def parse_operator(packet_version, packet_type, binary_str):
    packet_length_type = binary_str[0]
    if packet_length_type == '0':
        subpackets_len_in_bits = int(binary_str[1:16], 2)
        remaining_subpacket_body = binary_str[16: 16 + subpackets_len_in_bits]
        subpackets = []
        while '1' in remaining_subpacket_body:
            subpacket, remaining_subpacket_body = decode(remaining_subpacket_body)
            subpackets.append(subpacket)

        operator_packet = Packet(version=packet_version, type=packet_type, value=subpackets)
        remaining_body = binary_str[16 + subpackets_len_in_bits:]
        return operator_packet, remaining_body

    subpacket_ct = int(binary_str[1:12], 2)
    remaining_body = binary_str[12:]
    subpackets = []

    for _ in range(subpacket_ct):
        subpacket, remaining_body = decode(remaining_body)
        subpackets.append(subpacket)

    operator_packet = Packet(version=packet_version, type=packet_type, value=subpackets)
    return operator_packet, remaining_body


def decode(binary_str):
    packet_version = int(binary_str[:3], 2)
    packet_type = int(binary_str[3:6], 2)
    packet_body = binary_str[6:]

    if packet_type == LITERAL:
        packet, remaining_body = parse_literal(packet_version, packet_body)
    else:
        packet, remaining_body = parse_operator(packet_version, packet_type, packet_body)

    return packet, remaining_body


def add_up_versions(packet):
    if packet.type == LITERAL:
        return packet.version
    return packet.version + sum([add_up_versions(subpacket) for subpacket in packet.value])


def evaluate(packet):
    if packet.type == LITERAL:
        return packet.value

    subpacket_values = [evaluate(subpacket) for subpacket in packet.value]
    if packet.type == SUM:
        return sum(subpacket_values)
    if packet.type == PRODUCT:
        return reduce(lambda acc, x: acc * x, subpacket_values, 1)
    if packet.type == MINIMUM:
        return min(subpacket_values)
    if packet.type == MAXIMUM:
        return max(subpacket_values)

    left, right = subpacket_values
    if packet.type == GREATER_THAN:
        return int(left > right)
    if packet.type == LESS_THAN:
        return int(left < right)
    if packet.type == EQUAL_TO:
        return int(left == right)


if __name__ == '__main__':
    with open('./input.txt') as f:
        input = f.readlines()[0].strip()
        binary_transmission = ''.join(bin(int(h_digit, 16))[2:].zfill(4) for h_digit in input)

        master_packet, remaining_body = decode(binary_transmission)
        version_sum = add_up_versions(master_packet)
        print("Total sum of packet versions: {}".format(version_sum))

        result = evaluate(master_packet)
        print("Result of the master packet: {}".format(result))
