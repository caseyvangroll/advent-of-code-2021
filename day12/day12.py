import timeit


def traverse_cave(connections):
    unfinished_paths = [(['start', dest], None) for dest in connections['start']]
    successful_paths = []

    def is_visiting_repeat_small_cave(path):
        return path[-1].islower() and path[-1] in path[:-1]

    while len(unfinished_paths):
        unfinished_path, used_small_cave = unfinished_paths.pop(0)
        tail = unfinished_path[-1]
        continuations_of_path = [unfinished_path + [dest] for dest in connections[tail]]
        for continuation_of_path in continuations_of_path:
            if continuation_of_path[-1] == 'end':
                successful_paths.append('-'.join(continuation_of_path))
            elif not is_visiting_repeat_small_cave(continuation_of_path):
                unfinished_paths += [(continuation_of_path, used_small_cave)]
            elif used_small_cave == None:
                unfinished_paths += [(continuation_of_path, continuation_of_path[-1])]

    return successful_paths


if __name__ == '__main__':
    with open('./input.txt') as f:
        inputs = [line.strip().split('-') for line in f.readlines()]
        connections = dict()
        for node_a, node_b in inputs:
            if node_a not in connections:
                connections[node_a] = set()
            if node_b not in connections:
                connections[node_b] = set()
            if node_b != 'start':
                connections[node_a].add(node_b)
            if node_a != 'start':
                connections[node_b].add(node_a)

        start = timeit.default_timer()
        paths_that_visit_small_caves_at_most_once = traverse_cave(connections)
        stop = timeit.default_timer()
        print('(~{}s) Paths that visit small caves at most once: {}'.format(
            int(stop - start), len(paths_that_visit_small_caves_at_most_once)))
