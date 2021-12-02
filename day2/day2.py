def calculate_sub_position(movements):
    horizontal_position = 0
    depth = 0
    aim = 0

    for direction, magnitude in movements:
        if direction == 'forward':
            horizontal_position += magnitude
            depth += magnitude * aim
        elif direction == 'down':
            aim += magnitude
        elif direction == 'up':
            aim -= magnitude

    return horizontal_position, depth


if __name__ == '__main__':
    with open('./input.txt') as f:
        movements = [line.strip().split(' ') for line in f.readlines()]
        horizontal_position, depth = calculate_sub_position([
            (direction, int(magnitude))
            for (direction, magnitude)
            in movements
        ])
        print('Final horizontal position: {}'.format(horizontal_position))
        print('Final depth: {}'.format(depth))
        print('Multiplied together: {}'.format(horizontal_position * depth))
