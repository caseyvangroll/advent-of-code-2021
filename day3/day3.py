from collections import Counter, namedtuple

Frequency = namedtuple('Frequency', 'digit count')


def get_digit_frequencies(diagnostics, column):
    counter = Counter()
    counter['0'] = 0
    counter['1'] = 0
    counter.update([diagnostic[column] for diagnostic in diagnostics])

    freqs = counter.most_common()
    most_common = Frequency(freqs[0][0], freqs[0][1])
    least_common = Frequency(freqs[1][0], freqs[1][1])
    return most_common, least_common


def get_power_consumption(diagnostics):
    gamma_rate = ''
    epsilon_rate = ''
    for column in range(len(diagnostics[0])):
        most_common, least_common = get_digit_frequencies(diagnostics, column)
        gamma_rate += most_common.digit
        epsilon_rate += least_common.digit

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def get_oxygen_generator_rating(diagnostics):
    oxygen_generator_ratings = [*diagnostics]

    for column in range(len(diagnostics[0])):
        most_common, least_common = get_digit_frequencies(oxygen_generator_ratings, column)
        target_digit = most_common.digit if most_common.count != least_common.count else '1'
        if len(oxygen_generator_ratings) > 1:
            oxygen_generator_ratings = [diagnostic for diagnostic in oxygen_generator_ratings if diagnostic[column] == target_digit]

    return oxygen_generator_ratings[0]


def get_co2_scrubber_rating(diagnostics):
    co2_scrubber_ratings = [*diagnostics]

    for column in range(len(diagnostics[0])):
        most_common, least_common = get_digit_frequencies(co2_scrubber_ratings, column)
        target_co2_scrubber_digit = least_common.digit if most_common.count != least_common.count else '0'
        if len(co2_scrubber_ratings) > 1:
            co2_scrubber_ratings = [diagnostic for diagnostic in co2_scrubber_ratings if diagnostic[column] == target_co2_scrubber_digit]

    return co2_scrubber_ratings[0]


if __name__ == '__main__':
    with open('./input.txt') as f:
        diagnostics = [line.strip() for line in f.readlines()]
        power_consumption = get_power_consumption(diagnostics)
        oxygen_generator_rating = get_oxygen_generator_rating(diagnostics)
        co2_scrubber_rating = get_co2_scrubber_rating(diagnostics)
        life_support_rating = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
        print('Power consumption: {}'.format(power_consumption))
        print('Life support rating: {}'.format(life_support_rating))
