import random
import os
    
def display_board(board):
    os.system('cls')
    print('For Your Reference')
    print("-------------")
    print("| 1 | 2 | 3 |")
    print("-------------")
    print("| 4 | 5 | 6 |")
    print("-------------")
    print("| 7 | 8 | 9 |")
    print("-------------")
    print()
    print(' -------------')
    print(' | '+board[1]+' | '+board[2]+' | '+board[3]+ ' |')
    print(' -------------')
    print(' | '+board[4]+' | '+board[5]+' | '+board[6]+' |')
    print(' -------------')
    print(' | '+board[7]+' | '+board[8]+' | '+board[9]+' |')
    print(' -------------')
         
def player_input():
    markers=' '
    print("player 1 : choose  X or 0")
    markers=input("player 1= ")
    if markers=='X':
        return('X','0')
    else:
        return('0','X')
def play_first():
    flip=random.randint(0,1)
    if flip==0:
        return('player1')
    else:
        return('player2')
def player_choice(board):
    position=int(input("enter the number where you want to place your marker= "))
    if board[position]==' ':            
        return position
    else:
        while (board[position]!=' '):
            print("you have entered the marker where marker is already placed ...please enter new position")
            position=int(input("enter the number where you want to place your marker= "))
        return position             
def place_marker(board,marker,position):

        board[position]=marker
def win_check(board,marker):
    if((board[1]==board[2]==board[3]==marker)or(board[4]==board[5]==board[6]==marker)or(board[7]==board[8]==board[9]==marker)or(board[1]==board[4]==board[7]==marker)or(board[2]==board[5]==board[8]==marker)or(board[3]==board[6]==board[9]==marker)or(board[3]==board[5]==board[7]==marker)or(board[1]==board[5]==board[9]==marker)):
        return(True)
    else:
        return(False)    
        
def replay():
    x=input(" PLAY AGAIN? yes or no:")
    if(x=='yes'):
        return(True)
    else:
        return(False)        

def play_game():
    print('Tic Tac Toe')
    board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']               
    display_board(board)
    player1,player2=player_input()
    print('player 2='+player2)
    turn=play_first()
    print("first chance:"+turn)
    play_game=input("ready to play? yes or no:")
    if(play_game=='yes'):
        game_on=True
    else:
        game_on=False
    while game_on :       
        if(turn=='player1'):
            display_board(board)
            position=player_choice(board)
            place_marker(board,player1,position)
            if(win_check(board,player1)):
                display_board(board)
                print("player1 won")
                game_on=False
            else:
                c=0
            
                for i in range(1,10):
                    if board[i]==' ':
                        c=c+1
                if(c==0):
                    print("game tie")
                    game_on=False
                else:
                    turn='player2'
            
                
        if(turn=='player2'):
            display_board(board)
            position=player_choice(board)
            place_marker(board,player2,position)
            if(win_check(board,player2)):
                display_board(board)
                print("player2 won")
                game_on=False
            else:
                c=0
                for i in range(1,10):
                    if board[i]==' ':
                        c=c+1
                if(c==0):
                    print("game tie")
                    game_on=False
                else:
                    turn='player1'                  
play_game()
while (replay()):
     play_game()
        