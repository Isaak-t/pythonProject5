#import Pygames
import random
#Board set up 2D array
Board = [["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_",]]
def Mine_Board ():
    print ("coloms  0    1    2    3    4")
    print ("row 0",Board[0])
    print ("row 1",Board[1])
    print ("row 2",Board[2])
    print ("row 3",Board[3])
    print ("row 4",Board[4])
mine_num = 5
counter =0
while counter < mine_num:
    row = random.randint(0, 4)
    col = random.randint(0, 4)
    if (Board[row][col]=="_") and (counter <= mine_num):
        Board[row][col]="X"
        counter = counter +1

print(Board)
num = 0
def Numbers ():
    while counter == 5 and mine_num == 5 and Board[row][col]=="X":
       num = Board[row+1][col+1]
       num = Board[row-1][col+1]
       num = Board[row-1][col-1]
       num = Board[row+1][col-1]
       num = Board[row+1][col]
       num = Board[row-1][col]
       num = Board[row][col+1]
       num = Board[row][col-1]



Mine_Board()

def Player_move():
    Player_choice_row = input("select a row")
    Player_choice_colom = input("select a colom")
    int_Player_choice_row = int(Player_choice_row)
    int_Player_choice_colom = int(Player_choice_colom)

#def gameplay():
    Player_move()
#gameplay()

