
import sprites as sp
from var import frame
import defaults as df
import var
import pygame
import time

class Square(sp.Sprite):
    def __init__(self, color, x, y, w, key):
        sp.Sprite.__init__(self)
        if color =='w':
            self.file = df.assetsDir + 'squarew.jpg'
        else:
            self.file = df.assetsDir + 'squareb.jpg'
        self.w = w
        self.h = self.w
        self.load_image()
        self.rect.x = x
        self.rect.y = y
        self.empty = True
        self.key = key
        print('created Board Game from:', self.file)

    def highlight(self,color):
        s = pygame.Surface((self.rect.w, self.rect.h))
        s.set_alpha(50)
        s.fill(color)
        pygame.draw.rect(var.frame.gameDisplay, color, [self.rect.x, self.rect.y, self.rect.w, 3])
        pygame.draw.rect(var.frame.gameDisplay, color, [self.rect.x, self.rect.y, 3, self.rect.h])
        pygame.draw.rect(var.frame.gameDisplay, color, [self.rect.x, self.rect.y + self.rect.h, self.rect.w, 3])
        pygame.draw.rect(var.frame.gameDisplay, color, [self.rect.x + self.rect.w, self.rect.y, 3, self.rect.h])
        # var.gameDisplay.blit(s, (self.rect.x, self.rect.y))

    def onClick(self, mouse):
        if self.rect.collidepoint(mouse.get_pos()) == 1:
            # print(self.empty)
            if self.empty:
                self.highlight(df.green)
            else:
                self.highlight(df.red)

            if mouse.get_pressed()[0]:
                # self.animating = True
                # self.clicked = True
                self.origin = (self.rect.x, self.rect.y)
                # print('button clicked', self.file)
                # self.index = 0
                time.sleep(0.5)
                return True
        return False

class BoardGame(sp.Sprite):
    def __init__(self):
        sp.Sprite.__init__(self)
        self.w = 600
        self.dx = self.w / 8
        self.dy = self.dx
        self.sqs = []
        self.h = self.w
        color = 'w'
        x0 = 0.5 * (frame.w - self.w)
        y = 0.5 * (frame.h - self.h)
        x = x0

        for i in range(1,9):
            n = 9 - i
            for j in range(1,9):

                key = chr(ord('a')+j-1) + str(n)
                # print(key)
                self.sqs.append(Square(color, x, y, abs(self.dx), key))

                x += self.dx

                if color == 'w': color = 'b'
                else: color = 'w'

            x = x0
            if color == 'w': color = 'b'
            else:color = 'w'
            y += self.dy

        # grid = self.sqs

        print('created layer Game from:',self.file)

    def draw(self):
        for sq in self.sqs:
            frame.gameDisplay.blit(sq.image, (sq.rect.x, sq.rect.y))


    def get_xy_from_key(self,key):
        for sq in self.sqs:
            if sq.key == key:
                return sq.rect.x, sq.rect.y

    def empty_square(self,key,empty_value):
        for sq in self.sqs:
            if sq.key == key:
                sq.empty = empty_value



board = BoardGame()
var.layer_board = board
# print(board.get_xy_from_key('a1'))