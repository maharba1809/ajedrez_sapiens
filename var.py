print('Loading vars')
import pygame
import defaults as df

class Frame():
    def __init__(self):
        print('Loading Video')
        print('pygame initialized')
        pygame.init()
        print('created caption')
        pygame.display.set_caption('Ajedrez 0.0')
        print('created Game display')
        self.gameDisplay = pygame.display.set_mode( (  df.display_width, df.display_height ) )
        self.fps = 30
        self.clock = pygame.time.Clock()
        self.w = df.display_width
        self.h = df.display_height
        print('Frame done')

frame = Frame()
layer_board = []


