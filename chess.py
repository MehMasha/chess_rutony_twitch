class Piece:
    def __init__(self, color, x, y) -> None:
        self.color = color
        self.x = x
        self.y = y


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

    def draw(self):
        pass




class Pawn(Piece):
    def check_move(self):
        pass

    def draw(self, width, height):
        pass


class King(Piece):
    def check_move(self):
        pass


class Queen(Piece):
    def check_move(self):
        pass


class Rook(Piece):
    def check_move(self):
        pass


class Bishop(Piece):
    def check_move(self):
        pass


class Knight(Piece):
    def check_move(self):
        pass





class ChessBoard:
    def __init__(self) -> None:
        self.board = [
            ['', '', '', ''],
        ]
        self.pictures = {
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
        }