def find_lowest_risk_path(grid):
    print(grid)


if __name__ == '__main__':
    with open('./sample_input.txt') as f:
        grid = [[int(cell) for cell in line.strip()] for line in f.readlines()]
        lowest_risk_path = find_lowest_risk_path(grid)
        print('Lowest risk path: {}'.format(lowest_risk_path))


# plan: breadth-first search, keep shortest path to get to each cell
