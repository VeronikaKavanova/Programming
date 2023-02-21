import pygame

turn = 1 

def old_position(self):
    x = str(self.rows) + self.columns
    return x

def new_position(self):
    x = str(self.newrows) + self.newcolumns 
    return x

class piece:
    
    def __init__(self, colour, name, rows, columns):
        self.name = name
        self.colour = colour
        self.rows = rows
        self.columns = columns

    def jump_possible(self, direction):
        self.newrows = self.rows + 1*self.colour
        self.newcolumns = chr(ord(self.columns) + 1*direction)
        x = new_position(self)
        k = board[x]
        if k != "" and k.colour != self.colour:
            print("yes")
        else:
            print("no")
    
    def move(self, direction):
        global turn
        if turn == self.colour:
            if self in board.values():
                self.newrows = self.rows + 1*self.colour
                self.newcolumns = chr(ord(self.columns) + 1*direction) #direction... -1=left, 1=right
                x = new_position(self)
                if (x in board.keys() and board[x] == ""):
                    y = old_position(self)
                    board[x] = self
                    board[y] = ""
                    self.rows = self.newrows
                    self.columns = self.newcolumns
                    turn = turn*(-1)
                    print(self.name, x)
                else:
                    print("Toto políčko neexistuje nebo je obsazené.")
            else:
                print("Tato figurka již neexistuje.")
        else:
            print("Nejsi na tahu.")
    def take(self, direction):
        pass

W1 = piece(1,"W1",1,"A")
W2 = piece(1,"W2",1,"C")
W3 = piece(1,"W3",1,"E")
W4 = piece(1,"W4",1,"G")
W5 = piece(1,"W5",2,"B")
W6 = piece(1,"W6",2,"D")
W7 = piece(1,"W7",2,"F")
W8 = piece(1,"W8",2,"H")
W9 = piece(1,"W9",3,"A")
W10 = piece(1,"W10",3,"C")
W11 = piece(1,"W11",3,"E")
W12 = piece(1,"W12",3,"G")

B1 = piece(-1,"B1",6,"B")
B2 = piece(-1,"B2",6,"D")
B3 = piece(-1,"B3",6,"F")
B4 = piece(-1,"B4",6,"H")
B5 = piece(-1,"B5",7,"A")
B6 = piece(-1,"B6",7,"C")
B7 = piece(-1,"B7",7,"E")
B8 = piece(-1,"B8",7,"G")
B9 = piece(-1,"B9",8,"B")
B10 = piece(-1,"B10",8,"D")
B11 = piece(-1,"B11",8,"F")
B12 = piece(-1,"B12",8,"H")

board = {
    "1A" : W1, "1C" : W2, "1E" : W3, "1G" : W4,
    "2B" : W5, "2D" : W6, "2F" : W7, "2H" : W8,
    "3A" : W9, "3C" : W10, "3E" : W11, "3G" : W12,
    "4B" : "", "4D" : "", "4F" : "", "4H" : "",
    "5A" : "", "5C" : "", "5E" : "", "5G" : "",
    "6B" : B1, "6D" : B2, "6F" : B3, "6H" : B4,
    "7A" : B5, "7C" : B6, "7E" : B7, "7G" : B8,
    "8B" : B9, "8D" : B10, "8F" : B11, "8H" : B12,
    }

W9.move(1)
B1.move(1)
W9.jump_possible(-1)
