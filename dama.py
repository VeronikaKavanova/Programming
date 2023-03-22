import pygame

from pygame.locals import (
    RLEACCEL,
    K_ESCAPE,
    KEYDOWN,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    QUIT,
)

#postup jak na git
#git add .
#git commit -m "smyslnuplna zprava"
#git push

pygame.init()

screen_width = 1200
screen_height = 650

screen = pygame.display.set_mode((screen_width, screen_height))

coordinates = {
    "1A" : (64,491.5), "1C" : (186,491.5), "1E" : (308,491.5), "1G" : (430,491.5),
    "2B" : (124,430), "2D" : (246,430), "2F" : (368,430), "2H" : (490,430),
    "3A" : (64,368.5), "3C" : (186,368.5), "3E" : (308,368.5), "3G" : (430,368.5),
    "4B" : (124,307), "4D" : (246,307), "4F" : (368,307), "4H" : (490,307),
    "5A" : (64,245.5), "5C" : (186,245.5), "5E" : (308,245.5), "5G" : (430,245.5),
    "6B" : (124,184), "6D" : (246,184), "6F" : (368,184), "6H" : (490,184),
    "7A" : (64,122.5), "7C" : (186,122.5), "7E" : (308,122.5), "7G" : (430,122.5),
    "8B" : (124,61), "8D" : (246,61), "8F" : (368,61), "8H" : (490,61),
    }

turn = 1
can_jump = []
can_jump_queens = []
active = ""

game = True

def end_of_game():
    global game
    if turn == 1: 
        array = white
        name = "white"
    else: 
        array = black
        name = "black"
    if array == []:
        game = False
        print(name, "lost, because they don't have any more pieces.")
    else: 
        can_jump.clear()
        can_jump_queens.clear()
        for i in array:
            i.jump_possible()
        if can_jump == [] and can_jump_queens == []:
            for i in array:
                if i.__class__.__name__ == "queen": 
                    x = i.old_position()
                    for diagonal in diagonals:
                        if x in diagonal:
                            for space in diagonal:
                                if space != x:
                                    k = board[space]
                                    if k == "":
                                        return True
                else:                        
                    side = 1
                    for j in range(2):
                        side = side*(-1)
                        i.update(side)
                        x = i.new_position()
                        if (x in board.keys() and board[x] == ""):
                            return True
            game = False
            print(name, "lost, because none of their pieces can move.")

class piece:
    
    def __init__(self, colour, name, rows, columns):
        self.name = name
        self.colour = colour
        self.rows = rows
        self.columns = columns
        if self.colour == 1:
            self.surf = pygame.image.load("WPiece.png").convert_alpha()
        else:
            self.surf = pygame.image.load("BPiece.png").convert_alpha()
        self.surf = pygame.transform.smoothscale(self.surf, (60,60))

    def is_queen(self):
        if self.rows == (4.5+3.5*self.colour):
            self.__class__ = queen
            return True
    
    def old_position(self):
        x = str(self.rows) + self.columns
        return x

    def new_position(self):
        x = str(self.newrows) + self.newcolumns 
        return x

    def update(self,direction):
        self.newrows = self.rows + self.colour 
        self.newcolumns = chr(ord(self.columns) + direction)

    def check(self):
        if self.newrows == self.rows + self.colour:
            if self.newcolumns == chr(ord(self.columns) + 1):
                return True
            elif self.newcolumns == chr(ord(self.columns) - 1):
                return True

    def can_queens_jump(self):
        if self.colour == 1: array = white
        else: array = black
        for i in array:
            if i.__class__.__name__ == "queen":
                i.jump_possible()

    def jump_possible(self):
        side = 1
        for i in range(2):
            side = side*(-1)
            self.update(side)
            enemy_space = self.new_position()
            if enemy_space in board.keys():
                k = board[enemy_space]
                if k != "" and k.colour != self.colour:
                    self.newrows = self.newrows + self.colour
                    self.newcolumns = chr(ord(self.newcolumns) + side)
                    empty_space = self.new_position()
                    if empty_space in board.keys(): 
                        if board[empty_space] == "":
                            #print(self, "can jump", side)
                            can_jump.append([self, enemy_space, empty_space])
                        #else:
                            #print("There's not an empty space")
                #lse:
                    #print("There's noone to jump over")
    
    def move(self, goal_empty_space):
        global turn
        if game == True: 
            if turn == self.colour:
                if self in board.values():
                    if self.colour == 1: array = white
                    else: array = black
                    can_jump.clear()
                    can_jump_queens.clear()
                    for i in array:
                        i.jump_possible()
                    #print(can_jump)
                    if can_jump == [] and can_jump_queens == []:
                        self.newrows = int(goal_empty_space[0])
                        self.newcolumns = goal_empty_space[1]
                        x = self.new_position()
                        if (x in board.keys() and board[x] == ""):
                            if i.check() == True:
                                y = self.old_position()
                                board[x] = self
                                board[y] = ""
                                self.rows = self.newrows
                                self.columns = self.newcolumns
                                self.is_queen
                                print(self, y, "to", x)
                                turn = turn*(-1)
                                active = ""
                                end_of_game()
                            else:
                                print("you can't get to this space")
                        else:
                            print("Toto políčko neexistuje nebo je obsazené.")
                    else:
                        print("Someone can jump.")
                else:
                    print("Tato figurka již neexistuje.")
            else:
                print("Nejsi na tahu.")
        else:
            print("The game is over.")

    def jump(self, goal_empty_space): #zadat, kam chce skončit
        global turn
        if game == True:
            if turn == self.colour:
                if self in board.values():
                    can_jump_queens.clear()
                    self.can_queens_jump()
                    if can_jump_queens == []:
                        can_jump.clear()
                        self.jump_possible()
                        if self.__class__.__name__ == "queen": jumping_possibilities = can_jump_queens
                        else: jumping_possibilities = can_jump 
                        for i in jumping_possibilities:
                            if self in i:
                                if goal_empty_space == i[2]:
                                    if self.colour == 1: array = black
                                    else: array = white
                                    array.remove(board[i[1]])
                                    print([str(obj) for obj in array])
                                    board[i[2]] = self
                                    board[i[1]] = ""
                                    y = self.old_position()
                                    board[y] = ""
                                    position = list(i[2])
                                    self.rows = int(position[0])
                                    self.columns = position[1]
                                    print(self, y, "takes", i[1])
                                    print(self, y, "to", i[2])
                                    turn = turn*(-1)
                                    active = ""
                                    end_of_game()
                                    if self.is_queen() == True:
                                        break
                                    can_jump.clear()
                                    can_jump_queens.clear()
                                    self.jump_possible()
                                    if self.__class__.__name__ == "queen": jumping_possibilities = can_jump_queens
                                    else: jumping_possibilities = can_jump 
                                    for i in jumping_possibilities:
                                        if self in i:
                                            goal_empty_space = input("Write to which space would you like to jump: ")
                                            turn = turn*(-1)
                                            self.jump(goal_empty_space)
                                    break
                                #else:
                                    #print("You can't jump there,")
                            else:
                                print("This piece can't jump.")
                    else:
                        print("A queen can jump") 
                else:
                    print("This piece doesn't exist.")        
            else:
                print("It's not your turn")
        else:
            print("The game is over.")

    def __str__(self):
        return f"{self.name}"

class queen(piece):

    def is_queen(self):
        pass

    def can_queens_jump(self):
        pass

    def check(self):
        y = self.old_position
        for diagonal in diagonals:
            if y in diagonal:
                if x in diagonal:
                    return True

    def update(self, direction):
        number = direction[0]
        horizontal = direction[1]
        vertical = direction[2]
        self.newrows = self.rows + number*vertical     
        self.newcolumns = chr(ord(self.columns) + number*horizontal)
    
    def jump_possible(self):
        x = self.old_position()
        for diagonal in diagonals:
            if x in diagonal:
                for space in diagonal:
                    if space != x:
                        k = board[space] 
                        if k != "" and k.colour != self.colour:
                            enemy_space_index = diagonal.index(space)
                            my_space_index = diagonal.index(x)
                            enemy_space = diagonal[enemy_space_index]
                            if enemy_space_index < my_space_index: 
                                way = -1 
                                number_of_spaces = enemy_space_index
                            else: 
                                way = 1
                                number_of_spaces = len(diagonal) - enemy_space_index - 1
                            empty_space_index = enemy_space_index
                            for i in range(number_of_spaces):
                                empty_space_index = empty_space_index + way
                            #if empty_space_index>-1 and empty_space_index<(len(diagonal)):
                                empty_space = diagonal[empty_space_index]
                                if board[empty_space] == "":
                                    can_jump_queens.append([self, enemy_space, empty_space])
                                else:
                                    break
                                #else:
                                    #print("This space isn't empty.")
                            #else:
                                #print("This space doesn't exist.")

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

diagonals = [["7A", "8B"],["5A", "6B", "7C", "8D"],["3A","4B","5C","6D","7E","8F"],["1A", "2B", "3C", "4D", "5E", "6F", "7G", "8H"], ["1C", "2D", "3E", "4F", "5G", "6H"], ["1E", "2F", "3G", "4H"], ["1G", "2H"], ["3A", "2B", "1C"], ["5A", "4B", "3C", "2D", "1E"], ["7A", "6B", "5C", "4D", "3E", "2F", "1G"], ["8B", "7C", "6D", "5E", "4F", "3G" ,"2H"], ["8D", "7E", "6F", "5G", "4H"], ["8F", "7G", "6H"]]

black = [B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11, B12]
white = [W1, W2, W3, W4, W5, W6, W7, W8, W9, W10, W11, W12]

chessboard = pygame.image.load("chessboard.jpg").convert()

space_8B = pygame.image.load("Policko.jpg").convert()
space_8D = pygame.image.load("Policko.jpg").convert()
space_8F = pygame.image.load("Policko.jpg").convert()
space_8H = pygame.image.load("Policko.jpg").convert()
space_7A = pygame.image.load("Policko.jpg").convert()
space_7C = pygame.image.load("Policko.jpg").convert()
space_7E = pygame.image.load("Policko.jpg").convert()
space_7G = pygame.image.load("Policko.jpg").convert()
space_6B = pygame.image.load("Policko.jpg").convert()
space_6D = pygame.image.load("Policko.jpg").convert()
space_6F = pygame.image.load("Policko.jpg").convert()
space_6H = pygame.image.load("Policko.jpg").convert()
space_5A = pygame.image.load("Policko.jpg").convert()
space_5C = pygame.image.load("Policko.jpg").convert()
space_5E = pygame.image.load("Policko.jpg").convert()
space_5G = pygame.image.load("Policko.jpg").convert()
space_4B = pygame.image.load("Policko.jpg").convert()
space_4D = pygame.image.load("Policko.jpg").convert()
space_4F = pygame.image.load("Policko.jpg").convert()
space_4H = pygame.image.load("Policko.jpg").convert()
space_3A = pygame.image.load("Policko.jpg").convert()
space_3C = pygame.image.load("Policko.jpg").convert()
space_3E = pygame.image.load("Policko.jpg").convert()
space_3G = pygame.image.load("Policko.jpg").convert()
space_2B = pygame.image.load("Policko.jpg").convert()
space_2D = pygame.image.load("Policko.jpg").convert()
space_2F = pygame.image.load("Policko.jpg").convert()
space_2H = pygame.image.load("Policko.jpg").convert()
space_1A = pygame.image.load("Policko.jpg").convert()
space_1C = pygame.image.load("Policko.jpg").convert()
space_1E = pygame.image.load("Policko.jpg").convert()
space_1G = pygame.image.load("Policko.jpg").convert()

spaces = [space_8B, space_8D, space_8F, space_8H, space_7A, space_7C, space_7E, space_7G, 
          space_6B, space_6D, space_6F, space_6H, space_5A, space_5C, space_5E, space_5G, 
          space_4B, space_4D, space_4F, space_4H, space_3A, space_3C, space_3E, space_3G, 
          space_2B, space_2D, space_2F, space_2H, space_1A, space_1C, space_1E, space_1G]

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if active == "":
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pos = (mouse_pos[0] - 294, mouse_pos[1] - 19)
                    if turn == 1: array = white
                    else: array = black
                    for i in array:
                        if i.rect.collidepoint(mouse_pos):
                            active = i
                            print("yes")
            else:
                if event.button == 3:
                    active = ""
                elif event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pos = (mouse_pos[0] - 294, mouse_pos[1] - 19)
                    for space in spaces:
                        if space.rect.collidepoint(mouse_pos):
                            print("yes")

    screen.fill((255,255,255))
    screen.blit(chessboard, ((screen_width-chessboard.get_width())/2,(screen_height-chessboard.get_height())/2))
    for space in spaces:
        y = 61
        for j in range(4):
            x = 124
            for k in range(4):
                chessboard.blit(space, (x,y))
                space.get_rect()
                space.rect.left = x
                space.rect.top = y
                #space.rect = pygame.Rect((x,y), (60,60))
                x += 122
            y += 61.5
            x = 64
            for k in range(4):
                chessboard.blit(space, (x,y))
                space.get_rect()
                space.rect.left = x
                space.rect.top = y
                #space.rect = pygame.Rect((x,y), (60,60))
                x += 122
            y += 61.5

    pieces = white
    for i in range(2):
        for p in pieces:
            chessboard.blit(p.surf, coordinates[p.old_position()])
            p.rect = pygame.Rect(coordinates[p.old_position()], (60,60))
        pieces = black

    pygame.display.flip()

#W12.move("4F")
#B1.move("5A")
#W8.move("3G")
#B5.move("6B")
#W4.move("2H")
#B2.move("5C")
#W11.move("4D")
#B2.jump("3E")
#W8.move("4H")
#B2.move("3E")
#W10.move("4B")
#B2.jump("5G")
#W3.move("2F")
#B1.jump("3C")
#W9.move("4B")
#B1.jump("5A")
#W2.move("2D")
#B1.jump("1E")
#W4.jump("4F")
#B2.jump("3E") 
#W5.move(1)
#B4.move(-1)
#W1.move(1)
#B2.move([1,1,1])
#W5.move(1)
#B2.move([1,-1,1])
#W1.move(1)
#B2.jump("2B")