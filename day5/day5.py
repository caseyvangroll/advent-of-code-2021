from collections import namedtuple

Point = namedtuple('Point', 'x y')
Line = namedtuple('Line', 'start end')


def get_cells_of_line(line):
    x = line.start.x
    y = line.start.y
    cells = []
    y_delta = 0
    if line.start.y < line.end.y:
        y_delta = 1
    elif line.start.y > line.end.y:
        y_delta = -1
    x_delta = 0
    if line.start.x < line.end.x:
        x_delta = 1
    elif line.start.x > line.end.x:
        x_delta = -1
    while x != line.end.x or y != line.end.y:
        cells.append(str([x, y]))
        x += x_delta
        y += y_delta
    cells.append(str([x, y]))
    return cells


def count_cells_of_overlap(lines):
    counts = dict()
    for line in lines:
        cells_of_line = get_cells_of_line(line)
        for cell in cells_of_line:
            if cell not in counts:
                counts[cell] = 0
            counts[cell] += 1

    cells_of_overlap = filter(lambda item: item[1] > 1, counts.items())
    return len(cells_of_overlap)


def is_horizontal_or_vertical(line):
    return line.start.x == line.end.x or line.start.y == line.end.y


def is_diagonal(line):
    return abs(line.end.y - line.start.y) == abs(line.end.x - line.start.x)


def parse_input(inputs):
    lines = []
    for input in inputs:
        start, end = [Point(*[int(coord) for coord in coords.split(',')]) for coords in input.split(' -> ')]
        lines.append(Line(start, end))

    return filter(lambda line: is_horizontal_or_vertical(line) or is_diagonal(line), lines)


if __name__ == '__main__':
    with open('./input.txt') as f:
        lines = parse_input([line.strip() for line in f.readlines()])
        cells_of_overlap = count_cells_of_overlap(lines)
        print('Lines overlap in {} cells.'.format(cells_of_overlap))
