from collections import namedtuple, Counter

Point = namedtuple('Point', 'x y')
Fold = namedtuple('Fold', 'x y')


class Paper():
    def __init__(self, points):
        width = max([point.x for point in points]) + 1
        height = max([point.y for point in points]) + 1
        self.lines = [['.'] * width for _ in range(height)]
        for point in points:
            self.lines[point.y][point.x] = '#'

    def fold(self, x, y):
        width = len(self.lines[0])
        height = len(self.lines)
        if x != None:
            shim = 0 if width % 2 == 0 else 1
            for i in range(x + 1, width):
                for j in range(height):
                    if self.lines[j][i] == '#':
                        self.lines[j][width - shim - i] = '#'

            self.lines = [line[:(width / 2)] for line in self.lines]
        elif y != None:
            shim = 0 if height % 2 == 0 else 1
            for j in range(y + 1, height):
                for i in range(width):
                    if self.lines[j][i] == '#':
                        self.lines[height - shim - j][i] = '#'

            self.lines = self.lines[:(height / 2)]

    def get_visible_dot_ct(self):
        visible_dot_ct = Counter()
        for line in self.lines:
            visible_dot_ct.update(line)
        return visible_dot_ct.get('#')

    def __str__(self):
        result = ''
        for line in self.lines:
            result += ''.join(line) + '\n'
        return result


def parse_input(input):
    def make_point(s):
        x, y = s.split(',')
        return Point(int(x), int(y))

    def make_fold(s):
        x = int(s.split('=')[1]) if 'x' in s else None
        y = int(s.split('=')[1]) if 'y' in s else None
        return Fold(x, y)

    points = [make_point(s) for s in input if ',' in s]
    paper = Paper(points)
    folds_to_make = [make_fold(s) for s in input if 'fold along ' in s]
    return paper, folds_to_make


if __name__ == '__main__':
    with open('./input.txt') as f:
        input = [line.strip() for line in f.readlines()]
        paper, folds_to_make = parse_input(input)
        first_fold = folds_to_make.pop(0)
        paper.fold(*first_fold)
        print('Visible dot ct after 1 fold: {}'.format(paper.get_visible_dot_ct()))
        for x, y in folds_to_make:
            paper.fold(x, y)
        print(paper)
