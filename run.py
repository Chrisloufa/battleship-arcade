from random import randint

computer_board = [[' '] * 8 for x in range(8)]
player_board = [[' '] * 8 for x in range(8)]

letter_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
"""Convert letters to numbers"""

def print_board(board):
    """
    Creates the playing board
    """
    print('  A B C D E F G H')
    print('  ===============')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def build_ships(board):
    """ 
    Adds ships to the board for players
    """
    for ship in range(6):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = "X"

def ship_location():
    """
    Add ship location choice
    """
    row = input("Please enter a ship row 1-8: ")
    while row not in '12345678':
        print("Please enter a valid row")
        row = input("Please enter a ship row 1-8: ")
    column = input("Please enter a ship column A-H: ").upper()
    while column not in 'ABCDEFGH':
        print("Please enter a valid column")
        column = input("Please enter a ship column A-H: ").upper()
    return int(row) - 1, letter_to_num(column)

def sum_hit_ships(board):
    count = 0
    for row in board:
        if column == "X":
            count += 1
    return count 

build_ships(computer_board)
turns = 15
while turns > 0:
    print("Welcome to Battleship Arcade")
    print_board(computer_board)
    row, column = ship_location()
    if computer_board[row][column] == "-":
        print("You have already chosen this")
    elif player_board [row][column] == "X":
        print("You have hit sunk a battleship!")
        computer_board[row][column] = "X"
        turns -= 1
    else:
        print("Unlucky, you missed!")
        computer_board[row][column] = "-"
        turns -= 1
    if sum_hit_ships(computer_board) == 6:
        print("Congratulations you have sunk all their battleships!")
        break
    print('You have ' + str(turns) + 'turns remaining')
    if turns == 0:
        print("You are out of turns, game is over")
        break
