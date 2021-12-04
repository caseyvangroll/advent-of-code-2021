def bold(s):
    return '\033[1m' + s + '\033[0m'


class BingoBoard():
    def __init__(self, numbers):
        self.numbers = [row.split() for row in numbers]
        self.marked_cells = [[False] * 5 for _ in range(5)]

    def check_number(self, number):
        has_win = False
        for row_idx, row in enumerate(self.numbers):
            for col_idx, cell in enumerate(row):
                if cell == number:
                    self.marked_cells[row_idx][col_idx] = True
                    has_win = self.check_win(row_idx, col_idx)
        return has_win

    def check_win(self, row_idx, col_idx):
        row = self.marked_cells[row_idx]
        col = [row[col_idx] for row in self.marked_cells]
        return all(row) or all(col)

    def print_win(self, last_called_number):
        print('Winning board:')
        print(self)
        sum_of_all_unmarked = 0
        for row_idx, row in enumerate(self.numbers):
            for col_idx, cell in enumerate(row):
                if not self.marked_cells[row_idx][col_idx]:
                    sum_of_all_unmarked += int(cell)
        final_score = sum_of_all_unmarked * int(last_called_number)
        print('Final score: {}'.format(final_score))

    def __str__(self):
        result = '\n'
        for row_idx, row in enumerate(self.numbers):
            for col_idx, cell in enumerate(row):
                if self.marked_cells[row_idx][col_idx]:
                    result += bold(cell.rjust(3))
                else:
                    result += cell.rjust(3)
            result += '\n'
        return result


def parseInput(lines):
    called_numbers = lines[0].split(',')
    bingo_board_inputs = [lines[i: i + 5] for i in range(1, len(lines), 5)]
    bingo_boards = [BingoBoard(input) for input in bingo_board_inputs]
    return called_numbers, bingo_boards


if __name__ == '__main__':
    with open('./input.txt') as f:
        called_numbers, bingo_boards = parseInput([line.strip() for line in f.readlines() if line.strip() != ''])
        for number in called_numbers:
            for board in bingo_boards:
                board_has_win = board.check_number(number)
                if board_has_win:
                    board.print_win(number)
                    exit(0)
