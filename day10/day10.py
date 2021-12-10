# Part 1

char_map = dict([
    ('(', ')'),
    ('[', ']'),
    ('{', '}'),
    ('<', '>'),
])

opening_chars = char_map.keys()
closing_chars = char_map.values()

illegal_char_values = dict([
    (None, 0),
    (')', 3),
    (']', 57),
    ('}', 1197),
    ('>', 25137),
])


def get_expected_closing_char(opening_char):
    return char_map.get(opening_char)


def get_first_ilegal_char(line):
    expected_closing_chars = []
    for char in line:
        if char in closing_chars:
            if not len(expected_closing_chars):
                return None  # Undefined behavior in problem - closing char before opening char
            elif char != expected_closing_chars.pop():
                return char
        elif char in opening_chars:
            expected_closing_chars.append(get_expected_closing_char(char))

    return None

# Part 2


missing_char_values = dict([
    (')', 1),
    (']', 2),
    ('}', 3),
    ('>', 4),
])


def get_autocomplete_score(line):
    expected_closing_chars = []
    for char in line:
        if char in closing_chars:
            if not len(expected_closing_chars):
                return None  # Undefined behavior in problem - closing char before opening char
            expected_closing_chars.pop()
        elif char in opening_chars:
            expected_closing_chars.append(get_expected_closing_char(char))

    autocomplete_str = ''.join(reversed(expected_closing_chars))
    autocomplete_score = 0
    for char in autocomplete_str:
        autocomplete_score *= 5
        autocomplete_score += missing_char_values[char]
    return autocomplete_score


if __name__ == '__main__':
    with open('./input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        first_ilegal_chars = [get_first_ilegal_char(line) for line in lines]
        total_syntax_error_score = sum([illegal_char_values[char] for char in first_ilegal_chars])
        print('Total syntax error score: {}'.format(total_syntax_error_score))

        valid_lines = [line for idx, line in enumerate(lines) if first_ilegal_chars[idx] == None]
        autocomplete_scores = sorted([get_autocomplete_score(valid_line) for valid_line in valid_lines])
        middle_idx = (len(autocomplete_scores) - 1) / 2
        print('Middle autocomplete score: {}'.format(autocomplete_scores[middle_idx]))
