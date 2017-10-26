import pygame, sys
from pygame.locals import *
from pygame.rect import Rect


class Cell():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = False
        self.rect = None

    def get_rect(self):
        return self.rect

    def draw(self, display):
        if self.alive:
            alive = 0
        else:
            alive = 1
        print(alive)
        self.rect = pygame.draw.rect(display, (255, 255, 255), (self.x, self.y, 50, 50), alive)
        return self.rect

    def is_alive(self):
        return self.alive

    def live(self):
        self.alive = True

    def die(self):
        self.alive = False

def generate_grid(display,x_size, y_size):
    x = 0
    y = 0
    grid = []
    while x < x_size:
        while y < y_size:
            cell = Cell(x, y)
            cell.draw(display)
            grid.append(cell)
            y += 50
        x += 50
        y = 0
    return grid

def update_cell(grid, display, x, y):
    pygame.draw.rect(display, (0, 0, 0), (x, y, 50, 50), 0)
    pygame.draw.rect(display, (255, 255, 255), (x, y, 50, 50), 1)

def main():
    x_screen = 500
    y_screen = 500
    pygame.init()
    DISPLAY = pygame.display.set_mode((x_screen,y_screen),0,32)
    BLACK=(0,0,0)

    DISPLAY.fill(BLACK)
    grid = generate_grid(DISPLAY, x_screen, y_screen)
    cell = Cell(0, 0)

    while True:
        rect = None

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                sprites_clicked = [sprite for sprite in grid if sprite.get_rect().collidepoint(x, y)]
                print(sprites_clicked)
                for sprite in sprites_clicked:
                    if sprite.is_alive():
                        sprite.die()
                    else:
                        sprite.live()
                    update_cell(grid, DISPLAY, sprite.x, sprite.y)
                    sprite.draw(DISPLAY)


        pygame.display.update()

main()
