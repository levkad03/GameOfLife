import time

import pygame as p
import random
from pygame import locals

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

root = p.display.set_mode((1000, 500))

while True:
    root.fill(WHITE)

    for i in range(0, root.get_height() // 20):
        p.draw.line(
            root,
            BLACK,
            (
                0,
                i * 20,
            ),
            (root.get_width(), i * 20),
        )
    for j in range(0, root.get_width() // 20):
        p.draw.line(root, BLACK, (j * 20, 0), (j * 20, root.get_height()))

    for i in p.event.get():
        if i.type == locals.QUIT:
            quit()

    p.display.update()
