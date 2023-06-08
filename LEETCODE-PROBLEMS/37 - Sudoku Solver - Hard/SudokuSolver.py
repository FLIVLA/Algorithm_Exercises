class SudokuSolver(object): 
    # recursion counter   
    def __init__(self):
        self.rec = 0
    
    # prints matrix in table format
    def printer(self, rec, matrix):
        hor = "-------------------------------------"
        print(hor)
        for r in range(len(matrix)):
            l = "| "
            for c in range(len(matrix[r])):
                l += str(matrix[r][c])
                l += " | "
            print(l)
            print(hor)
    
    # validates n for position x, y
    def validate_n(self, matrix, y, x, n):
        for i in range(0, 9):
            if matrix[y][i] == n:
                return False
        for i in range(0, 9):
            if matrix[i][x] == n:
                return False
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if matrix[y0 + i][x0 + j] == n:
                    return False
        return True 
    
    # recursive function for solving matrix
    def solve(self, matrix):
        self.rec += 1
        for y in range(9):
            for x in range(9):
                if matrix[y][x] == 0:
                    for n in range(1, 10):
                        if self.validate_n(matrix, y, x, n):
                            matrix[y][x] = n
                            self.solve(matrix)
                            matrix[y][x] = 0
                    return
        self.printer(5, matrix)
        print("Recursions: ", self.rec)


# --------------- TEST ---------------
solver = SudokuSolver()
matrix = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solver.solve(matrix)

