import pygame, sys
from pygame.locals import *

def generate_grid(display,x_size, y_size):
    x = 0
    y = 0
    grid = []
    while x < x_size:
        while y < y_size:
            grid.append(pygame.draw.rect(display, (255, 255, 255), (x, y, 50, 50), 1))
            y += 50
        x += 50
        y = 0
    return grid


def main():
    x_screen = 1000
    y_screen = 1000
    pygame.init()
    DISPLAY = pygame.display.set_mode((x_screen,y_screen),0,32)
    BLACK=(0,0,0)

    DISPLAY.fill(BLACK)
    grid = generate_grid(DISPLAY, x_screen, y_screen)


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                sprites_clicked = [sprite for sprite in grid if sprite.collidepoint(x, y)]
                print(sprites_clicked)
        pygame.display.update()

main()
