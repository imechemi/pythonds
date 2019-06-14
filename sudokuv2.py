debug = False 

class Cell:

    def __init__(self, r, c):
        self.notes = list(range(1, 10))
        self.value = 0
        self.row = r
        self.col = c 
    
    def note(self, n):
        self.notes.insert(n-1, n)

    def unnote(self, n):
        if n in self.notes: 
            self.notes.remove(n)

    def __str__(self):
        return str(self.value)

    def show_notes(self):
        res = ''
        for n in range(8):
            res = res + str(self.notes[n]) + ", "
        return res + str(self.notes[8])

class Sudoku:
    def __init__(self):
        self.board = [
            [0] * 9, 
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9
        ]
        for row in range(9):
            for col in range(9):
                self.board[row][col] = Cell(row, col)
    
    def set_board(self, values):
        i = 0
        for row in range(9):
            for col in range(9):
                self.board[row][col].value = values[i]
                if values[i] != 0:
                    self.board[row][col].notes = []
                i = i + 1

    def display(self):
        
        for row in range(9):
            for col in range(9):
                print(self.board[row][col], end=' ')
            print(end="\n")

    def solve_cell(self, r, c):
        freq = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: []
        }

        # Box 
        start_col = 0
        start_row = 0

        if r > 2 and r < 6: 
            start_row = 3
        elif r > 5 and r < 9:
            start_row = 6

        if c > 2 and c < 6: 
            start_col = 3
        elif c > 5 and c < 9:
            start_col = 6      

        for row in range(start_row, start_row+3):
            for col in range(start_col, start_col+3):
                if self.board[row][col].value != 0:
                    self.board[r][c].unnote(self.board[row][col].value)
                    freq[self.board[row][col].value].append(self.board[row][col])

        to_unnote = []
        for f in freq:
            if len(freq[f]) == 1:
                print(freq[f][0].row)
                target_cell = self.board[freq[f][0].row][freq[f][0].col] 
                target_cell.value = freq[f][0].value
                target_cell.notes = []
                to_unnote.append(target_cell.value)

        # Column 
        for row in range(9):
            if row != r and self.board[row][c].value != 0:
                self.board[r][c].unnote(self.board[row][c].value)

        # Row
        for col in range(9):
            if col != c and self.board[r][col].value != 0:
                self.board[r][c].unnote(self.board[r][col].value)

        #print("After notes for", r, c, ": ", self.board[r][c].notes)

        nlist = set(self.board[r][c].notes)
        print("Length = ", len(self.board[r][c].notes))
        if len(self.board[r][c].notes) == 1:
            found = self.board[r][c].notes[0] #list(nlist - set([0]))[0]
            print("Found = ", found)
            self.board[r][c].value = found
            return True
        
        return False 


    def solve(self):
        change_observed = False
        while True:
            print("#" * 100)
            self.display()
            change_observed = False 
            for row in range(9):
                for col in range(9):
                    #print("Value ", row, col, ": ", self.board[row][col].value)
                    if self.board[row][col].value == 0:
                        prev_notes = self.board[row][col].notes.copy()
                        self.solve_cell(row, col)
                        current_notes = self.board[row][col].notes
                        print("Prev notes: [",row, ",", col, "]", prev_notes)
                        print("Curr notes: [",row, ",", col, "]", current_notes)
                        if len(prev_notes) > len(current_notes):
                            change_observed = True         

            if change_observed == False:
                break
        



su = Sudoku()
# su.set_board(
#     [
#         0,3,4,0,0,0,0,6,0,
#         0,0,0,0,0,0,9,0,0,
#         0,0,9,0,0,4,8,0,5,
#         5,6,0,0,2,7,0,0,0,
#         0,0,0,0,8,0,0,0,2,
#         0,0,0,0,0,0,0,0,0,
#         9,0,0,0,0,0,0,4,0,
#         8,0,0,3,0,0,6,0,0,
#         0,7,0,2,5,0,0,0,0
#     ]
# )

# su.set_board(
#     [
#         5,0,8,4,0,2,0,0,1,
#         3,0,0,9,5,1,0,7,8,
#         1,0,0,6,0,0,0,0,5,
#         0,3,4,0,8,9,0,2,0,
#         0,0,0,1,2,3,0,9,7,
#         0,1,9,7,4,6,0,0,3,
#         0,0,1,0,0,0,0,6,0,
#         0,2,6,8,0,0,0,0,4,
#         0,7,0,0,0,0,0,1,0
#     ]
# )

su.set_board(
    [
        0,0,0,0,0,0,9,0,0,
        0,0,9,0,4,3,0,8,0,
        3,0,0,7,0,1,0,0,0,
        0,0,0,0,8,0,0,0,9,
        0,0,5,0,0,0,0,6,0,
        4,6,0,0,0,0,5,0,0,
        0,0,8,6,0,0,0,4,0,
        0,5,0,0,7,0,0,0,0,
        0,4,0,1,5,0,7,2,0
    ]
)

print("Before")
su.display()
su.solve()

print("After")
su.display()