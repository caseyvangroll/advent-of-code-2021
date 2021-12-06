def bold(s):
    return '\033[1m' + s + '\033[0m'


class BingoBoard():
    def __init__(self, idx, numbers):
        self.idx = idx
        self.numbers = [row.split() for row in numbers]
        self.marked_cells = [[False] * 5 for _ in range(5)]

    def check_number(self, number):
        has_win = False
        for row_idx, row in enumerate(self.numbers):
            for col_idx, cell in enumerate(row):
                if cell == number:
                    self.marked_cells[row_idx][col_idx] = True
                    has_win = has_win or self.check_win(row_idx, col_idx)
                    if (self.idx == 3):
                        print(number)
                        print(self)
        return has_win

    def check_win(self, row_idx, col_idx):
        marked_row = self.marked_cells[row_idx]
        marked_col = [row[col_idx] for row in self.marked_cells]
        return all(marked_row) or all(marked_col)

    def print_win(self, last_called_number):
        sum_of_all_unmarked = 0
        for row_idx, row in enumerate(self.numbers):
            for col_idx, cell in enumerate(row):
                if not self.marked_cells[row_idx][col_idx]:
                    sum_of_all_unmarked += int(cell)
        final_score = sum_of_all_unmarked * int(last_called_number)
        print('Board {} wins on {} with final score: {}'.format(self.idx, last_called_number, final_score))
        print(self)

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


def parse_input(lines):
    called_numbers = lines[0].split(',')
    bingo_board_inputs = [lines[i: i + 5] for i in range(1, len(lines), 5)]
    bingo_boards = [BingoBoard(idx, input) for idx, input in enumerate(bingo_board_inputs)]
    return called_numbers, bingo_boards


if __name__ == '__main__':
    with open('./input.txt') as f:
        called_numbers, bingo_boards = parse_input([line.strip() for line in f.readlines() if line.strip() != ''])
        for number in called_numbers:
            boards_to_remove = []
            for board in bingo_boards:
                if board.check_number(number):
                    board.print_win(number)
                    boards_to_remove.append(board)

            for board_to_remove in boards_to_remove:
                bingo_boards.remove(board_to_remove)
            if not len(bingo_boards):
                print('No boards left.')
                exit(0)
