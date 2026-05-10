def print_board(board):
    print('\n')
    print(board[0] + "|" + board[1] + "|" + board[2])
    print('--+---+--')
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("--+---+--")
    print(board[6] + "|" + board[7] + "|"  + board[8])
    print("\n")

# Rows
def check_winner(board, player) :
    if(board[0] == board[1] == board[2]==player or
       board[3] == board[4] == board[5] == player or
       board [6] == board[7] == board[8] == player) :
        return True

# Columns
    if(board[0] == board[3] == board[6] == player or
   board[1] == board[4] == board[7] == player or
   board[2] == board[5] == board[8] == player):
        return True

# Diagonals
    if(board[0] == board[4] == board[8] == player or
    board[2] == board[4] == board[6] == player):
        return True

   
    

def is_draw(board):
    return '' not in board

def play_game():
    board = [''] * 9
    current_player = 'X'

    print('Welcome to Tic Tac Toe!')
    print('Positions are numbered from 1 to 9 as follows:\n')
    print('1 | 2 | 3')
    print("--+---+--")
    print("4 | 5 | 6")
    print('--+---+--')
    print('7 | 8 | 9')

    while True:
        print_board(board)

        try:
            move = int(input(f"Player {current_player}, enter your move(1-9):")) - 1
            if move < 0 or move > 8 :
                print('Invalid position! Try again.')
                continue

            if board[move] != "":
                print('Position already taken! Try again.')
                continue

            board[move] = current_player
            
            if check_winner(board, current_player):
                print_board(board)
                print(f'🎉Player {current_player} wins!')
                break

            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            #Switch player
            current_player = "O" if current_player == "X" else "X"


        except ValueError:
            print("Please enter a valid number!")

play_game()