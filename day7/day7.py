
# Algorithm:
#   Take turns moving in outermost crabs until all crabs in one spot.
#   If one side costs less to move in then only move that side.
#   Doesn't work for when the optimal spot to move to could be 2 spaces (evenly-distributed even-length distributions)

# Given the sample input [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]...
# (each position is an array of how much fuel it has spent to get each crab there)
# [[0], [0, 0], [0, 0, 0], [], [0], [], [], [0], [], [], [], [], [], [], [0], [], [0]]
# [[], [0, 0, 1], [0, 0, 0], [], [0], [], [], [0], [], [], [], [], [], [], [0], [1], []]
# [[], [0, 0, 1], [0, 0, 0], [], [0], [], [], [0], [], [], [], [], [], [], [0, 2], [], []]
# [[], [], [0, 0, 0, 1, 1, 2], [], [0], [], [], [0], [], [], [], [], [], [1, 3], [], [], []]
# [[], [], [0, 0, 0, 1, 1, 2], [], [0], [], [], [0], [], [], [], [], [2, 4], [], [], [], []]
# [[], [], [0, 0, 0, 1, 1, 2], [], [0], [], [], [0], [], [], [], [3, 5], [], [], [], [], []]
# [[], [], [], [1, 1, 1, 2, 2, 3], [0], [], [], [0], [], [], [4, 6], [], [], [], [], [], []]
# [[], [], [], [1, 1, 1, 2, 2, 3], [0], [], [], [0], [], [5, 7], [], [], [], [], [], [], []]
# [[], [], [], [1, 1, 1, 2, 2, 3], [0], [], [], [0], [6, 8], [], [], [], [], [], [], [], []]
# [[], [], [], [], [0, 2, 2, 2, 3, 3, 4], [], [], [0, 7, 9], [], [], [], [], [], [], [], [], []]
# [[], [], [], [], [0, 2, 2, 2, 3, 3, 4], [], [1, 8, 10], [], [], [], [], [], [], [], [], [], []]
# [[], [], [], [], [0, 2, 2, 2, 3, 3, 4], [2, 9, 11], [], [], [], [], [], [], [], [], [], [], []]
# [[], [], [], [], [0, 2, 2, 2, 3, 3, 4], [2, 9, 11], [], [], [], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [2, 9, 11, 1, 3, 3, 3, 4, 4, 5], [], [], [], [], [], [], [], [], [], [], []]

def calculate_alignment_fuel_cost(min_crab_position, max_crab_position, crabs_in_each_position):
    fuel_cost = 0
    while min_crab_position != max_crab_position:
        move_in_left = False
        move_in_right = False
        cost_to_move_in_left = sum(crabs_in_each_position[min_crab_position]) + len(crabs_in_each_position[min_crab_position])
        cost_to_move_in_right = sum(crabs_in_each_position[max_crab_position]) + len(crabs_in_each_position[max_crab_position])
        if cost_to_move_in_left <= cost_to_move_in_right:
            move_in_left = True
        if cost_to_move_in_right <= cost_to_move_in_left:
            move_in_right = True

        if move_in_left:
            fuel_cost += cost_to_move_in_left
            crabs_in_each_position[min_crab_position + 1] += [cost + 1 for cost in crabs_in_each_position[min_crab_position]]
            crabs_in_each_position[min_crab_position] = []
            min_crab_position += 1
        if move_in_right:
            fuel_cost += cost_to_move_in_right
            crabs_in_each_position[max_crab_position - 1] += [cost + 1 for cost in crabs_in_each_position[max_crab_position]]
            crabs_in_each_position[max_crab_position] = []
            max_crab_position -= 1

    return fuel_cost


def get_crabs_in_each_position(input):
    crabs_in_each_position = []
    min_crab_position = None
    max_crab_position = None
    for position in input:
        crab_position = int(position)
        if min_crab_position == None or crab_position < min_crab_position:
            min_crab_position = crab_position
        if max_crab_position == None or crab_position > max_crab_position:
            max_crab_position = crab_position
            len_difference = max_crab_position - len(crabs_in_each_position) + 1
            crabs_in_each_position += [[] for _ in range(len_difference)]
        crabs_in_each_position[crab_position].append(0)

    return min_crab_position, max_crab_position, crabs_in_each_position


if __name__ == '__main__':
    with open('./input.txt') as f:
        input = f.readline().strip().split(',')
        fuel_cost = calculate_alignment_fuel_cost(*get_crabs_in_each_position(input))
        print("Cost to align crabs: {}".format(fuel_cost))
