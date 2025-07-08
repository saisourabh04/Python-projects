import random
import  time

board=[' ']*9

def display_board(board):
    print("GAME BOARD: ")
    i=1
    for item in board:
        print(item,end=' | ')
        if i % 3==0:
            print()
        i+=1
def switch_player(current_player):
    if current_player=='X':
        return 'O'
    else:
        return 'X'
def check_win_over_rows(board,player):
    if board[0]==player and board[1]==player and board[2]==player:
        return True
    elif board[3]==player and board[4]==player and board[5]==player:
        return True
    elif board[6]==player and board[7]==player and board[8]==player:
        return True
    else:
        return False

def check_win_over_cols(board,player):
    if board[0]==player and board[3]==player and board[6]==player:
        return True
    elif board[1]==player and board[4]==player and board[7]==player:
        return True
    elif board[2]==player and board[5]==player and board[8]==player:
        return True
    else:
        return False


def check_win_over_diagonal(board,player):
    if board[0]==player and board[4]==player and board[8]==player:
        return True
    elif board[2]==player and board[4]==player and board[6]==player:
        return True
    else:
        return False

def check_for_win(board,player):
    if check_win_over_rows(board,player) or check_win_over_cols(board,player) or check_win_over_diagonal(board,player):
        return True
    else:
        return False



current_player='X'
while True:
    display_board(board)
    if current_player=='X':
        location=int(input(f"Player {current_player},enter your choice(1-9):"))
    else:
        print("Computers turn")
        time.sleep(2)
        location=random.randint(1,9)
    if board[location-1]==' ':
        board[location-1]=current_player
        if check_for_win(board,current_player):
            print(f"Player {current_player} wins! ")
            display_board(board)
            break
        current_player=switch_player(current_player)
    else:
        print(f"place{location} is taken")

