import json

CELL_EMPTY = " "
CELL_PLAYER_1 = "O"
CELL_PLAYER_2 = "X"


def initialize_game_state():
    return {'turn': 0, 'board': initialize_board()}


def initialize_board():
    """
    Creates a new empty board
    :return: A board
    """
    return [[CELL_EMPTY for _ in range(3)] for _ in range(3)]


def display_board(board):
    """
    Displays a board
    :param board: Board to be displayed
    """
    print("\t" + "\t".join([str(i + 1) for i, cell in enumerate(board[0])]))
    for i, row in enumerate(board):
        print(i + 1, end='\t')
        for j, cell in enumerate(row):
            print(cell, end='\t')
        print()


def set_chip_to_board(board, row, column, chip):
    """
    Sets a chip to a cell in a board
    :param board: Board to be modified
    :param row: Row in which we will set the chip
    :param column: Column in which we will set the chip
    :param chip: Chip to be set in the board
    :return: Modified board
    """
    board[row][column] = chip
    return board


def check_empty_cell(board, row, column):
    """
    Checks if a determined cell is empty
    :param board: Board
    :param row: Row
    :param column:  Column
    :return: Whether the determined cell is empty or not
    """
    return board[row][column] == CELL_EMPTY


def check_cell_in_board(board, row, column):
    """

    :param board:
    :param row:
    :param column:
    :return:
    """
    return 0 <= row < len(board) and 0 <= column < len(board[0])


def safe_set_chip(board, row, column, chip):
    """
    Checks if the chip can be set and sets it if its alright
    :param board: Board to be modified
    :param row: Row
    :param column: Column
    :param chip: Chip to be set to the board
    :return: Whether the chip has been set or not
    """
    # ~~~~DANGER ZONE~~~~~~
    if not check_cell_in_board(board, row, column):
        print("Illo you cannot go outside the board!")
        return False
    elif not check_empty_cell(board, row, column):
        print("Illo you have to have a lil bit of respect for other chips in the board!")
        return False
    # ~~~~END OF DANGER~~~~~

    set_chip_to_board(board, row, column, chip)
    return True


"""
game_state = initialize_game_state()

with open('game.holis', 'w') as output_file:
    json.dump(game_state, output_file, indent=4, sort_keys=True)
"""

with open('game.holis', 'r') as input_file:
    game_state = json.load(input_file)

def int_input(text=""):
    while 1:
        try:
            return int(input(text))
        except:
            pass

int_input("> ")
display_board(game_state['board'])