from collections import namedtuple
from queue import PriorityQueue

Path = namedtuple('Path', 'cost prev_cell')


def find_lowest_risk_path(grid):
    width = len(grid[0])
    height = len(grid)

    paths_to_explore = PriorityQueue(0)
    paths_to_explore.put((grid[1][0], (0, 1)))
    paths_to_explore.put((grid[0][1], (1, 0)))

    best_paths = [[Path(None, None)] * width for _ in range(height)]
    best_paths[1][0] = Path(grid[1][0], (0, 0))
    best_paths[0][1] = Path(grid[0][1], (0, 0))

    seen = dict()
    seen[(0, 0)] = True
    seen[(1, 0)] = True
    seen[(0, 1)] = True

    while paths_to_explore.qsize() > 0:
        cost, (x, y) = paths_to_explore.get()

        def check_adjacent_cell(x2, y2):
            if 0 <= x2 < width and 0 <= y2 < height and (
                best_paths[y2][x2].cost == None or
                cost + grid[y2][x2] < best_paths[y2][x2].cost
            ):
                best_paths[y2][x2] = Path(cost + grid[y2][x2], (x2, y2))
                if x2 == width - 1 and y2 == height - 1:
                    return cost + grid[y2][x2]
                if (x2, y2) not in seen:
                    seen[(x2, y2)] = True
                    paths_to_explore.put((cost + grid[y2][x2], (x2, y2)))

        finishing_costs = [
            finishing_cost for finishing_cost in [
                check_adjacent_cell(x, y - 1),
                check_adjacent_cell(x + 1, y),
                check_adjacent_cell(x, y + 1),
                check_adjacent_cell(x - 1, y)
            ] if finishing_cost != None
        ]

        if any(finishing_costs):
            return finishing_costs[0]


def quintuple_size(grid):
    quintuple_width_grid = []
    for row in grid:
        new_row = [x for x in row]
        for i in range(1, 5):
            new_row += [(x + i) % 9 if x + i > 9 else x + i for x in row]
        quintuple_width_grid.append(new_row)

    quintuple_grid = []
    for i in range(0, 5):
        for row in quintuple_width_grid:
            quintuple_grid.append([(x + i) % 9 if x + i > 9 else x + i for x in row])

    return quintuple_grid


if __name__ == '__main__':
    with open('./input.txt') as f:
        grid = [[int(cell) for cell in line.strip()] for line in f.readlines()]
        lowest_risk_path = find_lowest_risk_path(grid)
        print('Lowest risk path: {}'.format(lowest_risk_path))
        lowest_risk_path_2 = find_lowest_risk_path(quintuple_size(grid))
        print('Lowest risk path in expanded grid: {}'.format(lowest_risk_path_2))
