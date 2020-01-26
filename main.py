board = ['-','-','-',
         '-','-','-',
         '-','-','-']


def display_board():
    print(board[0] + " | " +board[1] +" | "+board[2])
    print(board[3] + " | " +board[4] +" | "+board[5])
    print(board[6] + " | " +board[7] +" | "+board[8])

display_board()

def flip_player(first):
    if first == "X":
        first = "O"
        return (first)
    else:
        return('X')

def check_result(board,first):
    if (board[0]==board[1]==board[2]!="-") or (board[3]==board[4]==board[5]!="-") or (board[6]==board[7]==board[8]!="-")or(board[0]==board[3]==board[6]!="-") or (board[1]==board[4]==board[7]!="-") or (board[2]==board[5]==board[8]!="-")or(board[0]==board[4]==board[8]!="-") or (board[2]==board[4]==board[6]!="-"):
        return (first)
    else:
        return (0)

def user_input():
    first ="X"
    while "-" in board:
        print(first + "'s turn")
        player = input("Where do you want to your move (1-9)?")
        valid= False
        while not valid:
            while player not in ["1","2","3","4","5","6","7","8","9"]:
                player =input("Choose the number from 1 to 9 ")
            player = int(player)-1
            if board[player]=="-":
                valid= True
            else:
                print("choose again")
        board[player]= first
        display_board()
        result = check_result(board,first)
        if result == "X":
            print('X is the winner')
            break
        elif result =="O":
            print("O if the winner")
        first = str(flip_player(first))
        if "-" not in board:
            print("No result")
        
    

user_input()
