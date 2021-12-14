def get_min_max_elements(polymer_template, insertion_rules):
    # Keep track of how many there are of each pair
    pair_cts = dict()
    for i in range(len(polymer_template) - 1):
        pair = polymer_template[i:i + 2]
        if pair not in pair_cts:
            pair_cts[pair] = 0
        pair_cts[pair] += 1

    # Each iteration replace each pair with the corresponding pairs in the rules
    for i in range(40):
        next_pair_cts = dict()
        for pair, pair_ct in pair_cts.items():
            for added_pair in insertion_rules[pair]:
                if added_pair not in next_pair_cts:
                    next_pair_cts[added_pair] = 0
                next_pair_cts[added_pair] += pair_ct
        pair_cts = next_pair_cts

    # Count em up
    element_cts = dict()
    for pair, pair_ct in pair_cts.items():
        for element in pair:
            if element not in element_cts:
                element_cts[element] = 0
            element_cts[element] += pair_ct

    # Get min/max
    max_ct, max_element = None, None
    min_ct, min_element = None, None
    for element, element_ct in element_cts.items():
        if max_ct == None or element_ct > max_ct:
            max_element = element
            max_ct = element_ct
        if min_ct == None or element_ct < min_ct:
            min_element = element
            min_ct = element_ct

    # Halve because every element is counted twice (it's in 2 pairs)
    min_ct /= 2
    max_ct /= 2

    # Edge elements shouldn't count toward the halfing part
    edge_elements = [polymer_template[0], polymer_template[-1]]
    if max_element in edge_elements:
        max_ct += 1
    if min_element in edge_elements:
        min_ct += 1
    return min_ct, max_ct


def parse_input(input):
    polymer_template, rules = input[0], input[2:]
    insertion_rules = dict()
    for pair, inserted_element in [rule.split(' -> ') for rule in rules]:
        insertion_rules[pair] = [pair[0] + inserted_element, inserted_element + pair[1]]
    return polymer_template, insertion_rules


if __name__ == '__main__':
    with open('./input.txt') as f:
        input = [line.strip() for line in f.readlines()]
        polymer_template, insertion_rules = parse_input(input)
        min_ct, max_ct = get_min_max_elements(polymer_template, insertion_rules)
        print("Count of least common element: {}".format(min_ct))
        print("Count of most common element: {}".format(max_ct))
        print("Difference : {}".format(max_ct - min_ct))
