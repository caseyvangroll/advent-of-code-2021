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

# pseudocode:

# paths_to_explore = []
# shortest_paths_to_each_cell = Infinity for each cell
# push first 2 paths from upper right into paths_to_explore

# while len(paths_to_explore):
#   grab shortest_paths_to_explore from paths_to_explore
#   for each path in shortest_paths_to_explore:
#     determine next node(s) to explore in path (whichever nodes path hasn't seen AND result in lowest value for path AND haven't been visited by another shorter path)
#     if next node(s) includes end node stop and return this path
#     next_paths = this path + next node(s)
#     for next_path in next_paths:
#       if ending in a node that hasn't been visited before or has only been visited by a longer path:
#         update shortest_paths_to_each_cell to contain this path's cost
#     drop next_pathsinto paths_to_explore along with their corresponding costs
