from random import randint

computer_board = [[' '] * 8 for x in range(8)]
player_board = [[' '] * 8 for x in range(8)]

letter_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
"""Convert letters to numbers"""

def print_board(board):
    """
    Creates the playing board
    """
    print('A B C D E F G H')
    print('===============')
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
    row = input("Please enter a ship row 1-8")
    while row not in '12345678':
        print("Please enter a valid row")
        row = input("Please enter a ship row 1-8")
    column = input("Please enter a ship column A-H").upper()
    while column not in 'ABCDEFGH':
        print("Please enter a valid column")
        column = input("Please enter a ship column A-H")
    return int(row) - 1, letter_to_num(column)

def sum_hit_ships():
    pass

build_ships()
turns = 15
#while turns > 0:
