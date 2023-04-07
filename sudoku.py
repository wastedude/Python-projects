class Sudoku:
    def __init__(self, puzzle):
        self.grid = puzzle

    def display(self):
        for i in range(9):
            for j in range(9):
                print(self.grid[i][j], end=' ')
                if (j + 1) % 3 == 0 and j != 8:
                    print('|', end=' ')
            print()
            if (i + 1) % 3 == 0 and i != 8:
                print('-' * 22)

    def is_valid(self, row, col, num):
        # Check row
        if num in self.grid[row]:
            return False

        # Check column
        if num in [self.grid[i][col] for i in range(9)]:
            return False

        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.grid[i][j] == num:
                    return False

        # All checks passed
        return True

    def is_solved(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return False
        return True

    def get_next_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return (i, j)
        return None

    def solve(self):
        if self.is_solved():
            return True

        row, col = self.get_next_empty_cell()
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num

                if self.solve():
                    return True

                self.grid[row][col] = 0

        return False
