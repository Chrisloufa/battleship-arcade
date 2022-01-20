
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


def build_ships():
    pass

def ship_location():
    pass

def sum_hit_ships():
    pass

build_ships()
turns = 15
#while turns > 0:
