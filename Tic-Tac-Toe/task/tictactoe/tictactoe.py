a = input("Enter cells: > ")
a = list(a)
def print_board():
    print("---------")
    print("|", board[0][0],  board[0][1], board[0][2], "|")
    print("|", board[1][0],  board[1][1], board[1][2], "|")
    print("|", board[2][0],  board[2][1], board[2][2], "|")
    print("---------")

board = [
    [a[0], a[1], a[2]],
    [a[3], a[4], a[5]],
    [a[6], a[7], a[8]]
]
def x():
    if (a[0] == "X" and a[1] == "X" and a[2] == "X" or
            a[3] == "X" and a[4] == "X" and a[5] == "X" or
            a[6] == "X" and a[7] == "X" and a[8] == "X" or
            a[0] == "X" and a[3] == "X" and a[6] == "X" or
            a[1] == "X" and a[4] == "X" and a[7] == "X" or
            a[2] == "X" and a[5] == "X" and a[8] == "X" or
            a[0] == "X" and a[4] == "X" and a[8] == "X" or
            a[2] == "X" and a[4] == "X" and a[6] == "X"):
        return True
    else:
        return False


def o():
    if (a[0] == "O" and a[1] == "O" and a[2] == "O" or
            a[3] == "O" and a[4] == "O" and a[5] == "O" or
            a[6] == "O" and a[7] == "O" and a[8] == "O" or
            a[0] == "O" and a[3] == "O" and a[6] == "O" or
            a[1] == "O" and a[4] == "O" and a[7] == "O" or
            a[2] == "O" and a[5] == "O" and a[8] == "O" or
            a[0] == "O" and a[4] == "O" and a[8] == "O" or
            a[2] == "O" and a[4] == "O" and a[6] == "O"):
        return True
    else:
        return False


def _():
    if (a[0] == "_" or a[1] == "_" or a[2] == "_" or a[3] == "_" or a[4] == "_" or
            a[5] == "_" or a[6] == "_" or a[7] == "_" or a[8] == "_"):
        return True
    else:
        return False


def imp():
    if a.count("X") - a.count("O") >= 2:
        return True
    elif a.count("O") - a.count("X") >= 2:
        return True
    else:
        return False


if x() and o() or imp():
    print("Impossible")
elif x():
    print("X wins")
elif o():
    print("O wins")
elif _():
    print("Game not finished")
else:
    print("Draw")

board = [
    [a[0], a[1], a[2]],
    [a[3], a[4], a[5]],
    [a[6], a[7], a[8]]
]

def board_display():
    print("---------")
    print("|", board[0][0],  board[0][1], board[0][2], "|")
    print("|", board[1][0],  board[1][1], board[1][2], "|")
    print("|", board[2][0],  board[2][1], board[2][2], "|")
    print("---------")

board_display()

board2 = [
  [a[6], a[3], a[0]],
  [a[7], a[4], a[1]],
  [a[8], a[5], a[2]],
]

while True:
    move = input("Enter the coordinates:")
    coords = move.split(" ")
    if coords[0].isalpha() or coords[1].isalpha():
        print("You should enter numbers!")
    elif int(coords[0]) < 1 or int(coords[0]) > 3 or int(coords[1]) < 1 or int(coords[1]) > 3:
        print("Coordinates should be from 1 to 3!")
    elif board2[int(coords[0]) - 1][int(coords[1]) - 1] == "X" or board2[int(coords[0]) - 1][int(coords[1]) - 1] == "O":
        print("This cell is occupied! Choose another one!")
    else:
        if int(coords[0]) == 1 and int(coords[1]) == 1:
            board[2][0] = "X"
        if int(coords[0]) == 1 and int(coords[1]) == 2:
            board[1][0] = "X"
        if int(coords[0]) == 1 and int(coords[1]) == 3:
            board[0][0] = "X"
        if int(coords[0]) == 2 and int(coords[1]) == 1:
            board[2][1] = "X"
        if int(coords[0]) == 2 and int(coords[1]) == 2:
            board[1][1] = "X"
        if int(coords[0]) == 2 and int(coords[1]) == 3:
            board[0][1] = "X"
        if int(coords[0]) == 3 and int(coords[1]) == 1:
            board[2][2] = "X"
        if int(coords[0]) == 3 and int(coords[1]) == 2:
            board[1][2] = "X"
        if int(coords[0]) == 3 and int(coords[1]) == 3:
            board[0][2] = "X"
        break

board_display()