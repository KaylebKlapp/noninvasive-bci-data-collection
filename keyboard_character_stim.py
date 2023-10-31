# Keyboard stimulus

import pygame as pg
import random
from datetime import datetime
import time

date_string = datetime.now().strftime("%y_%m_%d_%H_%M_%S")
collection_type = "keyboard_stim"
subject_name = "jayden"
more_info = ""

pg.init()
pg.font.init()

TIME_KEYS = []
LETTERS = ['K', 'W', 'E']
KEYS = [pg.K_k, pg.K_w, pg.K_e]
FONT_COLOR = (255,255,255)
KEY_COLOR = (0,0,0)
FLASH_COLOR = (255,0,0)
FLASH_NUM = 5
FLASH_DELAY = 250
KEY_BUFFER = 0.95
KEYBOARD_FONT = "Alata"
FLASH = True
SHOW_TIME = time.time() * 1000
SHUFFLE_FREQUENCY = 3
DELAY_BETWEEN_CHARS_MS = 700

TRAINING_KEY_PERCENTAGE = 0.75

#keyboard = [
 #           ['Q','W','E','R','T','Y','U','I','O','P'],
  #          ['A','S','D','F','G','H','J','K','L'],
   #         ['Z','X','C','V','B','N','M']
#]

# [character, size, coordinate]
keyboard = [
            [['Q',0,tuple],['W',0,tuple],['E',0,tuple],['R',0,tuple],['T',0,tuple],['Y',0,tuple],['U',0,tuple],['I',0,tuple],['O',0,tuple],['P',0,tuple]],
            [['A',0,tuple],['S',0,tuple],['D',0,tuple],['F',0,tuple],['G',0,tuple],['H',0,tuple],['J',0,tuple],['K',0,tuple],['L',0,tuple]],
            [['Z',0,tuple],['X',0,tuple],['C',0,tuple],['V',0,tuple],['B',0,tuple],['N',0,tuple],['M',0,tuple]]
]

training_letters = ['K', 'W', 'E']
training_keys = [pg.key.key_code(letter) for letter in training_letters]

alphabet = [chr(i) for i in range(ord("A"), ord("Z"))]
nontraining_letters = alphabet

for let in training_letters:
    nontraining_letters.remove(let)

def get_random_letter_key_pair():
    if (random.random() <= TRAINING_KEY_PERCENTAGE):
        rand_index = random.randint(0,2)
    else:
        return nontraining_letters[random.randrange(0, len(nontraining_letters))], None
    return (training_letters[rand_index], training_keys[rand_index])

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
    wid = key_size * max_columns - (2 * key_size * (1-KEY_BUFFER))
    hei = key_size * num_rows - (2 * key_size * (1-KEY_BUFFER))
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

def draw_keys(screen, key, x_offset, y_offset, size, draw, font_keyboard):
    # Change the font size to match that of the keys it will sit on
    if(draw):
        # Draw the keys
        pg.draw.rect(screen,KEY_COLOR,pg.Rect(x_offset, y_offset, size, size))
        screen.blit(font_keyboard.render(key[0], True, FONT_COLOR), (x_offset,y_offset))

def flash_keys(original, screen, key, x_offset, y_offset, size, font_keyboard):
    for i in range(FLASH_NUM*2):
        if(original):
            # Draw the keys
            pg.draw.rect(screen,KEY_COLOR,pg.Rect(x_offset, y_offset, size, size))
            screen.blit(font_keyboard.render(key[0], True, FONT_COLOR), (x_offset,y_offset))
            pg.display.flip()
            pg.time.wait(FLASH_DELAY)
            original = False
        else:
            # Draw the keys
            pg.draw.rect(screen,FLASH_COLOR,pg.Rect(x_offset, y_offset, size, size))
            screen.blit(font_keyboard.render(key[0], True, FONT_COLOR), (x_offset,y_offset))
            pg.display.flip()
            pg.time.wait(FLASH_DELAY)
            original = True

def perform_method(method, char_row_and_col, flash, screen, font_keyboard):
    charRow = char_row_and_col[0]
    charCol = char_row_and_col[1]
    x_offsetChar = keyboard[charRow][charCol][2][0]
    y_offsetChar = keyboard[charRow][charCol][2][1]
    char = keyboard[charRow][charCol][0]
    size = keyboard[charRow][charCol][1]
    if( method == 1 ):
        if(flash):
            if (int(time.time() * 4) % 2 == 0):
                # Draw the keys
                pg.draw.rect(screen,KEY_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
                screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))
                pg.display.flip()
                pg.time.wait(FLASH_DELAY)
                    
            else:
                # Draw the keys
                pg.draw.rect(screen,FLASH_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
                screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))
                pg.display.flip()
                pg.time.wait(FLASH_DELAY)
        else:
            pg.draw.rect(screen,FLASH_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
            screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))
            pg.display.flip()
            pg.time.wait(FLASH_DELAY)

    elif( method == 2 ):
        pg.time.wait(1000)
        size = keyboard[charRow][charCol][1] * 2
        font_keyboard = pg.font.SysFont(KEYBOARD_FONT, int(size*2))
        if(flash):
            if (int(time.time() * 4) % 2 == 0):
                # Draw the keys
                pg.draw.rect(screen,KEY_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
                screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))
                pg.display.flip()
                pg.time.wait(FLASH_DELAY)
                    
            else:
                # Draw the keys
                pg.draw.rect(screen,FLASH_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
                screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))
                pg.display.flip()
                pg.time.wait(FLASH_DELAY)
        else:
            pg.draw.rect(screen,FLASH_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
            screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))
            pg.display.flip()
            pg.time.wait(FLASH_DELAY)

    elif( method == 3 ):
        pg.time.wait(1000)
        screen.fill((205,205,205))
        #pg.display.flip()
        #pg.time.wait(500)
        
        if(flash):
            if (int(time.time() * 4) % 2 == 0):
                # Draw the keys
                pg.draw.rect(screen,KEY_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
                screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))
                pg.display.flip()
                pg.time.wait(FLASH_DELAY)
                    
            else:
                # Draw the keys
                pg.draw.rect(screen,FLASH_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
                screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))
                pg.display.flip()
                pg.time.wait(FLASH_DELAY)
        else:
            pg.draw.rect(screen,FLASH_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
            screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))
            pg.display.flip()
            pg.time.wait(FLASH_DELAY)

        draw_keys(screen,keyboard[charRow][charCol],x_offsetChar,y_offsetChar,size,True)

    pg.display.flip()





def init_keyboard(char, screen):
    char_row_and_col = (0,0)

    # Determine the key size and offset to center the keyboard
    x_offset, y_offset, max_columns, key_size = determine_keysize_and_offset()
    
    # Add a buffer between keys to look more natural
    keySize = key_size*KEY_BUFFER

    # Define the font for the keyboard
    font_keyboard = pg.font.SysFont(KEYBOARD_FONT, int(keySize))

    # Go through each row in the keyboard, print each key based on the height and 
    # width of the key determined above
    for row in range(keyboard.__len__()):
        # Determine the distance the row is staggered
        row_offset = determine_row_stagger_size(keyboard[row], max_columns, key_size)

        # Boolean variable to track whether to add the stagger or not
        first = True

        # Go through each key in the row
        for key in range(keyboard[row].__len__()):

            # Draw the keys and letters for the keyboard
            if(first):
                x_offset += row_offset
                first = False

            keyboard[row][key][1] = keySize
            keyboard[row][key][2] = (x_offset, y_offset)

            if( keyboard[row][key][0] == char ):
                char_row_and_col = (row, key)

            draw_keys(screen,keyboard[row][key],x_offset,y_offset,keySize,True,font_keyboard)

            # Iterate the x_offset based on the size of the keys
            x_offset += key_size

        # Reset the x_offset so it prints at the beginning of the screen again
        x_offset = 0

        # Add the key_size to the y_offset to print the next row
        y_offset += key_size
    
    pg.display.flip()

    return char_row_and_col, font_keyboard

    

       
def start_window():

    # Initialize the screen
    pg.display.set_caption("BCI training")
    screen = initialize_screen()

    character, character_key = get_random_letter_key_pair()
    method = random.random()
    char_row_and_col, font_keyboard = init_keyboard(character,screen)

    show_next_char_time = time.time()*1000 + DELAY_BETWEEN_CHARS_MS
    running = True
    while running:
        if (time.time()*1000 > show_next_char_time):
            character, character_key = get_random_letter_key_pair()
            method = random.random()
            show_next_char_time = time.time()*1000 + DELAY_BETWEEN_CHARS_MS

        print(method)

        pg.time.wait(3000)
        screen.fill((205, 205, 205))
        pg.display.flip()
        pg.time.wait(1000)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                    break
                #if event.key == pg.K_BACKSPACE:
                #    del time_keys[-1]
                if character in training_letters and event.key == character_key:
                    TIME_KEYS.append([character, SHOW_TIME]) # fix show_time

        perform_method(method, char_row_and_col, FLASH, screen, font_keyboard)

    #print(time_keys)



time_end_training = 0
time_start_training = int(time.time() * 1000)

try:
    start_window()
    time_end_training = int(time.time() * 1000)
except Exception as e:
    print(e.__str__())
    print("An error occurred. Please double check the file.")
#finally:
 #   file_name = f"{date_string}_{subject_name}_{collection_type}_{more_info}_{time_end_training}_{time_start_training}.txt"
  #  with open(file_name, "w") as fp:
   #     for input in time_keys:
    #        fp.write(f"{input[0]},{input[1]}\n")
