from collections import Counter


def get_1_4_7_8_digit_ct(entries):
    digit_ct = 0
    for entry in entries:
        digit_ct += len([val for val in entry[1].split(' ') if len(val) in [2, 3, 4, 7]])
    return digit_ct


def get_char_replacement_map(signal_patterns):
    replacements = dict([('a', None), ('b', None), ('c', None), ('d', None), ('e', None), ('f', None), ('g', None)])
    signal_patterns = [''.join(sorted(signal_pattern)) for signal_pattern in sorted(signal_patterns, key=len)]

    # Solve signals b/e/f based on how often they're used within entire set of signal patterns
    true_signal_count_in_all_signal_patterns = dict([('e', 4), ('b', 6), ('d', 7), ('g', 7), ('c', 8), ('a', 8), ('f', 9)])
    signal_count_in_all_signal_patterns = Counter(''.join(signal_patterns)).items()

    for char, true_ct in true_signal_count_in_all_signal_patterns.items():
        replacements[char] = [replacement_char for replacement_char, ct in signal_count_in_all_signal_patterns if ct == true_ct]

    # Solve signal a because it's in digit 7 but not digit 1
    replacements['a'] = [c for c in signal_patterns[1] if c not in signal_patterns[0]]

    # Solve signal c
    replacements['c'] = [replacement_char for replacement_char in replacements['c'] if replacement_char not in replacements['a']]

    # Solve g using 0 digit
    # Signal_pattern that has abcef in it also has g in it (digit 0)
    required_0_digit_signals = [replacements[c][0] for c in 'abcef']
    possible_0_digit_signal_patterns = [pattern for pattern in signal_patterns if len(pattern) == 6]
    for signal_pattern in possible_0_digit_signal_patterns:
        if all([(c in signal_pattern) for c in required_0_digit_signals]):
            replacements['g'] = [c for c in signal_pattern if c not in required_0_digit_signals]

    # Solve d using g
    replacements['d'] = [c for c in replacements['d'] if c not in replacements['g']]
    # Invert for use later -> key = replacement_char, value = true_char
    return {v[0]: k for k, v in replacements.items()}


digit_map = dict([
    ('abcefg', '0'),
    ('cf', '1'),
    ('acdeg', '2'),
    ('acdfg', '3'),
    ('bcdf', '4'),
    ('abdfg', '5'),
    ('abdefg', '6'),
    ('acf', '7'),
    ('abcdefg', '8'),
    ('abcdfg', '9'),
])


def get_output_value(char_replacements, output_patterns):
    output_value = ''
    for pattern in output_patterns:
        decrypted_pattern = ''.join(sorted([char_replacements[c][0] for c in pattern]))
        output_value += digit_map[decrypted_pattern]
    return int(output_value)


if __name__ == '__main__':
    with open('./input.txt') as f:
        entries = [line.strip().split(' | ') for line in f.readlines()]
        digit_ct = get_1_4_7_8_digit_ct(entries)
        print("Count of 1,4,7,8 digits in output values: {}".format(digit_ct))

        output_sum = 0
        for entry in entries:
            signal_patterns = entry[0].split(' ')
            char_replacements = get_char_replacement_map(signal_patterns)
            output_patterns = [sorted(pattern) for pattern in entry[1].split(' ')]
            output_sum += get_output_value(char_replacements, output_patterns)

        print("Sum of output values: {}".format(output_sum))
