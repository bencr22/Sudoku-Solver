import sudoku


def solve(b):
    
    for i in range(9):
        for j in range(9):
            for number in range(1,10):
                if sudoku.valid(b, i, j, number):
                    b[i][j] = number
                    solve(b)
                    # this solution may not be correct so backtrack
                    # reset the value incase wrong
                    b[i][j] = 0
            

    sudoku.display_board(b)


solve(sudoku.board)