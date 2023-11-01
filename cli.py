from logic import check_winner

def get_empty_board():
 #   """
 #   row_1 = ['0','0','0']
 #   row_2 = ['0','0','0']
 #   row_3 = ['0','0','0']

 #   board = [row_1, row_2, row_3]
 #   """
 
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def print_board(board):
    for row in board:
        print(row) #print will print the varible in the new line

def get_player_input(current_player):
#    """
#    return:
#        row: int -> the index of row
#        col: int -> the index of colum
#    """
    prompt = f"player {current_player} > "
    player_input = input(prompt) # this is a string
    row_col_list = player_input.split(',')  # "1,1".split(',')->["1","1"]
    row, col = [int(x) for x in row_col_list]  #["1","1"]
    return row, col

def switch_player(current_player):
    if current_player == 'X':
        return '0'
    return 'X'


if __name__ == '__main__':# if the prorgam is excute directly, run the following
    current_player = 'X'
    board = get_empty_board()# get a empty board
    winner = None
    # row, col = get_player_input()# ask user input
    # print(row)
    # print(col)


    # check for winner
    while winner is None:
        print_board(board)  #print the board
        try:
            row, col = get_player_input(current_player) #ask user input
        except ValueError:
            print("Invalid input, try again\n")
            continue

        board[row][col] = current_player # mark the board of the current player
        winner = check_winner(board) #"0","X" break out of the loop
        current_player = switch_player(current_player)

        print_board(board)
        print(f"Winner is{current_player}")
    # check if game is draw
    # print the winner