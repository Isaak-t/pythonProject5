

import random
#Board set up 2D array
Board = [["_","_","_"],["_","_","_"],["_","_","_"]]
win_X = [["X","X","X"],["X","X","X"],["X","X","X"]]
win_O = [["O","O","O"],["O","O","O"],["O","O","O"]]
def TIK_TAK_TOH_BOARD ():
    print ("coloms  0    1    2")
    print ("row 0",Board[0])
    print ("row 1",Board[1])
    print ("row 2",Board[2])
print ("welcome to the game")

#ERROR HANDLING

Player_choice = input("X or O?")
print ("Great choice you are", Player_choice)
def Player_choosing ():
    global Player_choice
    global Computer_choice
    if (Player_choice != "X") and (Player_choice != "O"):
        print ("type X or O")
        #Player_choosing()
    if Player_choice == "X":
        Computer_choice = "O"
    if Player_choice == "O":
        Computer_choice = "X"
        print ("the computer chose", Computer_choice)

Player_choosing()

def Compuer_move ():
    Random_choice_row = random.randint(0,2)
    Random_choice_colom = random.randint(0,2)
    if Board[Random_choice_row][Random_choice_colom] == "_":
        Board[Random_choice_row][Random_choice_colom] = (Computer_choice)
    else:
        Compuer_move()
    TIK_TAK_TOH_BOARD ()
def Player_move():
    Player_choice_row = input("select a row")
    Player_choice_colom = input("select a colom")
    int_Player_choice_row = int(Player_choice_row)
    int_Player_choice_colom = int(Player_choice_colom)

    if Board[int_Player_choice_row][int_Player_choice_colom] == "_":
        Board[int_Player_choice_row][int_Player_choice_colom] = Player_choice
    else:
        print ("pick again")
        Player_move()

def gameplay():
   while True:
    Compuer_move()
    if win_X [0] == Board[0]:
        print ("X wins")
        break
    if win_X [1] == Board[1]:
        print ("X wins")
        break
    if win_X [2] == Board[2]:
        print ("X wins")
        break
    if (((Board[0][0] == "X") and (Board[1][0] == "X" )and (Board[2][0])) == "X"):
        print ("X wins")
        break
    if (((Board[0][1] == "X") and (Board[1][1] == "X" )and (Board[2][1])) == "X"):
        print ("X wins")
        break
    if (((Board[0][2] == "X") and (Board[1][2] == "X" )and (Board[2][2])) == "X"):
        print ("X wins")
        break
    if win_O[0] == Board[0]:
        print("O wins")
        break
    if win_O[1] == Board[1]:
        print("O wins")
        break
    if win_O[2] == Board[2]:
        print("O wins")
        break
    if (((Board[0][0] == "O") and (Board[1][0] == "O") and (Board[2][0])) == "O"):
        print("O wins")
        break
    if (((Board[0][1] == "O") and (Board[1][1] == "O") and (Board[2][1])) == "O"):
        print("O wins")
        break
    if (((Board[0][2] == "O") and (Board[1][2] == "O") and (Board[2][2])) == "O"):
        print("O wins")
        break
    if (((Board[0][0] == "O") and (Board[1][1] == "O") and (Board[2][2])) == "O"):
        print ("O wins")
        break
    if (((Board[2][0] == "O") and (Board[1][1] == "O") and (Board[0][2])) == "O"):
        print ("O wins")
    if (((Board[0][0] == "X") and (Board[1][1] == "X") and (Board[2][2])) == "X"):
        print ("X wins")
        break
    if (((Board[2][0] == "X") and (Board[1][1] == "X") and (Board[0][2])) == "X"):
        print ("X wins")
        break
    Player_move()
    if win_X [0] == Board[0]:
        print ("X wins")
        break
    if win_X [1] == Board[1]:
        print ("X wins")
        break
    if win_X [2] == Board[2]:
        print ("X wins")
        break
    if (((Board[0][0] == "X") and (Board[1][0] == "X" )and (Board[2][0])) == "X"):
        print ("X wins")
        break
    if (((Board[0][1] == "X") and (Board[1][1] == "X" )and (Board[2][1])) == "X"):
        print ("X wins")
        break
    if (((Board[0][2] == "X") and (Board[1][2] == "X" )and (Board[2][2])) == "X"):
        print ("X wins")
        break
    if win_O[0] == Board[0]:
        print("O wins")
        break
    if win_O[1] == Board[1]:
        print("O wins")
        break
    if win_O[2] == Board[2]:
        print("O wins")
        break
    if (((Board[0][0] == "O") and (Board[1][0] == "O") and (Board[2][0])) == "O"):
        print("O wins")
        break
    if (((Board[0][1] == "O") and (Board[1][1] == "O") and (Board[2][1])) == "O"):
        print("O wins")
        break
    if (((Board[0][2] == "O") and (Board[1][2] == "O") and (Board[2][2])) == "O"):
        print("O wins")
        break
    if (((Board[0][0] == "O") and (Board[1][1] == "O") and (Board[2][2])) == "O"):
        print ("O wins")
        break
    if (((Board[2][0] == "O") and (Board[1][1] == "O") and (Board[0][2])) == "O"):
        print ("O wins")
    if (((Board[0][0] == "X") and (Board[1][1] == "X") and (Board[2][2])) == "X"):
        print ("X wins")
        break
    if (((Board[2][0] == "X") and (Board[1][1] == "X") and (Board[0][2])) == "X"):
        print ("X wins")
        break
    Compuer_move()
    Player_move()
gameplay()

