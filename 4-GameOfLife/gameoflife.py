import pygame, sys
from pygame.locals import *
from pygame.rect import Rect

CELL_SIZE = 50

class Cell():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = False
        self.rect = None

    def __repr__(self):
        return str(self.alive) + " " + "X: " + str(self.x) + " " + "Y: " + " " + str(self.y)

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

    def get_neighbors(self,grid):
        neighbors = []
        neighbors_alive = []
        x = self.x - CELL_SIZE
        y = self.y - CELL_SIZE
        while x < self.x + CELL_SIZE + CELL_SIZE:
            while y <= self.y + CELL_SIZE :
                if not(x == self.x and y == self.y):
                    neighbors += [sprite for sprite in grid if sprite.get_rect().collidepoint(x, y)]
                y += CELL_SIZE
            x += CELL_SIZE
            y = self.y - CELL_SIZE
        for neighbor in neighbors:
            if neighbor.is_alive():
                neighbors_alive.append(neighbor)
        return len(neighbors_alive)

    def miracle_of_life(self, grid):
        neighbors = self.get_neighbors(grid)
        print(neighbors)
        if self.is_alive() != True:
            if neighbors == 3:
                self.live()
        else:
            if neighbors > 3 or neighbors < 2:
                self.die()
            elif neighbors == 2 or neighbors ==3:
                pass
        self.get_neighbors(grid)

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

    time = 0
    pygame.time.set_timer(USEREVENT+1, 1000)
    while True:
        if time < 1:
            for cell in grid:
                cell.miracle_of_life(grid)
                update_cell(grid, DISPLAY, cell.x, cell.y)
                cell.draw(DISPLAY)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == USEREVENT+1:
                time -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                time = 5
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
                    print(sprite)
                    sprite.miracle_of_life(grid)
        pygame.display.update()

main()
