from collections import namedtuple
import re

Point = namedtuple('Point', 'x y')
Target = namedtuple('Target', 'min max')


def get_min_initial_dx(target):
    for i in range(1, target.max.x):
        if target.min.x <= sum(range(1, i + 1)) <= target.max.x:
            return i


def simulate(target, initial_dx, initial_dy):
    x = 0
    y = 0
    dx = initial_dx
    dy = initial_dy
    positions = []
    hit_target = False
    while y >= target.min.y:
        if target.min.x <= x <= target.max.x and target.min.y <= y <= target.max.y:
            hit_target = True
        positions += [(x, y)]
        x += dx
        y += dy
        if dx > 0:
            dx -= 1
        if dx < 0:
            dx += 1
        dy -= 1
    return hit_target, positions


def part_one(target):
    min_initial_dx = get_min_initial_dx(target)
    max_initial_dy = abs(target.min.y) - 1
    hit_target, positions = simulate(target, min_initial_dx, max_initial_dy)
    max_y = max([y for x, y in positions])
    print('Max y position reached: {}'.format(max_y))
    return min_initial_dx, max_initial_dy


def part_two(target, min_initial_dx, max_initial_dy):
    max_initial_dx = target.max.x
    min_initial_dy = target.min.y

    velocities_that_hit_target = []
    for initial_dx in range(min_initial_dx, max_initial_dx + 1):
        for initial_dy in range(min_initial_dy, max_initial_dy + 1):
            hit_target, positions = simulate(target, initial_dx, initial_dy)
            if hit_target:
                velocities_that_hit_target += [(initial_dx, initial_dy)]

    print('Unique initial velocities that hit target {}'.format(len(velocities_that_hit_target)))


if __name__ == '__main__':
    with open('./input.txt') as f:
        input = f.readline().strip()
        min_x, max_x, min_y, max_y = [int(num) for num in re.findall(r'\-?\d+', input)]
        target = Target(Point(min_x, min_y), Point(max_x, max_y))
        min_initial_dx, max_initial_dy = part_one(target)
        part_two(target, min_initial_dx, max_initial_dy)
