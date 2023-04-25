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
        self.has_moved = False
        if self.color == 'b':
            self.picture = '♟︎'
        else:
            self.picture = '♙'

    def check_move(self, finish, to_go, board):
        if self.col == finish[1]:
            if board.hod == 'w':
                row = self.row - finish[0]
                if row == 2 and not self.has_moved and not board.board[self.row - 1][self.col]:
                    self.has_moved = 2
                    return True
                elif row == 1 and not to_go:
                    return True
            elif board.hod == 'b':
                row = finish[0] - self.row
                if row == 2 and not self.has_moved  and not board.board[self.row + 1][self.col]:
                    self.has_moved = 2
                    return True
                elif row == 1 and not to_go:
                    return True
        if abs(self.col - finish[1]) == 1:
            if board.hod == 'w':
                row = self.row - finish[0]
                check_row = self.row
                check_col = finish[1]
                piece = board.board[check_row][check_col]

                if row == 1 and to_go and to_go.color == 'b':
                    return True
                if row == 1 and piece and type(piece).__name__ == 'Pawn':
                    if board.moves and board.moves[-1][-1] == piece and piece.has_moved == 2:
                        board.remove(check_row, check_col)
                        return True
            elif board.hod == 'b':
                check_row = self.row
                check_col = finish[1]
                row = finish[0] - self.row
                piece = board.board[check_row][check_col]
                if row == 1 and piece and type(piece).__name__ == 'Pawn':
                    if board.moves and board.moves[-1][-1] == piece and piece.has_moved == 2:
                        board.remove(check_row, check_col)
                        return True
                if row == 1 and to_go and to_go.color == 'w':
                    return True
        # 4) пешка, при достижении конца поля может превратиться в любую другую фигуру кроме пешки или короля 
        # 5) пешка уязвима к взятию на проходе и способна его делать
        return False
        # raise Exception('То ли ты собрался сделать взятие на проходе, то ли Я не знаю!!!!!!!!!')
            



class King(Piece):
    def __init__(self, color, row, col) -> None:
        super().__init__(color, row, col)
        self.has_moved = False
        if self.color == 'b':
            self.picture = '♚'
        else:
            self.picture = '♔'

    def check_move(self, finish, to_go, board):
        if -1 <= self.row - finish[0] <= 1 and -1 <= self.col - finish[1] <= 1:
            self.has_moved = True
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
        return False


class Rook(Piece):
    def __init__(self, color, row, col) -> None:
        super().__init__(color, row, col)
        self.has_moved = False
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
            self.has_moved = True
            return True
        return False


class Bishop(Piece):
    def __init__(self, color, row, col) -> None:
        super().__init__(color, row, col)
        if self.color == 'b':
            self.picture = '♝'
        else:
            self.picture = '♗'

    def check_move(self, finish, to_go, board):
        if abs(self.row - finish[0]) == abs(self.col - finish[1]) != 0:
            n = abs(self.row - finish[0])
            dir_x = abs(finish[0] - self.row) // (finish[0] - self.row)
            dir_y = abs(finish[1] - self.col) // (finish[1] - self.col)
            for i in range(1, n):
                piece = board.board[self.row + dir_x * i][self.col + dir_y * i]
                if piece:
                    return False
            return True
        return False


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


