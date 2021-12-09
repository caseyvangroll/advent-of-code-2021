from functools import reduce


def get_low_points(rows):
    low_points = []
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            cell = rows[y][x]
            is_lower_than_up = y <= 0 or rows[y - 1][x] > cell
            is_lower_than_right = x >= len(rows[y]) - 1 or rows[y][x + 1] > cell
            is_lower_than_down = y >= len(rows) - 1 or rows[y + 1][x] > cell
            is_lower_than_left = x <= 0 or rows[y][x - 1] > cell
            if all([is_lower_than_up, is_lower_than_right, is_lower_than_down, is_lower_than_left]):
                low_points.append((x, y))

    return low_points


def get_basin(rows, low_point):
    cells_in_basin = [low_point]
    cells_to_check = [low_point]
    cells_seen = dict()

    while len(cells_to_check):
        x, y = cells_to_check.pop(0)
        if str((x, y)) not in cells_seen:
            cells_seen[str((x, y))] = True
            is_up_in_basin = y > 0 and rows[y - 1][x] > rows[y][x] and rows[y - 1][x] != 9
            is_right_in_basin = x < len(rows[y]) - 1 and rows[y][x + 1] > rows[y][x] and rows[y][x + 1] != 9
            is_down_in_basin = y < len(rows) - 1 and rows[y + 1][x] > rows[y][x] and rows[y + 1][x] != 9
            is_left_in_basin = x > 0 and rows[y][x - 1] > rows[y][x] and rows[y][x - 1] != 9

            if is_up_in_basin and str((y - 1, x)) not in cells_seen:
                cells_in_basin.append((y - 1, x))
                cells_to_check.append((y - 1, x))
            if is_right_in_basin and str((y, x + 1)) not in cells_seen:
                cells_in_basin.append((y, x + 1))
                cells_to_check.append((y, x + 1))
            if is_down_in_basin and str((y + 1, x)) not in cells_seen:
                cells_in_basin.append((y + 1, x))
                cells_to_check.append((y + 1, x))
            if is_left_in_basin and str((y, x - 1)) not in cells_seen:
                cells_in_basin.append((y, x - 1))
                cells_to_check.append((y, x - 1))

    return cells_in_basin


if __name__ == '__main__':
    with open('./input.txt') as f:
        rows = [line.strip() for line in f.readlines()]
        low_points = get_low_points(rows)
        low_point_risk_level_sum = sum([1 + int(rows[y][x]) for x, y in low_points])
        print("Sum of risk level of low points: {}".format(low_point_risk_level_sum))

        basins = [get_basin(rows, low_point) for low_point in low_points]
        three_largest_basin_sizes = [len(basin) for basin in basins[-3]]
        print("Product of three largest basin sizes: {}".format(reduce(lambda acc, x: acc + x, three_largest_basin_sizes, 1)))

# not 73
