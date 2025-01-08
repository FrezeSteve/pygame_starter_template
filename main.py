import pygame as pg
from pygame.locals import DOUBLEBUF, HWSURFACE

WIDTH = 480
HEIGHT = 600
TITLE = "Shmup"
FPS = 30

# initialize pygame and create window
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | HWSURFACE, 32)
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

running = True
while running:
    # keep loop running at the right speed
    delta = clock.tick(FPS) / 1000

    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False

    # Update
    pg.display.set_caption(TITLE + " | {:.2f}".format(clock.get_fps()))

    # Draw / Render

    # *after*  drawing everything , flip the display last
    pg.display.flip()

quit()
