from collections import Counter

if True:
    x = 1

print(x)


def analyze_diagnostics(diagnostics):
    gamma_rate = ''
    epsilon_rate = ''

    for column in range(len(diagnostics[0])):
        digits_in_column = [diagnostic[column] for diagnostic in diagnostics]
        counter = Counter(digits_in_column)

        # Make safe for case where column is entirely one digit
        if '0' not in counter:
            counter['0'] = 0
        elif '1' not in counter:
            counter['1'] = 0

        most_common, least_common = Counter(digits_in_column).most_common()
        gamma_rate += most_common[0]
        epsilon_rate += least_common[0]

    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)

    # Use gamma_rate and epsilon_rate to find
    oxygen_generator_rating = 0
    co2_scrubber_rating = 0

    life_support_rating = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)

    return power_consumption, life_support_rating


if __name__ == '__main__':
    with open('./input.txt') as f:
        diagnostics = [line.strip() for line in f.readlines()]
        power_consumption, life_support_rating = analyze_diagnostics(diagnostics)
        print('Power consumption: {}'.format(power_consumption))
        print('Life support rating: {}'.format(life_support_rating))
