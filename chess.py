import pygame
pygame.init()


class Piece:
    def __init__(self, color, x, y) -> None:
        self.color = color
        self.x = x
        self.y = y
        self.pictures = ''
        
    def check_move(self):
        pass

    def move(self, finish):
        self.x = finish[1]
        self.y = finish[0]

    def draw(self, screen, width, height, size):
        font1 = pygame.font.SysFont('segoeuisymbol', int(width * 0.8) // 9)
        text = font1.render(self.picture, True, (0, 0, 0))
        x = size * self.x
        y = size * self.y + size * 0.1
        screen.blit(text, (y, x))



        




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
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.size = self.width // 9
        self.hod = 'w'
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
             King('w', 7, 4), Bishop('w', 7, 5), Knight('w', 7, 6), Rook('w', 7, 7)],           
        ]

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
        
    def make_move(self, start, finish):
        start = self.coords_to_x_y(start)
        finish = self.coords_to_x_y(finish)
        piece = self.board[start[1]][start[0]]
        to_go = self.board[finish[1]][finish[0]]
        if piece and piece.color == self.hod:
            if piece and not to_go:
                self.board[start[1]][start[0]], self.board[finish[1]][finish[0]] = to_go, piece
                piece.move(finish)
                if self.hod == 'b':
                    self.hod = 'w'
                else:
                    self.hod = 'b'
            if piece and to_go and to_go.color != piece.color:
                self.board[start[1]][start[0]], self.board[finish[1]][finish[0]] = None, piece
                piece.move(finish)
                if self.hod == 'b':
                    self.hod = 'w'
                else:
                    self.hod = 'b'


    def draw(self, screen):
        for i in range(8):
            row = self.board[i]
            for j in range(8):
                piece = row[j]
                x = self.size * i
                y = self.size * j
                if (i + j) % 2:
                    pygame.draw.rect(screen, (122, 122, 122), (y, x, self.size, self.size))
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (y, x, self.size, self.size))
                if piece:
                    piece.draw(screen, self.width, self.width, self.size)
        font1 = pygame.font.SysFont('segoeuisymbol', int(self.width * 0.8) // 9)
        for i in range(8):
            text = font1.render(str(9 - (i + 1)), True, (0, 0, 0))
            screen.blit(text, (self.size * 8.1, self.size * i))
        letters = 'abcdefgh'
        for i in range(len(letters)):
            text = font1.render(letters[i], True, (0, 0, 0))
            screen.blit(text, (self.size * i, self.size * 8.1))

