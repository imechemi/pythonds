class Sudoku:

    def __init__(self):
        # self.map = [
        #     [0] * 9, 
        #     [0] * 9,
        #     [0] * 9,
        #     [0] * 9,
        #     [0] * 9,
        #     [0] * 9,
        #     [0] * 9,
        #     [0] * 9,
        #     [0] * 9
        # ]

        self.map = [
            [0, 2, 0, 0, 0, 0, 0, 0, 3],
            [6, 0, 0, 0, 3, 1, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 8, 4],
            [3, 7, 0, 0, 0, 0, 5, 0, 1],
            [0, 0, 0, 0, 6, 0, 0, 0, 9],
            [0, 0, 0, 4, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 7, 8, 0, 0],
            [2, 0, 0, 0, 9, 0, 0, 4, 0],
            [0, 5, 0, 2, 0, 0, 1, 0, 0]
        ]
    
    def set_num(self, row, col, num):
        self.map[row][col] = num 
    
    def get_num(self, row, col):
        return self.map[row][col]
    
    def print_board(self):
        for row in range(9):
            for col in range(9):
                print(self.map[row][col], end=' ')
            print(end="\n")

    def solve_piece(self, r, c):
        status = {
            1: False, 2: False, 3: False,
            4: False, 5: False, 6: False,
            7: False, 8: False, 9: False
        }

        # Check by comparing alternate rows/cols
        
        
        # Check row
        for col in range(9):
            if col == c:
                pass 
            current_value = self.map[r][col]
            if current_value != 0:
                status[current_value] = True
        
        # Check column
        for row in range(9):
            current_value = self.map[row][c]
            if row == r: 
                pass 
            if current_value != 0:
                status[current_value] = True
        
        # Check box 
        start_row, start_col = 0, 0
        if r > 2 and r < 6:
            start_row = 3
        elif r > 5 and r < 9:
            start_row = 6
        
        if c > 2 and c < 6: 
            start_col = 3
        elif c > 5 and c < 9:
            start_col = 6

        for row in range(start_row, start_row + 3):
            if row == r: pass
            for col in range(start_col, start_col + 3):
                if (col == c): pass
                current_value = self.map[row][col]
                if current_value != 0:
                    status[current_value] = True

        if list(status.values()).count(False) == 1:
            idx = list(status.values()).index(False)
            self.set_num(r, c, idx + 1)
            return True
        return False

    def set_board(self):
        for row in range(9):
            for col in range(9):
                self.map[row][col] = int(input("Enter value for board[%d][%d]: " %(row+1, col+1)))

    def solve(self):
        pieces_to_solve = {}
        for row in range(9):
            for col in range(9):
                if self.map[row][col] == 0:
                    pieces_to_solve[str(row) + str(col)] = 1

        prev_count = len(pieces_to_solve) + 1
        while(len(pieces_to_solve) < prev_count):
            prev_count = len(pieces_to_solve)
            for row in range(9):
                for col in range(9):
                    if self.map[row][col] == 0:
                        if self.solve_piece(row, col):
                            del pieces_to_solve[str(row) + str(col)]
            
            self.print_board()



s = Sudoku()
s.set_board()
ch = 'y'
ch = input("Do you want to edit again [y/n] ?: ")
while(ch == 'y'):
    print("Enter row and column to edit")
    row = int(input("Enter row number: "))
    col = int(input("Enter column number: "))
    num = int(input("Enter value to place: "))
    s.set_num(row-1, col-1, num)
    s.print_board()
    ch = input("Do you want to edit again [y/n] ?: ")


s.print_board()
s.solve()
