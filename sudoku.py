board = [[9,1,5,3,0,0,6,7,0],
         [6,8,0,1,0,7,0,4,0],
         [4,2,7,5,6,0,0,0,0],
         [8,0,1,0,2,6,3,5,4],
         [0,4,0,0,0,1,0,0,0],
         [0,0,0,0,0,0,0,1,0],
         [0,6,0,2,0,0,0,0,0],
         [5,0,8,7,3,0,1,0,6],
         [0,0,0,6,8,0,0,9,7]]


# Tech with Tim's code
def display_board(b):

    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")


def valid(b, row, col, val):
    # checks row and col
    for z in range(9):
        if b[row][z] == val or b[z][col] == val:
            return False
    
    # check the box
    box = get_box(board, row, col)
    if val in box:
        return False

    return True


def get_box(b, r, c):

    box = []
    # help from Python Enthusiast youtube channel
    # finds the start of the 3x3 square 

    square_x = (c // 3) * 3
    square_y = (r // 3) * 3
    
    for x in range(0,3):
        for y in range(0,3):
            box.append(b[y + square_x][x + square_y])

    return box