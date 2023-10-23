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
flash_color = (255,0,0)
flash_num = 5
flash_delay = 0.25
key_buffer = 0.95

training_key_percentage = 0.75

#keyboard = [
 #           ['Q','W','E','R','T','Y','U','I','O','P'],
  #          ['A','S','D','F','G','H','J','K','L'],
   #         ['Z','X','C','V','B','N','M']
#]

# [character, size, coordinate, visibility, flash]
keyboard = [
            [['Q',0,tuple,True,False],['W',0,tuple,True,False],['E',0,tuple,True,False],['R',0,tuple,True,False],['T',0,tuple,True,False],['Y',0,tuple,True,False],['U',0,tuple,True,False],['I',0,tuple,True,False],['O',0,tuple,True,False],['P',0,tuple,True,False]],
            [['A',0,tuple,True,False],['S',0,tuple,True,False],['D',0,tuple,True,False],['F',0,tuple,True,False],['G',0,tuple,True,False],['H',0,tuple,True,False],['J',0,tuple,True,False],['K',0,tuple,True,False],['L',0,tuple,True,False]],
            [['Z',0,tuple,True,False],['X',0,tuple,True,False],['C',0,tuple,True,False],['V',0,tuple,True,False],['B',0,tuple,True,False],['N',0,tuple,True,False],['M',0,tuple,True,False]]
]

training_letters = ['K', 'W', 'E']
training_keys = [pg.key.key_code(letter) for letter in training_letters]

alphabet = [chr(i) for i in range(ord("A"), ord("Z"))]
nontraining_letters = alphabet

for let in training_letters:
    nontraining_letters.remove(let)
    
def get_random_letter_key_pair():
    if (random.random() <= training_key_percentage):
        rand_index = random.randint(0,2)
    else:
        return nontraining_letters[random.randrange(0, len(nontraining_letters))], None
    return (training_letters[rand_index], training_keys[rand_index])

#keyboard = [[['a',tuple,True]],[['b',tuple,True]]]
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

def draw_keys(screen, key):
    # Change the font size to match that of the keys it will sit on
    font_keyboard = pg.font.SysFont("Alata", int(key[1]))
    if(key[3]):
        if(key[4]):
            original = True
            for i in range(flash_num*2):
                if(original):
                    # Draw the keys
                    pg.draw.rect(screen,key_color,pg.Rect(key[2][0], key[2][1], key[1], key[1]))
                    screen.blit(font_keyboard.render(key[0], True, font_color), (key[2][0],key[2][1]))
                    pg.display.flip()
                    time.sleep(flash_delay)
                    original = False
                else:
                    # Draw the keys
                    pg.draw.rect(screen,flash_color,pg.Rect(key[2][0], key[2][1], key[1], key[1]))
                    screen.blit(font_keyboard.render(key[0], True, font_color), (key[2][0],key[2][1]))
                    pg.display.flip()
                    time.sleep(flash_delay)
                    original = True
        else:
            # Draw the keys
            pg.draw.rect(screen,key_color,pg.Rect(key[2][0], key[2][1], key[1], key[1]))
            screen.blit(font_keyboard.render(key[0], True, font_color), (key[2][0],key[2][1]))





def init_keyboard(char, method, flash):

    # Determine the key size and offset to center the keyboard
    x_offset, y_offset, max_columns, key_size = determine_keysize_and_offset()
    keySize = key_size*key_buffer

    # Go through each row in the keyboard, print each key based on the height and 
    # width of the key determined above
    for row in range(keyboard.__len__()):
        # Determine the distance the row is staggered
        row_offset = determine_row_stagger_size(keyboard[row], max_columns, key_size)

        # Boolean variable to track whether to add the stagger or not
        first = True

        # Add a buffer between keys to look more natural

        # Go through each key in the row
        for key in range(keyboard[row].__len__()):

            # Draw the keys and letters for the keyboard
            if(first):
                x_offset += row_offset
                first = False

            #draw_keys(screen,key)

            keyboard[row][key][1] = keySize
            keyboard[row][key][2] = (x_offset, y_offset)
            if(method == 3):
                if(keyboard[row][key][0] == char):
                    keyboard[row][key][3] = True
                else:
                    keyboard[row][key][3] = False

            else:
                keyboard[row][key][3] = True

            if(keyboard[row][key][0] == char):
                keyboard[row][key][4] = True

            # Iterate the x_offset based on the size of the keys
            x_offset += key_size

        # Reset the x_offset so it prints at the beginning of the screen again
        x_offset = 0

        # Add the key_size to the y_offset to print the next row
        y_offset += key_size
        






def start_window():

    # Initialize the screen
    pg.display.set_caption("BCI training")
    screen = initialize_screen()

    # CONSIDER MOVING DRAW_KEYS BACK INTO INIT KEYBOARD FOR SIMPLICITY IN FLASHING CHARACTERS

    running = True
    while running:
        character, character_key = get_random_letter_key_pair()

        method = random.random()
        print(method)
        # flash red key
        if( method <= 0.33 ):
            init_keyboard(character,1,True)
            for row in keyboard:
                for key in row:
                    draw_keys(screen, key)

        # enlarge key
        elif( method <= 0.66 ):
            init_keyboard(character,2,False)
            for row in keyboard:
                for key in row:
                    draw_keys(screen, key)
        
        # make keyboard disappear and flash one letter
        else:
            # Draw the initial keyboard
            init_keyboard(character,100,False)
            for row in keyboard:
                for key in row:
                    draw_keys(screen, key)

            pg.display.flip()
            time.sleep(1)

            # Clear the screen and display the character
            screen.fill((205,205,205))
            pg.display.flip()
            time.sleep(0.5)
            init_keyboard(character,3,True)
            for row in keyboard:
                for key in row:
                    draw_keys(screen, key)

        pg.display.flip()

        time.sleep(3)
        screen.fill((205, 205, 205))
        pg.display.flip()
        time.sleep(1)

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

    

    #letter_index = 0
    #running = True
    #while running:
     #   for event in pg.event.get():
      #      if event.type == pg.QUIT:
       #         running = False
        #        break
         #   elif event.type == pg.KEYDOWN:
          #      if event.key == keys[letter_index]:
           #         time_keys.append([letters[letter_index], int(time.time() * 1000)])
            #        letter_index += 1
             #       letter_index %= len(letters)
#
 #               elif event.key == pg.K_ESCAPE:
  #                  running = False

try:
    start_window()
except Exception as e:
    print(e.__str__())
    print("An error occurred. Please double check the file.")
#finally:
    #with open("test.csv", "w") as fp:
     #   for input in time_keys:
      #      fp.write(f"{input[0]},{input[1]}\n")
