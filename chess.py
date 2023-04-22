import pygame
pygame.init()


class Piece:
    def __init__(self, color, row, col) -> None:
        self.color = color
        self.row = row
        self.col = col
        self.pictures = ''
        
    def check_move(self, finish):
        pass

    def move(self, finish, to_go, board):
        if not self.check_move(finish, to_go, board):
            raise Exception('Не прошла проверка хода!')
        self.row = finish[0]
        self.col = finish[1]

    def draw(self, screen, width, height, size):
        font1 = pygame.font.SysFont('segoeuisymbol', int(width * 0.8) // 9)
        text = font1.render(self.picture, True, (0, 0, 0))
        row = size * self.row
        col = size * self.col + size * 0.1
        screen.blit(text, (col, row))


class Pawn(Piece):
    def __init__(self, color, row, col) -> None:
        super().__init__(color, row, col)
        self.not_moved = True
        if self.color == 'b':
            self.picture = '♟︎'
        else:
            self.picture = '♙'

    def check_move(self, finish, to_go, board):
        if self.col == finish[1]:
            if board.hod == 'w':
                row = self.row - finish[0]
                if row == 2 and self.not_moved and not board.board[self.row - 1][self.col]:
                    self.not_moved = False
                    return True
                elif row == 1:
                    return True
            elif board.hod == 'b':
                row = finish[0] - self.row
                if row == 2 and self.not_moved  and not board.board[self.row + 1][self.col]:
                    self.not_moved = False
                    return True
                elif row == 1:
                    return True
        if abs(self.col - finish[1]) == 1:
            if board.hod == 'w':
                row = self.row - finish[0]
                if row == 1 and to_go and to_go.color == 'b':
                    return True
            elif board.hod == 'b':
                row = finish[0] - self.row
                if row == 1 and to_go and to_go.color == 'w':
                    return True
        # 4) пешка, при достижении конца поля может превратиться в любую другую фигуру кроме пешки или короля 
        # 5) пешка уязвима к взятию на проходе и способна его делать
        raise Exception('То ли ты собрался сделать взятие на проходе, то ли Я не знаю!!!!!!!!!')
            



class King(Piece):
    def __init__(self, color, row, col) -> None:
        super().__init__(color, row, col)
        self.not_moved = True
        if self.color == 'b':
            self.picture = '♚'
        else:
            self.picture = '♔'

    def check_move(self, finish, to_go, board):
        # Параметр "ходил ли" для короля. Проверили. 
        # Далее мы на основании описания рокировки (0-0 или 0-0-0) проверяем клетки на пустоту в нужную сторону. 
        # Находим (или нет) ладью. У найденной Ладьи проверяем тот же параметр "ходила ли"
        if -1 <= self.row - finish[0] <= 1 and -1 <= self.col - finish[1] <= 1:
            return True
        return False


class Queen(Piece):
    def __init__(self, color, row, col) -> None:
        super().__init__(color, row, col)
        if self.color == 'b':
            self.picture = '♛'
        else:
            self.picture = '♕'

    def check_move(self, finish, to_go, board):
        diff_row = abs(self.row - finish[0])
        diff_col = abs(self.col - finish[1])
        dir_x = 0
        dir_y = 0
        if diff_row == diff_col or not diff_row or not diff_col:
            n = max(diff_row, diff_col)
            if diff_row:
                dir_x = abs(finish[0] - self.row) // (finish[0] - self.row)
            if diff_col:
                dir_y = abs(finish[1] - self.col) // (finish[1] - self.col)
            for i in range(1, n):
                piece = board.board[self.row + dir_x * i][self.col + dir_y * i]
                if piece:
                    return False
            return True


class Rook(Piece):
    def __init__(self, color, row, col) -> None:
        super().__init__(color, row, col)
        if self.color == 'b':
            self.picture = '♜'
        else:
            self.picture = '♖'

    def check_move(self, finish, to_go, board):
        diff_row = abs(self.row - finish[0])
        diff_col = abs(self.col - finish[1])
        dir_x = 0
        dir_y = 0
        if not diff_row or not diff_col:
            n = max(diff_row, diff_col)
            if diff_row:
                dir_x = abs(finish[0] - self.row) // (finish[0] - self.row)
            if diff_col:
                dir_y = abs(finish[1] - self.col) // (finish[1] - self.col)
            for i in range(1, n):
                piece = board.board[self.row + dir_x * i][self.col + dir_y * i]
                if piece:
                    return False
            return True


class Bishop(Piece):
    def __init__(self, color, row, col) -> None:
        super().__init__(color, row, col)
        if self.color == 'b':
            self.picture = '♝'
        else:
            self.picture = '♗'

    def check_move(self, finish, to_go, board):
        if abs(self.row - finish[0]) == abs(self.col - finish[1]):
            n = abs(self.row - finish[0])
            dir_x = abs(finish[0] - self.row) // (finish[0] - self.row)
            dir_y = abs(finish[1] - self.col) // (finish[1] - self.col)
            for i in range(1, n):
                piece = board.board[self.row + dir_x * i][self.col + dir_y * i]
                if piece:
                    return False
            return True


class Knight(Piece):
    def __init__(self, color, row, col) -> None:
        super().__init__(color, row, col)
        if self.color == 'b':
            self.picture = '♞'
        else:
            self.picture = '♘'

    def check_move(self, finish, to_go, board):
        if abs(self.row - finish[0]) == 1 and abs(self.col - finish[1]) == 2:
            return True
        elif abs(self.row - finish[0]) == 2 and abs(self.col - finish[1]) == 1:
            return True
        return False



class ChessBoard:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.size = self.width // 9
        self.hod = 'w'
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

    def coords_to_x_y(self, coords):
        letters = 'abcdefgh'
        try:
            row, col = list(coords.lower())
            col1 = letters.find(row)
            row1 = 7 - (int(col) - 1)
            if 0 <= row1 <= 7 and 0 <= col1 <= 7:
                return row1, col1
            raise Exception('Координаты вне поля')
        except Exception as e:
            print(f'Что-то не то с ходом {coords}')
            raise Exception(f'Некорректный формат: {e}')
        
    def make_move(self, hod):
        try:
            start, finish = hod.lower().split()
        except:
            raise Exception('Некорректный формат')
        start = self.coords_to_x_y(start)
        finish = self.coords_to_x_y(finish)
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
            elif piece and to_go and to_go.color != piece.color:
                piece.move(finish, to_go, self)
                self.board[start[0]][start[1]], self.board[finish[0]][finish[1]] = None, piece
                if self.hod == 'b':
                    self.hod = 'w'
                else:
                    self.hod = 'b'
                self.count += 1
            else:
                raise Exception('Так ходить нельзя')
        else:
            raise Exception('Так ходить нельзя')


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

