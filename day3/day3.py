from collections import Counter


def get_power_consumption(diagnostics):
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

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


if __name__ == '__main__':
    with open('./input.txt') as f:
        diagnostics = [line.strip() for line in f.readlines()]
        power_consumption = get_power_consumption(diagnostics)
        print('Power consumption: {}'.format(power_consumption))
