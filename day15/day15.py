def find_lowest_risk_path(grid):
    print(grid)


if __name__ == '__main__':
    with open('./sample_input.txt') as f:
        grid = [[int(cell) for cell in line.strip()] for line in f.readlines()]
        lowest_risk_path = find_lowest_risk_path(grid)
        print('Lowest risk path: {}'.format(lowest_risk_path))


# plan:
#   1. maintain list of explored paths (breadth-first)
#   2. only ever explore shortest path(s) in list of paths to explore
#   3. maintain marker at each cell with whether it's been visited before and the cost of its previous visit (use this to prune paths to explore)
#   4. if see goal then have found shortest path (because of #2)
