import pygame as pg
import numpy as np  
from datetime import datetime
import time
import argparse
import random
from math import floor
import time

# Admin Stuff for pygame
pg.init()
pg.font.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
ARROW_WIDTH = 270
ARROW_HEIGHT = 175

#Frequencies of arrows, in Hz
freq_up = 10
freq_down = 13
freq_right = 17
freq_left = 21

up, down, left, right = False, False, False, True

screen_width, screen_height = SCREEN_WIDTH, SCREEN_HEIGHT
height_markers = [(screen_width / 4) * i for i in range(1,4)]
width_markers = [(screen_height / 4) * i for i in range(1,4)]

def process_img(color, size_x=ARROW_WIDTH, size_y=ARROW_HEIGHT):
    img = pg.image.load(f"arrow_{color}.png")
    img = pg.transform.scale(img, (size_x, size_y))
    return img

images = dict()
for file_name in ["black", "red", "green"]:
    images[file_name] = process_img(file_name)

def draw_arrow(screen, color, x, y, rotation):
    img = images[color]
    img = pg.transform.rotate(img, rotation)
    screen.blit(img, (x, y))

# Main pygame loop
def start_window():
    """
    Beginning loop admin
    """
    # Setting this to false gives a brief pause on starting the program
    showing_character = False
    pg.display.set_caption("BCI training")
    screen = pg.display.set_mode((screen_width, screen_height))
    
    running = True
    while running:

        # Events manager
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running=False
                    break

        # redraw screen
        screen.fill((155, 155, 155))

        # All drawing logic goes under this line

        tick = time.time()

        color_up = "black" if floor(tick * freq_up) % 2 == 1 else "green"
        color_right = "black" if floor(tick * freq_right) % 2 == 1 else "green"
        color_down = "black" if floor(tick * freq_down) % 2 == 1 else "green"
        color_left = "black" if floor(tick * freq_left) % 2 == 1 else "green"

        # Up arrow
        if (up):
            draw_arrow(screen, color_up, floor(SCREEN_WIDTH/2 - ARROW_HEIGHT/2), 50, 90)

        # # Down arrow
        if(down):
            draw_arrow(screen, color_down, floor(SCREEN_WIDTH/2 - ARROW_HEIGHT/2), SCREEN_HEIGHT - ARROW_WIDTH - 50, 270)

        # # left Arrow
        if(left):
            draw_arrow(screen, color_left, 50, floor(SCREEN_HEIGHT*0.5 - 0.5*ARROW_HEIGHT), 180)

        # # Right Arrow
        if (right):
            draw_arrow(screen, color_right, SCREEN_WIDTH - ARROW_WIDTH - 50 , floor(SCREEN_HEIGHT*0.5 - 0.5*ARROW_HEIGHT), 0)

        pg.display.flip()

start_window()
