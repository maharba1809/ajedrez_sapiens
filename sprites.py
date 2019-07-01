import pygame
import os
import defaults as df
import random
import time
import var


class Sprite():
    def __init__(self):
        self.file = ""
        self.rect = []
        self.image = []
        self.w = 0
        self.h = 0

    def load_image(self):
        self.image = pygame.image.load(self.file)
        self.image = pygame.transform.scale(self.image, (int(self.w), int(self.h)))
        self.rect = self.image.get_rect()

    def draw(self):
        var.frame.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))


class Background(Sprite):

    def __init__(self):
        Sprite.__init__(self)
        self.file = df.assetsDir + 'gradient-1761190_1280.jpg'
        self.w = df.display_width
        self.h = df.display_height
        self.load_image()
        self.rect.x = 0
        self.rect.y = 0
        print('created Background from:',self.file)


class Piece(Sprite):
    def __init__(self, key,  team, file1, file2):
        Sprite.__init__(self)
        self.subdir = 'pieces/'
        if team =='w':filename = file1
        else: filename = file2
        self.file = df.assetsDir + self.subdir + filename
        self.w = 75
        self.h = self.w
        self.load_image()
        x, y = var.layer_board.get_xy_from_key(key)
        var.layer_board.empty_square(key,False)
        self.rect.x = x
        self.rect.y = y
        self.team = team
        self.clicked = False
        self.origin = (self.rect.x, self.rect.y)
        self.key = key
        print('created King:', self.file)
        self.selected = False

    def eat(self,key,enemy):
        if self.rules(key):
            print('comiendo enemigo:', type(self), type(enemy), key)
            return True
        return False

    def move(self, to_key):
        var.layer_board.empty_square(self.key,True)
        var.layer_board.empty_square(to_key,False)
        self.rect.x, self.rect.y = var.layer_board.get_xy_from_key(to_key)
        self.selected = False
        self.key = to_key

    def highlight(self,color):
        s = pygame.Surface((self.rect.w, self.rect.h))
        s.set_alpha(50)
        s.fill(color)
        pygame.draw.rect(var.frame.gameDisplay, color, [self.rect.x, self.rect.y, self.rect.w, 3])
        pygame.draw.rect(var.frame.gameDisplay, color, [self.rect.x, self.rect.y, 3, self.rect.h])
        pygame.draw.rect(var.frame.gameDisplay, color, [self.rect.x, self.rect.y + self.rect.h, self.rect.w, 3])
        pygame.draw.rect(var.frame.gameDisplay, color, [self.rect.x + self.rect.w, self.rect.y, 3, self.rect.h])
        # var.gameDisplay.blit(s, (self.rect.x, self.rect.y))

    def onClick(self,mouse):
        if self.rect.collidepoint(mouse.get_pos()) == 1:
            if mouse.get_pressed()[0]:
                self.highlight(df.red)
                # self.animating = True

                # print('button clicked', self.file)
                # self.index = 0
                time.sleep(0.1)
                return True


        # else:
            # self.highlight_color = self.hover_color

        # if self.animating:self.animate()

        # self.draw_sprite2()
        # if self.animating  or not self.clicked:


            # return  #continue running
        # else:
            # self.clicked = False
            # return True #clicken event is true
        return False

    def get_cartesian(self,key):

        self.x0 = int(ord(self.key[0]))
        self.x1 = int(ord(key[0]))
        self.y0 = int(self.key[1])
        self.y1 = int(key[1])

    def rules(self, key):
        pass

class King(Piece):
    def __init__(self, key, team):
        file1 = 'wking.png'
        file2 = 'bking.png'
        Piece.__init__(self, key, team, file1, file2)
        print('created:', self.file)



    def rules(self, key):
        self.get_cartesian(key)
        print('Moviendo', type(self), 'de', self.key, 'hacia', key)
        x1 = self.x1
        x0 = self.x0
        y1 = self.y1
        y0 = self.y0

        if abs(x0-x1) <2 and abs(y0 - y1) < 2:
            return True
        else:
            print('Movimiento invalido para', type(self))
        return False


class Queen(Piece):

    def __init__(self, key, team):
        file1 = 'wqueen.png'
        file2 = 'bqueen.png'
        Piece.__init__(self, key, team, file1, file2)
        print('created:', self.file)

    def rules(self, key):
        self.get_cartesian(key)
        print('Moviendo', type(self), 'de', self.key, 'hacia', key)
        x1 = self.x1
        x0 = self.x0
        y1 = self.y1
        y0 = self.y0

        if x1 == x0 or y1== y0 or abs(x0 - x1) == abs(y0 - y1):
            return True
        else:
            print('Movimiento invalido para', type(self))
        return False


class Rook(Piece):
    def __init__(self, key, team):
        file1 = 'wrook.png'
        file2 = 'brook.png'
        Piece.__init__(self, key, team, file1, file2)
        print('created:', self.file)


    def rules(self, key):
        self.get_cartesian(key)
        print('Moviendo', type(self), 'de', self.key, 'hacia', key)
        x1 = self.x1
        x0 = self.x0
        y1 = self.y1
        y0 = self.y0

        if x1 == x0 or y1 == y0:
            return True
        else:
            print('Movimiento invalido para', type(self))
        return False


class Bishop(Piece):
    def __init__(self, key, team):
        file1 = 'wbishop.png'
        file2 = 'bbishop.png'
        Piece.__init__(self, key, team, file1, file2)
        print('created:', self.file)

    def rules(self, key):
        self.get_cartesian(key)
        x1 = self.x1
        x0 = self.x0
        y1 = self.y1
        y0 = self.y0

        print('Moviendo', type(self), 'de', self.key, 'hacia', key)

        if abs(x0 - x1) == abs(y0- y1):
            return True
        else:
            print('Movimiento invalido para', type(self))
        return False


class Knight(Piece):
    def __init__(self, key, team):
        file1 = 'wknight.png'
        file2 = 'bknight.png'
        Piece.__init__(self, key, team, file1, file2)
        print('created:', self.file)

    def rules(self, key):
        print('Moviendo', type(self), 'de', self.key, 'hacia', key)
        self.get_cartesian(key)
        x1 = self.x1
        x0 = self.x0
        y1 = self.y1
        y0 = self.y0

        if abs(x1 - x0)**2 + abs(y1 - y0)**2 == 5:
            return True
        else:
                print('Movimiento invalido para', type(self))
        return False


class Pawn(Piece):
    def __init__(self, key, team):
        file1 = 'wpawn.png'
        file2 = 'bpawn.png'
        Piece.__init__(self, key, team, file1, file2)
        print('created:', self.file)

    def rules(self, key):
        # pass
        print('Moviendo', type(self), 'de', self.key, 'hacia', key)
        self.get_cartesian(key)
        x1 = self.x1
        x0 = self.x0
        y1 = self.y1
        y0 = self.y0

        if self.team =='w':factor = 1
        else: factor = -1

        if abs(x1-x0) ==0 and y1-y0 == factor:
            return True
        else:
            print('Movimiento invalido para',type(self))

        return False

    def eat(self, key, enemy):
        print('comiendo enemigo:', type(self), type(enemy),key)
        self.get_cartesian(key)
        x1 = self.x1
        x0 = self.x0
        y1 = self.y1
        y0 = self.y0

        if self.team =='w':factor = 1
        else: factor = -1

        if abs(x1-x0) ==1 and y1-y0 == factor:
            return True
        else:
            print('Movimiento invalido',type(self))

        return False

