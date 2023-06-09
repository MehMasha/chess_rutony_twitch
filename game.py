import pygame
from chess import ChessBoard


pygame.init()

WIDTH = 700
HEIGHT = 700

clock = pygame.time.Clock()

game = True
board = ChessBoard(WIDTH, HEIGHT)

WIDTH = WIDTH // 9 * 11
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.event.set_grab(True)
font1 = pygame.font.SysFont('segoeuisymbol', int(WIDTH * 0.8) // 9)

def main(q):
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()      
        screen.fill((200, 200, 200))
        board.draw(screen)
        pygame.display.flip() 
        clock.tick(10)        


        # Код закомментированный для игры без чата
        # hod = input('make move')
        # print(hod)
        # try:
        #     board.make_move(hod.split())
        # except Exception as e:
        #     print(f'Что-то пошло не так: {e}')
        if not q.empty():
            a = q.get_nowait()
            hod = a
            try:
                board.make_move(hod)
            except Exception as e:
                print(f'Что-то пошло не так: {e}')



if __name__ == '__main__':
    main(1)


