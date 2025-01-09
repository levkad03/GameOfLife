import numpy as np
import pygame as p
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# create window
root = p.display.set_mode((1000, 500))

p.display.set_caption("Game of Life")

rows = root.get_height() // 20
cols = root.get_width() // 20

cells = np.random.choice([0, 1], size=(rows, cols))

age = np.zeros_like(cells)


def get_color(age):
    return (min(255, age * 20), 0, min(255, age * 20))


def count_neighbours(cells):
    return (
        np.roll(cells, 1, axis=0)  # up
        + np.roll(cells, -1, axis=0)  # down
        + np.roll(cells, 1, axis=1)  # left
        + np.roll(cells, -1, axis=1)  # right
        + np.roll(np.roll(cells, 1, axis=0), 1, axis=1)  # up-left
        + np.roll(np.roll(cells, 1, axis=0), -1, axis=1)  # up-right
        + np.roll(np.roll(cells, -1, axis=0), 1, axis=1)  # down-left
        + np.roll(np.roll(cells, -1, axis=0), -1, axis=1)  # down-right
    )


while 1:
    root.fill(WHITE)

    # Grid
    for i in range(0, root.get_height(), 20):
        p.draw.line(root, BLACK, (0, i), (root.get_width(), i))
    for j in range(0, root.get_width(), 20):
        p.draw.line(root, BLACK, (j, 0), (j, root.get_height()))

    for i in p.event.get():
        if i.type == QUIT:
            quit()

    # draw cells
    for i in range(rows):
        for j in range(cols):
            if cells[i, j]:
                p.draw.rect(root, get_color(age[i, j]), [j * 20, i * 20, 20, 20])

    neighbours = count_neighbours(cells)

    # game rules
    new_cells = np.zeros_like(cells)
    new_cells[(cells == 1) & ((neighbours == 2) | (neighbours == 3))] = 1
    new_cells[(cells == 0) & (neighbours == 3)] = 1

    age = (age + 1) * new_cells

    cells = new_cells
    # Update screen
    p.display.update()

    p.time.delay(100)
