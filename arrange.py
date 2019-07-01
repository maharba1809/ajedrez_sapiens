
from var import frame
import sprites as sp

class Config():
    def __init__(self):
        self.pieceList = []

    def std(self):
        for i in range(1,9):
            key = chr(ord('a') + i - 1) + str('7')
            self.pieceList.append(sp.Pawn( key,'b'))

        self.pieceList.append(sp.Rook('a8', 'b'))
        self.pieceList.append(sp.Rook('h8', 'b') )
        self.pieceList.append(sp.Bishop('c8','b') )
        self.pieceList.append(sp.Bishop('f8', 'b'))
        self.pieceList.append(sp.Knight('g8', 'b'))
        self.pieceList.append(sp.Knight('b8', 'b'))
        self.pieceList.append(sp.Queen('d8','b'))
        self.pieceList.append(sp.King('e8', 'b'))

        for i in range(1,9):
            key = chr(ord('a') + i-1) + str('2')
            self.pieceList.append(sp.Pawn(key, 'w'))

        self.pieceList.append(sp.Rook('a1', 'w'))
        self.pieceList.append(sp.Rook('h1', 'w'))
        self.pieceList.append(sp.Bishop('c1', 'w'))
        self.pieceList.append(sp.Bishop('f1', 'w'))
        self.pieceList.append(sp.Knight('b1', 'w'))
        self.pieceList.append(sp.Knight('g1', 'w'))
        self.pieceList.append(sp.Queen('e1', 'w'))
        self.pieceList.append(sp.King('d1', 'w'))

    def draw(self):
        for piece in self.pieceList:
            frame.gameDisplay.blit(piece.image, (piece.rect.x, piece.rect.y))

    def get_piece(self, key):
        for piece in self.pieceList:
            if piece.key == key:
                return piece
        print('pieza no fue identificada con la clave')
        return []

layout = Config()
layout.std()