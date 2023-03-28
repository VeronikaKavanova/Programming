import pygame
import os

from pygame.locals import (
    RLEACCEL,
    K_ESCAPE,
    KEYDOWN,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    QUIT,
)

pygame.init()

screen_width = 1200
screen_height = 650


screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

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
draw_counter = 0
same_position_white = []
same_position_black = []

win_w_pieces = pygame.image.load("win_w_pieces.png")
win_w_moves = pygame.image.load("win_w_moves.png")
win_b_pieces = pygame.image.load("win_b_pieces.png")
win_b_moves = pygame.image.load("win_b_moves.png")
draw_moves = pygame.image.load("draw_moves.png")
draw_repetition = pygame.image.load("draw_repetition.png")

def notification(which_one):
    notification = True
    while notification == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    notification = False
        screen.blit(which_one, which_one.get_rect(center = screen.get_rect().center))
        pygame.display.flip()

def end_of_game():
    global game
    if turn == 1: 
        array = white
        same_position_white.append(dict(board))
        same_position = same_position_white
    else: 
        array = black
        same_position_black.append(dict(board))
        same_position = same_position_black
    for i in same_position:
        count = same_position.count(i)
        if count > 2:
            game = False
            notification(draw_repetition)
    if draw_counter == 15:
        game = False
        notification(draw_moves)
    elif array == []:
        game = False
        if turn == 1:
            notification(win_b_pieces)
        else:
            notification(win_w_pieces)
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
            if turn == 1:
                notification(win_b_moves)
            else:
                notification(win_w_moves)

class space:

    def __init__(self, which_one):
        self.surf = pygame.image.load("Policko.jpg").convert()
        self.which_one = which_one
        self.position = coordinates[which_one]
        self.rect = pygame.Rect(self.position, (60,60))

class button:

    def __init__(self, which_one,x,y,width,height):
        self.surf = pygame.image.load(which_one).convert()
        self.position = ((x,y))
        self.rect = pygame.Rect(self.position,(width,height))
        
class piece:
    
    def __init__(self, colour, name, rows, columns):
        self.name = name
        self.colour = colour
        self.rows = rows
        self.columns = columns
        self.is_not_active()

    def is_queen(self):
        if self.rows == (4.5+3.5*self.colour):
            self.__class__ = queen
            self.is_not_active()
            return True
    
    def is_active(self):
        if self.colour == 1:
            self.surf = pygame.image.load("WPiece_active.png").convert_alpha()
        else:
            self.surf = pygame.image.load("BPiece_active.png").convert_alpha()
        self.surf = pygame.transform.smoothscale(self.surf, (60,60))

    def is_not_active(self):
        if self.colour == 1:
            self.surf = pygame.image.load("WPiece.png").convert_alpha()
        else:
            self.surf = pygame.image.load("BPiece.png").convert_alpha()
        self.surf = pygame.transform.smoothscale(self.surf, (60,60))

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
                            can_jump.append([self, enemy_space, empty_space])
    
    def move(self, goal_empty_space):
        global game, turn, draw_counter
        if game == True: 
            if turn == self.colour:
                if self in board.values():
                    if self.colour == 1: array = white
                    else: array = black
                    can_jump.clear()
                    can_jump_queens.clear()
                    for i in array:
                        i.jump_possible()
                    if can_jump == [] and can_jump_queens == []:
                        self.newrows = int(goal_empty_space[0])
                        self.newcolumns = goal_empty_space[1]
                        x = self.new_position()
                        if (x in board.keys() and board[x] == ""):
                            if self.check() == True:
                                y = self.old_position()
                                board[x] = self
                                board[y] = ""
                                self.rows = self.newrows
                                self.columns = self.newcolumns
                                if self.__class__.__name__ == "queen":
                                    draw_counter += 1
                                else:
                                    draw_counter = 0
                                self.is_queen()
                                print(self, y, "to", x)
                                turn = turn*(-1)
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

    def jump(self, goal_empty_space):
        global game, game_running, turn, draw_counter
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
                                    draw_counter = 0
                                    turn = turn*(-1)
                                    end_of_game()
                                    if self.is_queen() == True:
                                        break
                                    can_jump.clear()
                                    can_jump_queens.clear()
                                    self.jump_possible()
                                    if self.__class__.__name__ == "queen": jumping_possibilities = can_jump_queens
                                    else: jumping_possibilities = can_jump 
                                    if jumping_possibilities != []:

                                        turn = turn*(-1) 
                                        have_to_jump = True
                                        
                                        while have_to_jump:
                                            
                                            screen.fill((134,111,188))
                                            screen.blit(chessboard, chessboard.get_rect(center = screen.get_rect().center))
                                            for place in spaces:
                                                chessboard.blit(place.surf, (place.position))

                                            pieces = white
                                            for i in range(2):
                                                for p in pieces:
                                                    chessboard.blit(p.surf, coordinates[p.old_position()])
                                                    p.rect = pygame.Rect(coordinates[p.old_position()], (60,60))
                                                pieces = black

                                            pygame.display.flip()

                                            for event in pygame.event.get():
                                                if event.type == pygame.KEYDOWN:
                                                    if event.key == K_ESCAPE:
                                                        end = True
                                                        while end:
                                                            for event in pygame.event.get():
                                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                                    if event.button == 1:
                                                                        mouse_pos = pygame.mouse.get_pos()
                                                                        mouse_pos = (mouse_pos[0] - (screen.get_rect().center[0]-300), mouse_pos[1] - (screen.get_rect().center[1]-150))
                                                                        if yes_button.rect.collidepoint(mouse_pos):
                                                                            have_to_jump = False
                                                                            end = False
                                                                            game = False
                                                                            game_running = False
                                                                        elif no_button.rect.collidepoint(mouse_pos):
                                                                            end = False
                                                            screen.blit(warning, warning.get_rect(center = screen.get_rect().center))
                                                            warning.blit(yes_button.surf,yes_button.position)
                                                            warning.blit(no_button.surf,no_button.position)
                                                            pygame.display.flip()
                                                elif event.type == pygame.MOUSEBUTTONDOWN:                                        
                                                    if event.button == 1:
                                                        mouse_pos = pygame.mouse.get_pos()
                                                        mouse_pos = (mouse_pos[0] - ((screen.get_width()-chessboard.get_width())/2), mouse_pos[1] - ((screen.get_height()-chessboard.get_height())/2))
                                                        for place in spaces:
                                                            if place.rect.collidepoint(mouse_pos):  
                                                                self.jump(place.which_one)
                                                                if turn != self.colour:
                                                                    have_to_jump = False
                                    break
                                else:
                                    print("You can't jump there")
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

    def is_active(self):
        if self.colour == 1:
            self.surf = pygame.image.load("WQueen_active.png").convert_alpha()
        else:
            self.surf = pygame.image.load("BQueen_active.png").convert_alpha()
        self.surf = pygame.transform.smoothscale(self.surf, (60,60))

    def is_not_active(self):
        if self.colour == 1:
            self.surf = pygame.image.load("WQueen.png").convert_alpha()
        else:
            self.surf = pygame.image.load("BQueen.png").convert_alpha()
        self.surf = pygame.transform.smoothscale(self.surf, (60,60))

    def check(self):
        y = self.old_position()
        for diagonal in diagonals:
            if y in diagonal:
                x = self.new_position()
                if x in diagonal:
                    return True
    
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
                                empty_space = diagonal[empty_space_index]
                                if board[empty_space] == "":
                                    can_jump_queens.append([self, enemy_space, empty_space])
                                else:
                                    break

diagonals = [["7A", "8B"],["5A", "6B", "7C", "8D"],["3A","4B","5C","6D","7E","8F"],
             ["1A", "2B", "3C", "4D", "5E", "6F", "7G", "8H"], ["1C", "2D", "3E", "4F", "5G", "6H"], 
             ["1E", "2F", "3G", "4H"], ["1G", "2H"], ["3A", "2B", "1C"], ["5A", "4B", "3C", "2D", "1E"], 
             ["7A", "6B", "5C", "4D", "3E", "2F", "1G"], ["8B", "7C", "6D", "5E", "4F", "3G" ,"2H"], 
             ["8D", "7E", "6F", "5G", "4H"], ["8F", "7G", "6H"]]

chessboard = pygame.image.load("chessboard.jpg").convert()

space_8B = space("8B")
space_8D = space("8D")
space_8F = space("8F")
space_8H = space("8H")
space_7A = space("7A")
space_7C = space("7C")
space_7E = space("7E")
space_7G = space("7G")
space_6B = space("6B")
space_6D = space("6D")
space_6F = space("6F")
space_6H = space("6H")
space_5A = space("5A")
space_5C = space("5C")
space_5E = space("5E")
space_5G = space("5G")
space_4B = space("4B")
space_4D = space("4D")
space_4F = space("4F")
space_4H = space("4H")
space_3A = space("3A")
space_3C = space("3C")
space_3E = space("3E")
space_3G = space("3G")
space_2B = space("2B")
space_2D = space("2D")
space_2F = space("2F")
space_2H = space("2H")
space_1A = space("1A")
space_1C = space("1C")
space_1E = space("1E")
space_1G = space("1G")

spaces = [space_8B, space_8D, space_8F, space_8H, space_7A, space_7C, space_7E, space_7G, 
          space_6B, space_6D, space_6F, space_6H, space_5A, space_5C, space_5E, space_5G, 
          space_4B, space_4D, space_4F, space_4H, space_3A, space_3C, space_3E, space_3G, 
          space_2B, space_2D, space_2F, space_2H, space_1A, space_1C, space_1E, space_1G]

running = True
game_running = False
game = False

gap = (3/16)*screen.get_height()-60
quit_button = button("QUIT.png",(screen.get_width()-300)/2,screen.get_height() - gap - 80,300,80)
tutorial_button = button("TUTORIAL.png",(screen.get_width()-300)/2,screen.get_height()-2*gap - 160,300,80)
play_button = button("PLAY.png",(screen.get_width()-300)/2,screen.get_height()-3*gap - 240,300,80)
yes_button = button("ANO.png",85,159,155,86)
no_button = button("NE.png",381,159,155,86)
left_arrow = button("left_arrow.png",20,20,120,60)
right_arrow = button("right_arrow.png",1060,20,120,60)

title = pygame.image.load("Title.png")
warning = pygame.image.load("warning.png")
tutorial_page_1 = pygame.image.load("tutorial_page_1.png")
tutorial_page_2 = pygame.image.load("tutorial_page_2.png")
tutorial_page_3 = pygame.image.load("tutorial_page_3.png")
tutorial_page_4 = pygame.image.load("tutorial_page_4.png")
tutorial_page_5 = pygame.image.load("tutorial_page_5.png")
tutorial_page_6 = pygame.image.load("tutorial_page_6.png")
tutorial_pages = [tutorial_page_1, tutorial_page_2, tutorial_page_3, tutorial_page_4, tutorial_page_5, tutorial_page_6]

while running:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if quit_button.rect.collidepoint(mouse_pos):
                    running = False
                elif tutorial_button.rect.collidepoint(mouse_pos):
                    tutorial = True
                    tutorial_number = 0
                    tutorial_page = tutorial_pages[tutorial_number]

                    while tutorial == True:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == K_ESCAPE:
                                    tutorial = False
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    mouse_pos = pygame.mouse.get_pos()
                                    mouse_pos = (mouse_pos[0] - (screen.get_rect().center[0]-600), mouse_pos[1] - (screen.get_rect().center[1]-325))
                                    if left_arrow.rect.collidepoint(mouse_pos):
                                        tutorial_number = (tutorial_number - 1)%6
                                    elif right_arrow.rect.collidepoint(mouse_pos):
                                        tutorial_number = (tutorial_number + 1)%6
                        
                        tutorial_page = tutorial_pages[tutorial_number]
                        screen.blit(tutorial_page, tutorial_page.get_rect(center = screen.get_rect().center))
                        tutorial_page.blit(left_arrow.surf,(left_arrow.position))
                        tutorial_page.blit(right_arrow.surf,(right_arrow.position))
                        pygame.display.flip()

                elif play_button.rect.collidepoint(mouse_pos):
                    game = True
                    game_running = True

                    turn = 1
                    can_jump = []
                    can_jump_queens = []
                    active = ""
                    draw_counter = 0
                    same_position_white = []
                    same_position_black = []

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

    screen.fill((134,111,188))
    screen.blit(quit_button.surf,(quit_button.position))
    screen.blit(tutorial_button.surf,(tutorial_button.position))
    screen.blit(play_button.surf,(play_button.position))
    screen.blit(title, ((screen.get_width()-title.get_width())/2,gap/2))
    pygame.display.flip()

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    end = True
                    while end:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    mouse_pos = pygame.mouse.get_pos()
                                    mouse_pos = (mouse_pos[0] - (screen.get_rect().center[0]-300), mouse_pos[1] - (screen.get_rect().center[1]-150))
                                    if yes_button.rect.collidepoint(mouse_pos):
                                        end = False
                                        game = False
                                        game_running = False
                                    elif no_button.rect.collidepoint(mouse_pos):
                                        end = False
                        screen.blit(warning, warning.get_rect(center = screen.get_rect().center))
                        warning.blit(yes_button.surf,yes_button.position)
                        warning.blit(no_button.surf,no_button.position)
                        pygame.display.flip()
                            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if active == "":
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        mouse_pos = (mouse_pos[0] - ((screen.get_width()-chessboard.get_width())/2), mouse_pos[1] - ((screen.get_height()-chessboard.get_height())/2))
                        if turn == 1: array = white
                        else: array = black
                        for i in array:
                            if i.rect.collidepoint(mouse_pos):
                                active = i
                                active.is_active()
                else:
                    if event.button == 3:
                        active.is_not_active()
                        active = ""
                    elif event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        mouse_pos = (mouse_pos[0] - ((screen.get_width()-chessboard.get_width())/2), mouse_pos[1] - ((screen.get_height()-chessboard.get_height())/2))
                        for place in spaces:
                            if place.rect.collidepoint(mouse_pos):
                                can_jump.clear()
                                can_jump_queens.clear()
                                active.jump_possible()
                                if can_jump == [] and can_jump_queens == []:
                                    active.move(place.which_one)
                                    active.is_not_active()
                                    active = ""
                                    break
                                else:
                                    active.jump(place.which_one)
                                    active.is_not_active()
                                    active = ""
                                    break
                        if active != "":
                            active.is_not_active()
                        active = ""

        screen.fill((134,111,188))
        screen.blit(chessboard, chessboard.get_rect(center = screen.get_rect().center))
        for place in spaces:
            chessboard.blit(place.surf, (place.position))

        pieces = white
        for i in range(2):
            for p in pieces:
                chessboard.blit(p.surf, coordinates[p.old_position()])
                p.rect = pygame.Rect(coordinates[p.old_position()], (60,60))
            pieces = black

        pygame.display.flip()