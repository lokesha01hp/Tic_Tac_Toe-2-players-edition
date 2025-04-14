def custom_sum(a,b,c):
    return a + b + c

def printBoard(xstate, zstate):
    zero = 'X' if xstate[0] else ('O' if zstate[0] else 0)  
    one = 'X' if xstate[1] else ('O' if zstate[1] else 1) 
    two = 'X' if xstate[2] else ('O' if zstate[2] else 2) 
    three = 'X' if xstate[3] else ('O' if zstate[3] else 3 ) 
    four = 'X' if xstate[4] else ('O' if zstate[4] else 4) 
    five = 'X' if xstate[5] else ('O' if zstate[5] else 5)  
    six = 'X' if xstate[6] else ('O' if zstate[6]  else 6 ) 
    seven = 'X' if xstate[7] else ('O' if zstate[7] else 7 ) 
    eight = 'X' if xstate[8] else ('O' if zstate[8] else 8 ) 
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")



def check_win(xstate,zstate):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if (custom_sum(xstate[win[0]],xstate[win[1]],xstate[win[2]]) == 3):
            print("X won the match")
            return 1
        if (custom_sum(zstate[win[0]],zstate[win[1]],zstate[win[2]]) == 3):
            print("O won the match")
            return 0
    return -1

if __name__ == "__main__":
    xstate= [0,0,0,0,0,0,0,0,0]
    zstate= [0,0,0,0,0,0,0,0,0]
    turn=input("Want X or O Type what's your pawn :").upper()
    if turn == 'X':
        turn = 1
    else:
        turn = 0

    print("Welcome to Tic Tac Toe")
    while True:
        printBoard(xstate, zstate)
    
        if turn == 1:
            print("X's chance")
            value = int(input("Enter the number: "))
            if xstate[value] == 1 or zstate[value] == 1:
                print("Yo! That spot's already taken. Try again.")
                continue
            xstate[value] = 1
        else:
            print("O's chance")
            value = int(input("Enter the number: "))
            if xstate[value] == 1 or zstate[value] == 1:
                print("Yo! That spot's already taken. Try again.")
                continue
            zstate[value] = 1

        cwins = check_win(xstate, zstate)
        if cwins != -1:
            printBoard(xstate, zstate)
            print("Match over 🎉")
            break

        if all([xstate[i] or zstate[i] for i in range(9)]):
            printBoard(xstate, zstate)
            print("It's a draw")
            break

        turn = 1 - turn
