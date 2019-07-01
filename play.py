
import imp

import pygame

import defaults as df
import layer as ly
import var #brfore arrange
import arrange as arr
import sprites as sp

print('Loading play')
class Screen():
    def __init__(self):
        print('play screen open...')
        self.stopEngine = False

    def run(self):
        imp.reload(sp)
        print('\n')
        background = sp.Background()
        total_time = 0
        selected_piece = False
        selected_key = False
        free_piece = False

        while not self.stopEngine:
            time_start = pygame.time.get_ticks()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    free_piece = True
                    print('librando pieza')
                else:
                    free_piece = False


            var.frame.gameDisplay.fill(df.blue)
            background.draw()

            var.layer_board.draw()
            arr.layout.draw()

            for piece in arr.layout.pieceList:

                if piece.selected:
                    piece.rect.x, piece.rect.y = pygame.mouse.get_pos()
                    piece.rect.x += 10
                    piece.rect.y += 10
                    piece.highlight(df.blue)


                if free_piece and piece.selected:
                    print('Deselecciónaste:', type(piece), piece.key)
                    piece.selected = False
                    selected_piece = piece.selected
                    piece.rect.x, piece.rect.y = piece.origin
                    break

                if piece.onClick(pygame.mouse):
                    if not selected_piece:
                        print('Selecciónaste:', type(piece), piece.key)
                        piece.origin = (piece.rect.x, piece.rect.y)
                        piece.selected = True
                        selected_piece = piece.selected
                        selected_key = piece.key
                    break

            for square in ly.board.sqs:
                if square.onClick(pygame.mouse):
                    if selected_key == square.key:#in case long click
                        break
                    print('Seleccionaste',square.key)
                    for piece in arr.layout.pieceList:
                        if piece.selected:
                            if square.empty:
                                if piece.rules(square.key):
                                    piece.move(square.key)
                                    selected_piece = False
                                    selected_key= False
                            else:
                                piece0 = arr.layout.get_piece(square.key)
                                if piece.team == piece0.team:
                                    print('este lugar esta ocupado por un compañero',type(piece0))
                                else:
                                    if piece.eat(square.key, piece0):
                                        var.layer_board.empty_square(piece0.key, True)
                                        arr.layout.pieceList.remove(piece0)
                                        piece.move(square.key)
                                        selected_key = False
                                        selected_piece = False
                            break

                    break

            var.frame.clock.tick(var.frame.fps)
            dt = pygame.time.get_ticks() - time_start

            total_time += dt
            pygame.display.update()



