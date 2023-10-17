import time
from datetime import datetime
import brainflow as bf
import numpy as np
import pygame as pg
import random

pg.init()
pg.font.init()

time_keys = []
letters = ['K', 'W', 'E']
keys = [pg.K_k, pg.K_w, pg.K_e]
font_color = (255,255,255)
key_color = (0,0,0)
key_buffer = 0.95

keyboard = [
            ['Q','W','E','R','T','Y','U','I','O','P'],
            ['A','S','D','F','G','H','J','K','L'],
            ['Z','X','C','V','B','N','M']
]

def init_keyboard():
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    screen.fill((205, 205, 205))

    #x_offset, y_offset, key_size = center_keyboard()
    width, height = pg.display.get_surface().get_size()
    max_columns = 0
    for row in keyboard:
        if(row.__len__() > max_columns):
            max_columns = row.__len__()

    num_rows = keyboard.__len__()
    key_size = width/max_columns
    if( (key_size * num_rows) > height ):
        key_size = height/max_columns
        
    wid = key_size * max_columns - (2 * key_size * (1-key_buffer))
    hei = key_size * num_rows - (2 * key_size * (1-key_buffer))

    x_offset = (width-wid)/2
    y_offset = (height-hei)/2

    for row in keyboard:
        num_keys = row.__len__()
        if(num_keys == max_columns ):
            row_offset = 0
        else:
            row_offset = (max_columns-num_keys)*(key_size/2)
        
        first = True
        keySize = key_size*key_buffer
        font_keyboard = pg.font.SysFont("Alata", int(keySize))
        for key in row:
            if(first):
                x_offset += row_offset
                pg.draw.rect(screen,key_color,pg.Rect(x_offset, y_offset, keySize, keySize))
                first = False
            else:
                pg.draw.rect(screen,key_color,pg.Rect(x_offset, y_offset, keySize, keySize))

            screen.blit(font_keyboard.render(key, True, font_color), (x_offset,y_offset))

            x_offset += key_size

        x_offset = 0
        y_offset += key_size

        

def start_window():
    pg.display.set_caption("BCI training")
    init_keyboard()

    method = random.random()

    pg.display.flip()

    if( method <= 0.33 ):
        # flash red key
        pass
    elif( method <= 0.66 ):
        # enlarge key
        pass
    else:
        # make keyboard disappear and flash one letter
        pass

    letter_index = 0
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            elif event.type == pg.KEYDOWN:
                if event.key == keys[letter_index]:
                    time_keys.append([letters[letter_index], int(time.time() * 1000)])
                    letter_index += 1
                    letter_index %= len(letters)

                elif event.key == pg.K_ESCAPE:
                    running = False 

try:
    start_window()
except Exception as e:
    print(e.__str__())
    print("An error occurred. Please double check the file.")
finally:
    with open("test.csv", "w") as fp:
        for input in time_keys:
            fp.write(f"{input[0]},{input[1]}\n")
