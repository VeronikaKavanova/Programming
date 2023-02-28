import pygame

#postup jak na git
#git add .
#git commit -m "smyslnuplna zprava"
#git push

#vice vetvi
#git branch nova_vetev
#git switch nazev_vetev
#kdyz poprve nova vetev. git push --set-upstream origin pokus
#git push

turn = 1
can_jump = []

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

    def jump_possible(self):
        direction = 1
        for i in range(2):
            direction = direction*(-1)
            self.newrows = self.rows + 1*self.colour
            self.newcolumns = chr(ord(self.columns) + 1*direction)
            m = new_position(self)
            if m in board.keys():
                k = board[m]
                if k != "" and k.colour != self.colour:
                    self.newrows = self.newrows + 1*self.colour
                    self.newcolumns = chr(ord(self.newcolumns) + 1*direction)
                    n = new_position(self)
                    if n in board.keys(): 
                        if board[n] == "":
                            #print(self, "can jump", direction)
                            can_jump.append([self, direction, m, n])
                        #else:
                            #print("There's not an empty space")
                #lse:
                    #print("There's noone to jump over")
    
    def move(self, direction):
        global turn
        if turn == self.colour:
            if self in board.values():
                if self.colour == 1: array = white
                else: array = black
                can_jump.clear()
                for i in array:
                    i.jump_possible()
                #print(can_jump)
                if can_jump == []:
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
                        print(self, x)
                    else:
                        print("Toto políčko neexistuje nebo je obsazené.")
                else:
                    print("Someone can jump.")
            else:
                print("Tato figurka již neexistuje.")
        else:
            print("Nejsi na tahu.")

    def take(self, direction):
        global turn
        if turn == self.colour:
            if self in board.values():
                can_jump.clear()
                self.jump_possible()
                for i in can_jump:
                    if self in i:
                        if direction == i[1]:
                            if self.colour == 1: array = black
                            else: array = white
                            array.remove(board[i[2]])
                            print([str(obj) for obj in array])
                            board[i[3]] = self
                            board[i[2]] = ""
                            y = old_position(self)
                            board[y] = ""
                            position = list(i[2])
                            self.rows = position[0]
                            self.columns = position[1]
                            print(self, "takes", i[2])
                            self.take(input())
                            turn = turn*(-1)
                            break
                
                        else:
                            print("no") 

    def __str__(self):
        return f"{self.name}"


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

black = [B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11, B12]
white = [W1, W2, W3, W4, W5, W6, W7, W8, W9, W10, W11, W12]


W11.move(-1)
B1.move(1)
W11.take(-1)
B6.take(1)
B6.take(-1)