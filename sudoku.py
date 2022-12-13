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

    if c < 3:
        # top left
        if r < 3:
            box = [b[0][0], b[0][1], b[0][2], b[1][0], b[1][1], b[1][2], b[2][0], b[2][1], b[2][2]]
        # bottom left
        elif r > 5:
            box = [b[6][0], b[6][1], b[6][2], b[7][0], b[7][1], b[7][2], b[8][0], b[8][1], b[8][2]]
        # middle left
        else:
            box = [b[3][0], b[3][1], b[3][2], b[4][0], b[4][1], b[4][2], b[5][0], b[5][1], b[5][2]]
    elif c > 5:
        # top right
        if r < 3:
            box = [b[0][6], b[0][7], b[0][8], b[1][6], b[1][7], b[1][8], b[2][6], b[2][7], b[2][8]]
        # bottom right
        elif r > 5:
            box = [b[6][6], b[6][7], b[6][8], b[7][6], b[7][7], b[7][8], b[8][6], b[8][7], b[8][8]]
        # middle right
        else:
            box = [b[3][6], b[3][7], b[3][8], b[4][6], b[4][7], b[4][8], b[5][6], b[5][7], b[5][8]]
    else:
        # top middle
        if r < 3:
            box = [b[0][3], b[0][4], b[0][5], b[1][3], b[1][4], b[1][5], b[2][3], b[2][4], b[2][5]]
        # bottom middle
        elif r > 5:
            box = [b[6][3], b[6][4], b[6][5], b[7][3], b[7][4], b[7][5], b[8][3], b[8][4], b[8][5]]
        # middle
        else:
            box = [b[3][3], b[3][4], b[3][5], b[4][3], b[4][4], b[4][5], b[5][3], b[5][4], b[5][5]]

    return box



