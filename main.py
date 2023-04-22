import pygame
pygame.init()

WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()      
    screen.fill((122, 122, 122))



    pygame.display.flip()
    clock.tick(30)