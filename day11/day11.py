def step(octopi):
    flash_ct = 0
    next_octopi = [[energy_lvl + 1 for energy_lvl in row] for row in octopi]

    flashing_octopi = []
    for y in range(len(octopi)):
        for x in range(len(octopi[0])):
            if next_octopi[y][x] == 10:
                flashing_octopi += [(x, y)]

    while len(flashing_octopi):
        flash_ct += 1
        x, y = flashing_octopi.pop()
        for adj_y in range(y - 1, y + 2):
            for adj_x in range(x - 1, x + 2):
                is_out_of_bounds = adj_x < 0 or adj_x >= len(octopi[0]) or adj_y < 0 or adj_y >= len(octopi)
                is_original_flasher = adj_x == x and adj_y == y
                if not is_out_of_bounds and not is_original_flasher:
                    next_octopi[adj_y][adj_x] += 1
                    if next_octopi[adj_y][adj_x] == 10:
                        flashing_octopi += [(adj_x, adj_y)]

    for y in range(len(octopi)):
        for x in range(len(octopi[0])):
            if next_octopi[y][x] >= 10:
                next_octopi[y][x] = 0

    return flash_ct, next_octopi


if __name__ == '__main__':
    with open('./input.txt') as f:
        input = [line.strip() for line in f.readlines()]
        octopi = [[int(energy_lvl)for energy_lvl in line] for line in input]
        step_ct = 0
        flashes_after_100_steps = 0
        first_synchronized_flash = None
        while first_synchronized_flash == None:
            step_ct += 1
            step_flash_ct, octopi = step(octopi)
            if step_ct <= 100:
                flashes_after_100_steps += step_flash_ct
            if step_flash_ct == len(octopi) * len(octopi[0]):
                first_synchronized_flash = step_ct

        print('Total flashes after 100 steps: {}'.format(flashes_after_100_steps))
        print('First synchronized flash: Step {}'.format(first_synchronized_flash))
