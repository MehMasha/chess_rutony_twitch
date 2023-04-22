import pygame
pygame.init()


class Piece:
    def __init__(self, color, x, y) -> None:
        self.color = color
        self.x = x
        self.y = y
        self.pictures = ''

    def coords_to_x_y(self, coords):
        letters = 'abcdefgh'
        try:
            x, y = list(coords.lower())
            x = letters.find(x)
            y = 7 - (int(y) - 1)
            if 0 <= x <= 7 and 0 <= y <= 7:
                return x, y
            return
        except:
            print(f'Что-то не то с ходом {coords}')
            return
        
    def check_move(self):
        pass

    def move(self):
        pass

    def draw(self, screen, width, height):
        font1 = pygame.font.Font(width // 8)
        text = font1.render(self.picture, True, (0, 0, 0))
        x = (width // 8) * self.x
        y = (width // 8) * self.y
        screen.blit(text, (x, y))



        




class Pawn(Piece):
    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)
        if self.color == 'b':
            self.picture = '♟︎'
        else:
            self.picture = '♙'

    def check_move(self):
        pass


class King(Piece):
    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)
        if self.color == 'b':
            self.picture = '♚'
        else:
            self.picture = '♔'

    def check_move(self):
        pass


class Queen(Piece):
    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)
        if self.color == 'b':
            self.picture = '♛'
        else:
            self.picture = '♕'

    def check_move(self):
        pass


class Rook(Piece):
    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)
        if self.color == 'b':
            self.picture = '♜'
        else:
            self.picture = '♖'

    def check_move(self):
        pass


class Bishop(Piece):
    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)
        if self.color == 'b':
            self.picture = '♝'
        else:
            self.picture = '♗'

    def check_move(self):
        pass


class Knight(Piece):
    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)
        if self.color == 'b':
            self.picture = '♞'
        else:
            self.picture = '♘'

    def check_move(self):
        pass





class ChessBoard:
    def __init__(self) -> None:
        self.board = [
            [Rook('b', 0, 0), Knight('b', 0, 1), Bishop('b', 0, 2), Queen('b', 0, 3),
             King('b', 0, 4), Bishop('b', 0, 5), Knight('b', 0, 6), Rook('b', 0, 7)],
            [Pawn('b', 1, 0), Pawn('b', 1, 1), Pawn('b', 1, 2), Pawn('b', 1, 3),
             Pawn('b', 1, 4), Pawn('b', 1, 5), Pawn('b', 1, 6), Pawn('b', 1, 7)],
             [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None],
            [Pawn('w', 6, 0), Pawn('w', 6, 1), Pawn('w', 6, 2), Pawn('w', 6, 3),
             Pawn('w', 6, 4), Pawn('w', 6, 5), Pawn('w', 6, 6), Pawn('w', 6, 7)],  
            [Rook('w', 7, 0), Knight('w', 7, 1), Bishop('w', 7, 2), Queen('w', 7, 3),
             King('w', 7, 6), Bishop('w', 7, 5), Knight('w', 7, 6), Rook('w', 7, 7)],           
        ]

    def draw(self):
        for row in self.board:
            for piece in row:
                if piece:
                    piece.draw()