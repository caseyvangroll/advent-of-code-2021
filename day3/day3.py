from collections import Counter


def analyze_diagnostics(diagnostics):
    gamma_rate = ''
    epsilon_rate = ''
    life_support_rating = 0
    oxygen_generator_ratings = [*diagnostics]
    co2_scrubber_ratings = [*diagnostics]

    for column in range(len(diagnostics[0])):
        digits_in_column = [diagnostic[column] for diagnostic in diagnostics]
        counter = Counter(digits_in_column)

        # Make safe for case where column is entirely one digit
        if '0' not in counter:
            counter['0'] = 0
        elif '1' not in counter:
            counter['1'] = 0

        (most_common_digit, most_common_ct), (least_common_digit, least_common_ct) = Counter(digits_in_column).most_common()

        gamma_rate += most_common_digit
        epsilon_rate += least_common_digit

        target_oxygen_generator_digit = most_common_digit if most_common_ct != least_common_ct else '1'
        target_co2_srubber_digit = least_common_digit if most_common_ct != least_common_ct else '0'

        if len(oxygen_generator_ratings) > 1:
            oxygen_generator_ratings = [
                diagnostic for diagnostic in oxygen_generator_ratings if diagnostic[column] == target_oxygen_generator_digit]
        if len(co2_scrubber_ratings) > 1:
            co2_scrubber_ratings = [
                diagnostic for diagnostic in co2_scrubber_ratings if diagnostic[column] == target_co2_srubber_digit]

    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    life_support_rating = int(oxygen_generator_ratings[0], 2) * int(co2_scrubber_ratings[0], 2)

    return power_consumption, life_support_rating


if __name__ == '__main__':
    with open('./input.txt') as f:
        diagnostics = [line.strip() for line in f.readlines()]
        power_consumption, life_support_rating = analyze_diagnostics(diagnostics)
        print('Power consumption: {}'.format(power_consumption))
        print('Life support rating: {}'.format(life_support_rating))
