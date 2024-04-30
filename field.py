import sys
import numpy as np

class board():     
    def __init__(self):
        self.player = None
        self.choice = None
        self.board = ["-","-","-",
                      "-","-","-",
                      "-","-","-"]
        
    def move(self):   
        #defining a mark to each player
        if self.player == "Player 1":
                self.mark = "X"
        elif self.player == "Player 2":
                self.mark = "O"    
        #automates the move of the player that hasn't been chosen by the user        
        if self.player != self.choice:
            #automatic player
            while True:
                auto_position = np.random.randint(0,8)
                if self.board[auto_position] == "-":
                    self.board[auto_position] = self.mark
                    break
                else:
                    pass
        else:
            #human
            #the loop is going to get exexuted untill all criteria is satesfied
            while True:
                position = int(input(f"{self.player} on position 1-9: "))
                if position > 9 or position < 1:
                    print("Please chose number between 1 and 9")
                else:
                    if self.board[position - 1] == "-":
                        self.board[position - 1] = self.mark
                        break
                    else:
                        print("Position ocupied")          
    #printing board
    def print_board(self):
        if self.player == self.choice:
            print("\n")
            print(self.board[0] + " | " + self.board[1] + " | " + self.board[2] + "      " + "1|2|3")
            print(self.board[3] + " | " + self.board[4] + " | " + self.board[5] + "      " + "4|5|6")
            print(self.board[6] + " | " + self.board[7] + " | " + self.board[8] + "      " + "7|8|9")
        
    #selecting what player we want to play with
    def chose_player(self):
        if self.player == None:
            self.choice = input("Select Player 1 = X, or Player 2 = O: ")
            self.player = self.choice
            
    #switching players after each turn       
    def switch_players(self):
        if self.player == "Player 1":
            self.player = "Player 2"
        else:
            self.player = "Player 1"
    pass
 
board = board()   
while True:
    board.chose_player()
    board.print_board()
    board.move()
    board.switch_players()
    
