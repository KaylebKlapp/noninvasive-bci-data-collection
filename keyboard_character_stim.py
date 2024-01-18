# Keyboard stimulus

import pygame as pg
import random
import time

pg.init()

# Change based on the type of keyboard you want
from keyboard_and_program_style_1 import *

pg.font.init()

def get_random_letter_key_pair():
    if (random.random() <= TRAINING_KEY_PERCENTAGE):
        rand_index = random.randint(0,len(KEYS)-1)
    else:
        return nontraining_letters[random.randrange(0, len(nontraining_letters))], None
    return (LETTERS[rand_index], KEYS[rand_index])

def determine_keysize_and_offset():
    global keyboard
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
    key_size = width/(max_columns+2)
    if( (key_size * (num_rows+2)) > height ):
        key_size = height/(max_columns+2)
        
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
    screen.fill(SCREEN_BACKGROUND)
    return screen

def draw_keyboard(screen, font_keyboard):
    global keyboard
    # Change the font size to match that of the keys it will sit on
    screen.fill(SCREEN_BACKGROUND)
    for row in range(keyboard.__len__()):
        for col in range(keyboard[row].__len__()):
            char = keyboard[row][col][0]
            x_offset = keyboard[row][col][2][0]
            y_offset = keyboard[row][col][2][1]
            size = keyboard[row][col][1]
            # Draw the keys
            pg.draw.rect(screen,KEY_COLOR,pg.Rect(x_offset, y_offset, size, size))
            screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offset, y_offset))

def draw_key(screen, key, x_offset, y_offset, size, draw, font_keyboard):
    if(draw):
        # Draw the keys
        pg.draw.rect(screen,KEY_COLOR,pg.Rect(x_offset, y_offset, size, size))
        screen.blit(font_keyboard.render(key[0], True, FONT_COLOR), (x_offset,y_offset))

def perform_method(method, char_row_and_col, screen, font_keyboard):
    global keyboard
    charRow = char_row_and_col[0]
    charCol = char_row_and_col[1]
    x_offsetChar = keyboard[charRow][charCol][2][0]
    y_offsetChar = keyboard[charRow][charCol][2][1]
    char = keyboard[charRow][charCol][0]
    size = keyboard[charRow][charCol][1]
    if( method == 1 ):
        if(FLASH):
            if (int(time.time() * 4) % 2 == 0):
                # Draw the keys
                pg.draw.rect(screen,KEY_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
                screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))
                    
            else:
                # Draw the keys
                pg.draw.rect(screen,FLASH_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
                screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))
        else:
            pg.draw.rect(screen,FLASH_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
            screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))

    elif( method == 2 ):
        size = keyboard[charRow][charCol][1] * ENLARGE_KEY_SIZE
        font_keyboard = pg.font.SysFont(KEYBOARD_FONT, int(size*ENLARGE_LETTER_SIZE))
        if(FLASH):
            if (int(time.time() * 4) % 2 == 0):
                # Draw the keys
                pg.draw.rect(screen,FLASH_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
                screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))
                    
            else:
                # Draw the keys
                pg.draw.rect(screen,KEY_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
                screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))
        else:
            pg.draw.rect(screen,FLASH_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
            screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))

    elif( method == 3 ):
        screen.fill(SCREEN_BACKGROUND)
        if(FLASH):
            if (int(time.time() * 4) % 2 == 0):
                # Draw the keys
                pg.draw.rect(screen,FLASH_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
                screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))
                    
            else:
                # Draw the keys
                pg.draw.rect(screen,KEY_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
                screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))
        else:
            pg.draw.rect(screen,FLASH_COLOR,pg.Rect(x_offsetChar, y_offsetChar, size, size))
            screen.blit(font_keyboard.render(char, True, FONT_COLOR), (x_offsetChar,y_offsetChar))

    pg.display.flip()





def init_keyboard(char, screen):
    global keyboard
    screen.fill(SCREEN_BACKGROUND)
    char_row_and_col = (0,0)

    # Determine the key size and offset to center the keyboard
    x_offset, y_offset, max_columns, key_size = determine_keysize_and_offset()
    temp_x_offset = x_offset
    
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

            draw_key(screen,keyboard[row][key],x_offset,y_offset,keySize,True,font_keyboard)

            # Iterate the x_offset based on the size of the keys
            x_offset += key_size

        # Reset the x_offset so it prints at the beginning of the screen again
        x_offset = temp_x_offset

        # Add the key_size to the y_offset to print the next row
        y_offset += key_size
    
    pg.display.flip()

    return char_row_and_col, font_keyboard

    

       
def start_window():

    # Initialize the screen
    pg.display.set_caption("BCI training")
    screen = initialize_screen()

    time_until_next_stim = random.randint(TIME_UNTIL_NEXT_STIM_CONST_RANGE[0],TIME_UNTIL_NEXT_STIM_CONST_RANGE[1])
    delay_between_chars_ms = random.randint(TIME_BETWEEN_CHARS_CONST_RANGE[0],TIME_BETWEEN_CHARS_CONST_RANGE[1])
    character, character_key = get_random_letter_key_pair()
    if(RANDOM_METHOD or METHOD not in range(1,4)):
        method = random.randint(1,3)
    else:
        method = METHOD
    new_keyboard = random.randint(NEW_KEYBOARD_FREQUENCY_RANGE[0], NEW_KEYBOARD_FREQUENCY_RANGE[1])
    iteration = 0
    if( RANDOM_KEYBOARD_KEYS ):
        randomize_board_keys()
    char_row_and_col, font_keyboard = init_keyboard(character,screen)
    pg.time.wait(time_until_next_stim)
    show_next_char_time = time.time()*1000 + delay_between_chars_ms
    show_time = time.time()
    print(method, character, char_row_and_col)

    running = True
    while running:
        if (time.time()*1000 > show_next_char_time):
            iteration += 1
            time_until_next_stim = random.randint(TIME_UNTIL_NEXT_STIM_CONST_RANGE[0],TIME_UNTIL_NEXT_STIM_CONST_RANGE[1])
            delay_between_chars_ms = random.randint(TIME_BETWEEN_CHARS_CONST_RANGE[0],TIME_BETWEEN_CHARS_CONST_RANGE[1])
            character, character_key = get_random_letter_key_pair()
            if(RANDOM_METHOD or METHOD not in range(1,4)):
                method = random.randint(1,3)
            else:
                method = METHOD
            if( iteration >= new_keyboard and RANDOM_KEYBOARD_KEYS):
                iteration = 0
                new_keyboard = random.randint(NEW_KEYBOARD_FREQUENCY_RANGE[0], NEW_KEYBOARD_FREQUENCY_RANGE[1])
                randomize_board_keys()
            char_row_and_col, font_keyboard = init_keyboard(character,screen)
            pg.time.wait(time_until_next_stim)
            show_next_char_time = time.time()*1000 + delay_between_chars_ms
            show_time = time.time()
            if not character in LETTERS:
                time_keys.append([character, show_time])
            print(method, character, char_row_and_col)

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                    break
                if event.key == pg.K_BACKSPACE:
                    del time_keys[-1]
                elif event.key == character_key: # and character in LETTERS:
                    time_keys.append([character, show_time])

        perform_method(method, char_row_and_col, screen, font_keyboard)

    print(time_keys)



time_end_training = 0
time_start_training = int(time.time() * 1000)

with open("collect_key.txt", "r") as fp:
    collect_key = int(fp.readline())

try:
    start_window()
    time_end_training = int(time.time() * 1000)
except Exception as e:
    print(e.__str__())
    print("An error occurred. Please double check the file.")
finally:
    file_name = f"{collect_key}_{date_string}_{subject_name}_{collection_type}_{more_info}_{time_end_training}_{time_start_training}.txt"
    with open(file_name, "w") as fp:
        for input in time_keys:
            fp.write(f"{input[0]},{input[1]}\n")
