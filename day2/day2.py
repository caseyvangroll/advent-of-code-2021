def calculate_sub_position(movements):
    horizontal_position = 0
    depth = 0
    for movement in movements:
        [direction, magnitude] = movement.split(' ')
        if direction == 'forward':
            horizontal_position += int(magnitude)
        elif direction == 'down':
            depth += int(magnitude)
        elif direction == 'up':
            depth -= int(magnitude)

    return horizontal_position, depth


if __name__ == '__main__':
    with open('./input.txt') as f:
        movements = [line.strip() for line in f.readlines()]
        horizontal_position, depth = calculate_sub_position(movements)
        print('Final horizontal position: {}'.format(horizontal_position))
        print('Final depth: {}'.format(depth))
        print('Multiplied together: {}'.format(horizontal_position * depth))
