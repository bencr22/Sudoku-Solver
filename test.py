import sys


def display_board():
    global board

    # Tech with Tim's code
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def valid(row, col, val):
    global board

    # checks row and col
    for z in range(9):
        if board[row][z] == val or board[z][col] == val:
            return False
    
    # check the box

    # help from Python Enthusiast youtube channel
    # finds the start of the 3x3 square 
    square_x = (col // 3) * 3
    square_y = (row // 3) * 3
    
    for x in range(0,3):
        for y in range(0,3):
            if board[square_y + x][square_x + y] == val:
                return False

    return True


def solve():
    global board
    
    for i in range(9):
        for j in range(9):
            for number in range(1,10):
                if valid(i, j, number):
                    board[i][j] = number
                    solve()
                    # this solution may not be correct so backtrack
                    # reset the value incase wrong
                    board[i][j] = 0
            
                    return

board = [[9,1,5,3,0,0,6,7,0],
         [6,8,0,1,0,7,0,4,0],
         [4,2,7,5,6,0,0,0,0],
         [8,0,1,0,2,6,3,5,4],
         [0,4,0,0,0,1,0,0,0],
         [0,0,0,0,0,0,0,1,0],
         [0,6,0,2,0,0,0,0,0],
         [5,0,8,7,3,0,1,0,6],
         [0,0,0,6,8,0,0,9,7]]

sys.setrecursionlimit(2000)
solve()
display_board()