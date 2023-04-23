import pygame
pygame.init()

from pieces import *


class ChessBoard:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.size = self.width // 9
        self.hod = 'w'
        self.last_move = (None, None)
        self.moves = []
        self.count = 0
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
        self.whites = []
        self.blacks = []
        for i in range(8):
            self.whites.append(self.board[0][i])
            self.whites.append(self.board[1][i])
            self.blacks.append(self.board[6][i])
            self.blacks.append(self.board[7][i])

    def coords_to_x_y(self, coords):
        letters = 'abcdefgh'
        try:
            row, col = list(coords.lower())
            print(row, col, coords)
            if row not in letters:
                raise Exception('Координаты вне поля буква')
            col1 = letters.find(row)
            row1 = 7 - (int(col) - 1)
            if 0 <= row1 <= 7 and 0 <= col1 <= 7:
                return row1, col1
            raise Exception('Координаты вне поля')
        except Exception as e:
            print(f'Что-то не то с ходом {coords}')
            raise Exception(f'Некорректный формат: {e}')
        
    def check_rock(self, color, row, col):
        if color == 'b':
            pieces = self.blacks
        else:
            pieces = self.whites
        for p in pieces:
            if p.check_move((row, col), self.board[row][col], self):
                return False
        return True

    def make_move(self, hod):
        start1, finish1, player, site = hod
        print(hod)
        # try:
        #     start, finish, player, site = hod.lower().split()
        # except:
        #     raise Exception('Некорректный формат')
        start = self.coords_to_x_y(start1)
        finish = self.coords_to_x_y(finish1)
        piece = self.board[start[0]][start[1]]
        to_go = self.board[finish[0]][finish[1]]
        if piece and piece.color == self.hod:
            if piece and not to_go:
                piece.move(finish, to_go, self)
                self.board[start[0]][start[1]], self.board[finish[0]][finish[1]] = to_go, piece
                if self.hod == 'b':
                    self.hod = 'w'
                else:
                    self.hod = 'b'
                self.count += 1
                self.last_move = (start, finish)
                self.moves.append((start1, finish1, player, site, piece))
            elif piece and to_go and to_go.color != piece.color:
                piece.move(finish, to_go, self)
                self.board[start[0]][start[1]], self.board[finish[0]][finish[1]] = None, piece
                if self.hod == 'b':
                    self.hod = 'w'
                else:
                    self.hod = 'b'
                if to_go in self.whites:
                    self.whites.remove(to_go)
                if to_go in self.blacks:
                    self.blacks.remove(to_go)
                self.count += 1
                self.last_move = (start, finish)
                self.moves.append((start1, finish1, player, site, piece))
            else:
                raise Exception('Так ходить нельзя')
        else:
            raise Exception('Так ходить нельзя')
    
    def remove(self, row, col):
        piece = self.board[row][col]
        self.board[row][col] = None
        if piece in self.whites:
            self.whites.remove(piece)
        if piece in self.blacks:
            self.blacks.remove(piece)


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
        if self.last_move[0] and self.last_move[1]:
            a1 = self.last_move[0]
            a2 = self.last_move[1]
            pygame.draw.rect(screen, (230, 122, 230), (a1[1] * self.size, a1[0] * self.size, self.size, self.size), self.size // 10)
            pygame.draw.rect(screen, (230, 122, 230), (a2[1] * self.size, a2[0] * self.size, self.size, self.size), self.size // 10)



        font1 = pygame.font.SysFont('segoeuisymbol', int(self.width * 0.8) // 9)
        font2 = pygame.font.SysFont('segoeuisymbol', int(self.width * 0.8) // 27)
        for i in range(8):
            text = font1.render(str(9 - (i + 1)), True, (0, 0, 0))
            screen.blit(text, (self.size * 8.1, self.size * i))
        letters = 'abcdefgh'
        for i in range(len(letters)):
            text = font1.render(letters[i], True, (0, 0, 0))
            screen.blit(text, (self.size * i, self.size * 8.1))
        if self.hod == 'b':
            text = font1.render('B', True, (0, 0, 0))
            screen.blit(text, (self.size * 9.1, self.size * 0.1))
        else:
            text = font1.render('W', True, (0, 0, 0))
            screen.blit(text, (self.size * 9.1, self.size * 0.1)) 
        moves = self.moves[-10:]
        for i in range(len(moves)):
            move = moves[i]
            text1 = font2.render(f'{move[3]} {move[2]}', True, (0, 0, 0))
            text2 = font2.render(f'     {move[0]} {move[1]}', True, (0, 0, 0))
            screen.blit(text1, (self.size * 9.1, self.size * (1 + 0.25 * (2 * i)))) 
            screen.blit(text2, (self.size * 9.1, self.size * (1 + 0.25 * (2 * i + 1)))) 

