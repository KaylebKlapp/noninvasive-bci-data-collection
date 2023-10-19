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

def determine_keysize_and_offset():
    # Find the width and height of the screen the program is run on
    width, height = pg.display.get_surface().get_size()

    # Find the max number of keys in a single row of the defined keyboard
    max_columns = 0
    for row in keyboard:
        if(row.__len__() > max_columns):
            max_columns = row.__len__()

    # Find the number of rows in the defined keyboard
    num_rows = keyboard.__len__()

    # Determine the size of the keys (want them to be squared) by determining
    # whether the height or width of the screen is the limiting factor
    key_size = width/max_columns
    if( (key_size * num_rows) > height ):
        key_size = height/max_columns
        
    # Center the keyboard by finding the distance leftover on the top and bottom
    # of the screen
    wid = key_size * max_columns - (2 * key_size * (1-key_buffer))
    hei = key_size * num_rows - (2 * key_size * (1-key_buffer))
    x_offset = (width-wid)/2
    y_offset = (height-hei)/2

    return x_offset, y_offset, max_columns, key_size

def determine_row_stagger_size(row, max_columns, key_size):
    # Determine the number of keys in the row currently being iterated through
    num_keys = row.__len__()

    # Stagger the keys similar to how a QWERTY keyboard is staggered
    if(num_keys == max_columns ):
        row_offset = 0
    else:
        row_offset = (max_columns-num_keys)*(key_size/2)

    return row_offset

def initialize_screen():
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    screen.fill((205, 205, 205))
    return screen

def draw_keys(screen, first, x_offset, row_offset, y_offset, keySize, font_keyboard, key):
    # If it's the first key, apply the stagger. Draw the keys here
    if(first):
        x_offset += row_offset
        pg.draw.rect(screen,key_color,pg.Rect(x_offset, y_offset, keySize, keySize))
        first = False
    else:
        pg.draw.rect(screen,key_color,pg.Rect(x_offset, y_offset, keySize, keySize))

    # Draws the letter on the key based on the keyboard defined above
    screen.blit(font_keyboard.render(key, True, font_color), (x_offset,y_offset))

    return x_offset, first






def init_keyboard():
    # Initialize the screen
    screen = initialize_screen()

    # Determine the key size and offset to center the keyboard
    x_offset, y_offset, max_columns, key_size = determine_keysize_and_offset()

    # Go through each row in the keyboard, print each key based on the height and 
    # width of the key determined above
    for row in keyboard:

        # Determine the distance the row is staggered
        row_offset = determine_row_stagger_size(row, max_columns, key_size)

        # Boolean variable to track whether to add the stagger or not
        first = True

        # Add a buffer between keys to look more natural
        keySize = key_size*key_buffer

        # Change the font size to match that of the keys it will sit on
        font_keyboard = pg.font.SysFont("Alata", int(keySize))

        # Go through each key in the row
        for key in row:

            # Draw the keys and letters for the keyboard
            x_offset, first = draw_keys(screen, first, x_offset, row_offset, y_offset, keySize, font_keyboard, key)

            # Iterate the x_offset based on the size of the keys
            x_offset += key_size

        # Reset the x_offset so it prints at the beginning of the screen again
        x_offset = 0

        # Add the key_size to the y_offset to print the next row
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
