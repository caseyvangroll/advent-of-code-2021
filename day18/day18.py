from math import ceil, floor


def get_split_nums(x):
    f = float(x) / 2
    return int(floor(f)), int(ceil(f))


class SnailfishNum():
    def __init__(self, n):
        # Remove outermost brackets and all whitespace
        n = "".join(n[1:-1].split())
        brackets_to_close = 0
        for i in range(len(n)):
            if n[i] == ',' and brackets_to_close == 0:
                self.left = n[:i]
                self.right = n[i+1:]
                break
            if n[i] == '[':
                brackets_to_close += 1
            elif n[i] == ']':
                brackets_to_close -= 1

        if len(self.left):
            if self.left.isdigit():
                self.left = int(self.left)
            else:
                self.left = SnailfishNum(self.left)
        if len(self.right):
            if self.right.isdigit():
                self.right = int(self.right)
            else:
                self.right = SnailfishNum(self.right)

    # Returns true if an explode occurred in this SnailfishNum tree
    def explode(self, depth):
        # check if this node explodes
        if depth >= 4 and isinstance(self.left, int) and isinstance(self.right, int):
            return self.left, 0, self.right, True

        # check left subtree for explosions
        if isinstance(self.left, SnailfishNum):
            l, c, r, exploded = self.left.explode(depth + 1)
            if exploded:
                # immediate child exploded - replace with 0
                if c != None:
                    self.left = c
                    c = None
                # r from exploded node needs a home and we have one
                if r != None:
                    if isinstance(self.right, int):
                        self.right += r
                        r = None
                    elif self.right.find_home(r, True):
                        r = None
                return l, c, r, exploded

        # check right subtree for explosions
        if isinstance(self.right, SnailfishNum):
            l, c, r, exploded = self.right.explode(depth + 1)
            if exploded:
                # immediate child exploded - replace with 0
                if c != None:
                    self.right = c
                    c = None
                # r from exploded node needs a home and we have one
                if l != None:
                    if isinstance(self.left, int):
                        self.left += l
                        l = None
                    elif self.left.find_home(l, False):
                        l = None
                return l, c, r, exploded

        return None, None, None, False

    def find_home(self, x, check_left_first):
        if check_left_first:
            if isinstance(self.left, int):
                self.left += x
                return True
            if self.left.find_home(x, check_left_first):
                return True
            if isinstance(self.right, int):
                self.right += x
                return True
            if self.right.find_home(x, check_left_first):
                return True
        else:
            if isinstance(self.right, int):
                self.right += x
                return True
            if self.right.find_home(x, check_left_first):
                return True
            if isinstance(self.left, int):
                self.left += x
                return True
            if self.left.find_home(x, check_left_first):
                return True
        return False

    # Returns true if a split occurred in this SnailfishNum tree
    def split(self):
        if isinstance(self.left, SnailfishNum) and self.left.split():
            return True
        if isinstance(self.left, int) and self.left > 9:
            left, right = get_split_nums(self.left)
            self.left = SnailfishNum('[{},{}]'.format(left, right))
            return True
        if isinstance(self.right, int) and self.right > 9:
            left, right = get_split_nums(self.right)
            self.right = SnailfishNum('[{},{}]'.format(left, right))
            return True
        if isinstance(self.right, SnailfishNum) and self.right.split():
            return True
        return False

    def reduce(self):
        if self.explode(0)[-1]:
            return True
        if self.split():
            return True
        return False

    def magnitude(self):
        l_mag = self.left * 3 if isinstance(self.left, int) else self.left.magnitude() * 3
        r_mag = self.right * 2 if isinstance(self.right, int) else self.right.magnitude() * 2
        return l_mag + r_mag

    def __str__(self):
        return '[{},{}]'.format(str(self.left), str(self.right))


if __name__ == '__main__':
    with open('./input.txt') as f:
        input = [line.strip() for line in f.readlines()]
        result = input[0]
        for n in input[1:]:
            sum = SnailfishNum('[{},{}]'.format(str(result), n))
            while sum.reduce():
                pass
            result = str(sum)

        print('Result: {}'.format(result))
        print('Magnitude of result: {}'.format(SnailfishNum(result).magnitude()))

        combos = []
        ct = len(input)
        for i in range(ct):
            for j in range(ct):
                if i != j:
                    combos += [(input[i], input[j])]

        biggest_mag = 0
        for l, r in combos:
            sum = SnailfishNum('[{},{}]'.format(l, r))
            while sum.reduce():
                pass
            biggest_mag = max(sum.magnitude(), biggest_mag)
        print('Largest magnitude of 2 nums in list: {}'.format(biggest_mag))
