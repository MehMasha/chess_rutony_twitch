import pygame
from chess import ChessBoard


pygame.init()

WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

game = True
board = ChessBoard(WIDTH, HEIGHT)

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()      
    screen.fill((200, 200, 200))
    board.draw(screen)
    pygame.display.flip()
    clock.tick(30)

    print(f'Сейчас ходят: {board.hod}')
    hod = input('Введите кто и куда ходит:')
    # try:
    hod = hod.split()
    start, finish = hod
    board.make_move(start, finish)
    # except:
    #     print('Некорректный формат хода')



