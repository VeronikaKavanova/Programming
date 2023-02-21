def old_position(self):
    x = str(self.rows) + self.columns
    return x

def new_position(self):
    x = str(self.newrows) + self.newcolumns 
    return x

def turns(self):
    global last_move
    if last_move != self.colour:
        return True
    else:
        print("It's not your turn yet.")


last_move = -1
game = "start"


class pawn:
    def __init__(self, colour, name, columns):
        self.name = name
        self.columns = columns
        self.colour = colour
        if self.colour == 1:
            self.rows = 2
        else:
            self.rows = 7
        self.number_of_moves = 0
        self.first_move = "No"
    
    def first_move(self):
        global last_move
        turn = turns(self)
        if turn == True:
            if self in pieces:
                if self.number_of_moves == 0:
                    self.newrows = self.rows + 2*self.colour
                    self.newcolumns = self.columns
                    x = new_position(self)
                    if spaces[x]:
                        print("Occupied.")
                    elif spaces[x] == "":
                        last_move = self.colour
                        y = old_position(self)
                        spaces[x] = self
                        spaces[y] = ""
                        self.rows = self.newrows
                        self.number_of_moves = 1
                        print(self.rows, self.columns)
                        self.first_move = "Yes"
                else:
                    print("You can't make that move anymore.")
    
    def normal_move(self):
        global last_move
        turn = turns(self)
        if turn == True:
            if self in pieces:
                self.newrows = self.rows + 1*self.colour
                self.newcolumns = self.columns
                x = new_position(self)
                if spaces[x]:
                    print("Occupied.")
                elif spaces[x]== "":
                    last_move = self.colour
                    self.number_of_moves += 1
                    y = old_position(self)
                    spaces[x] = self
                    spaces[y] = ""
                    self.rows = self.newrows
                    print(self.rows, self.columns)
                    self.first_move = "No"
            else:
                print("This piece doesn't exist anymore.")

    def take(self, direction):
        global last_move
        turn = turns(self)
        if turn == True:
            if self in pieces:
                self.newrows = self.rows + 1*self.colour
                self.newcolumns = chr(ord(self.columns) + 1*direction) #direction... -1=left, 1=right
                x = new_position(self)
                if (x in spaces.keys()) and (spaces[x]):
                    last_move = self.colour
                    self.number_of_moves += 1
                    y = old_position(self)
                    enemy = spaces[x]
                    pieces.remove(enemy)
                    spaces[x] = self
                    spaces[y] = ""
                    self.rows = self.newrows
                    self.columns = self.newcolumns
                    print(self.rows, self.columns)
                    self.first_move = "No"
                else:
                    print("There's noone to take.")
            else:
                print("This piece doesn't exist anymore.")

    def en_passant(self):
        global last_move
        turn = turns(self)
        if turn == True:
            if self.name in pieces:
                self.newrows = self.rows
                self.newcolumns = chr(ord(self.columns) + 1*direction)
                x = new_position(self)
                if (x in spaces.keys()) and (spaces[x]):
                    enemy = spaces[x]
                    pass

WP1 = pawn(1, "WP1", "A")
WP2 = pawn(1, "WP2", "B")
WP3 = pawn(1, "WP3", "C")
WP4 = pawn(1, "WP4", "D")
WP5 = pawn(1, "WP5", "E")
WP6 = pawn(1, "WP6", "F")
WP7 = pawn(1, "WP7", "G")
WP8 = pawn(1, "WP8", "H")
BP1 = pawn(-1, "BP1", "A")
BP2 = pawn(-1, "BP2", "B")
BP3 = pawn(-1, "BP3", "C")
BP4 = pawn(-1, "BP3", "D")
BP5 = pawn(-1, "BP5", "E")
BP6 = pawn(-1, "BP6", "F")
BP7 = pawn(-1, "BP7", "G")
BP8 = pawn(-1, "BP8", "H")

spaces = {
    "1A" : "", "1B" : "", "1C" : "", "1D" : "", "1E" : "", "1F" : "", "1G" : "", "1H" : "",
    "2A" : WP1, "2B" : WP2, "2C" : WP3, "2D" : WP4, "2E" : WP5, "2F" : WP6, "2G" : WP7, "2H" : "WP8",
    "3A" : "", "3B" : "", "3C" : "", "3D" : "", "3E" : "", "3F" : "", "3G" : "", "3H" : "",
    "4A" : "", "4B" : "", "4C" : "", "4D" : "", "4E" : "", "4F" : "", "4G" : "", "4H" : "",
    "5A" : "", "5B" : "", "5C" : "", "5D" : "", "5E" : "", "5F" : "", "5G" : "", "5H" : "",
    "6A" : "", "6B" : "", "6C" : "", "6D" : "", "6E" : "", "6F" : "", "6G" : "", "6H" : "",
    "7A" : "BP1", "7B" : "BP2", "7C" : "BP3", "7D" : "BP4", "7E" : "BP5", "7F" : "BP6", "7G" : "BP7", "7H" : "BP8",
    "8A" : "", "8B" : "", "8C" : "", "8D" : "", "8E" : "", "8F" : "", "8G" : "", "8H" : "",
    }

pieces = [WP1, WP2, WP3, WP4, WP5, WP6, WP7, WP8, BP1, BP2, BP3, BP4, BP5, BP6, BP7, BP8]

WP1.first_move()