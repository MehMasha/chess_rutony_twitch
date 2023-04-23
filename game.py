import pygame
from chess import ChessBoard


pygame.init()

WIDTH = 700
HEIGHT = 700

clock = pygame.time.Clock()

game = True
board = ChessBoard(WIDTH, HEIGHT)

WIDTH = WIDTH // 9 * 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main(q):
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()      
        screen.fill((200, 200, 200))
        board.draw(screen)
        pygame.display.flip()
        clock.tick(30)
        if not q.empty():
            a = q.get_nowait()
            print(f'Привет из функции main для {a}')

            print(f'Сейчас ходят: {board.hod}')
            hod = a
            try:
                board.make_move(hod)
            except Exception as e:
                print(f'Что-то пошло не так: {e}')


if __name__ == '__main__':
    main()


