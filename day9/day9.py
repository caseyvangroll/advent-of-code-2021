import pdb
from functools import reduce

UP = 'UP'
RIGHT = 'RIGHT'
DOWN = 'DOWN'
LEFT = 'LEFT'
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]


def get_adjacent_cell(rows, x, y, dir):
    adj_x = x
    adj_y = y
    adj_cell = None
    if dir == UP:
        adj_y -= 1
    if dir == RIGHT:
        adj_x += 1
    if dir == DOWN:
        adj_y += 1
    if dir == LEFT:
        adj_x -= 1
    if 0 <= adj_y < len(rows) and 0 <= adj_x < len(rows[0]):
        adj_cell = rows[adj_y][adj_x]
    return adj_x, adj_y, adj_cell


def get_low_points(rows):
    low_points = []
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            cell = rows[y][x]
            adjacent_cells = [get_adjacent_cell(rows, x, y, dir) for dir in DIRECTIONS]
            if all([adj_cell is None or cell < adj_cell for adj_x, adj_y, adj_cell in adjacent_cells]):
                low_points.append((x, y))

    return low_points


def get_basin(rows, low_point):
    cells_in_basin = set([low_point])
    cells_to_check = set([low_point])
    cells_checked = set()

    while len(cells_to_check):
        x, y = cells_to_check.pop()
        if str((x, y)) not in cells_checked:
            cell = rows[y][x]
            cells_checked.add(str((x, y)))

            adjacent_cells = [get_adjacent_cell(rows, x, y, dir) for dir in DIRECTIONS]
            for adj_x, adj_y, adj_cell in adjacent_cells:
                already_checked = str((adj_x, adj_y)) in cells_checked
                is_part_of_basin = adj_cell != None and adj_cell != '9' and cell < adj_cell
                if not already_checked and is_part_of_basin:
                    cells_in_basin.add((adj_x, adj_y))
                    cells_to_check.add((adj_x, adj_y))

    return cells_in_basin


if __name__ == '__main__':
    with open('./input.txt') as f:
        rows = [line.strip() for line in f.readlines()]
        low_points = get_low_points(rows)
        low_point_risk_level_sum = sum([1 + int(rows[y][x]) for x, y in low_points])
        print("Sum of risk level of low points: {}".format(low_point_risk_level_sum))

        basins = [get_basin(rows, low_point) for low_point in low_points]
        basin_sizes = sorted([len(basin) for basin in basins])
        sum_of_three_largest_basin_sizes = reduce(lambda acc, x: acc * x, basin_sizes[-3:], 1)
        print("Product of three largest basin sizes: {}".format(sum_of_three_largest_basin_sizes))
