import time
from datetime import datetime
import brainflow as bf
import numpy as np
import pygame as pg
import random
import tkinter as tk 


pg.init()
pg.font.init()
RED = (255,0,0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)

time_keys = []
letters = ['K', 'W', 'E']
alphabet22 = [chr(i) for i in range(ord("A"), ord("Z"))]
keys = [pg.K_k, pg.K_w, pg.K_e]
font_color = (255,255,255)
key_color = (0,0,0)
key_buffer = 0.95
date_string = datetime.now().strftime("%y_%m_%d_%H_%M_%S")
collection_type = "checkerboard"
subject_name = "aris"
more_info = ""


class create_keyboard(object):

    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    timeshowchar = 0
    randomcharchoice1 = ''
    keyboard = [[] for i in range(5)]

    def flash_color(self, letter):
        flash_COLOR = RED   
        flash_time = 0.2
        font_keyboard = pg.font.SysFont("Alata", 60)
        self.screen.fill((205, 205, 205))  # Clear the screen
        pg.draw.rect(self.screen, key_color, pg.Rect(100, 100, 60, 60))  # Draw a key
        self.screen.blit(font_keyboard.render(letter, True, flash_COLOR), (50, 50))  # Flash the letter
        pg.display.flip()  # Update the display
        time.sleep(flash_time)  # Wait for the flash to disappear
    
    def randomize_board(self): 
        keyboard = [[] for i in range(5)]
        alphabet = [chr(i) for i in range(ord("A"), ord("Z"))]
        for index, key_row in enumerate(self.keyboard):
            key_row = random.sample(alphabet,5)
            self.keyboard[index] = key_row
            for letter in key_row:
                alphabet.remove(letter)
        chance1 = random.randint(1,10)
        if(chance1<=7):
            REDLETTER1 = random.choice(letters)
            self.randomcharchoice1 = REDLETTER1
        else:
            REDLETTER1 = random.choice(alphabet22)
            self.randomcharchoice1 = REDLETTER1


    def draw_board(self, color_for_diff_letter = RED, color_for_diff_box = (255, 255, 255)):
        ##print(self.randomcharchoice1)
        ##screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
        self.screen.fill((205, 205, 205))

        width, height = pg.display.get_surface().get_size()
        max = 0
        for row in self.keyboard:
            if(row.__len__() > max):
                max = row.__len__()

        num_rows = len(self.keyboard)
        key_size = width
        if( (key_size * num_rows) > height ):
            key_size = height/max

        x_offset = height*0.005
        y_offset = (height-(key_size*num_rows))/2

        for row in self.keyboard:
            num_keys = row.__len__()
            if(num_keys == max ):
                row_offset = 0
            else:
                row_offset = (max-num_keys)*(key_size/2)
            
            first = True
            keySize = key_size*key_buffer
            font_keyboard = pg.font.SysFont("Alata", int(keySize))
            for key in row:

                if(first):
                    x_offset += row_offset
                    pg.draw.rect(self.screen, key_color, pg.Rect(x_offset, y_offset, keySize, keySize))
                    if(key==self.randomcharchoice1):
                        pg.draw.rect(self.screen, color_for_diff_box, pg.Rect(x_offset, y_offset, keySize, keySize))
                    first = False
                else:
                    pg.draw.rect(self.screen, key_color,pg.Rect(x_offset, y_offset, keySize, keySize))
                    if(key==self.randomcharchoice1):
                        pg.draw.rect(self.screen, color_for_diff_box, pg.Rect(x_offset, y_offset, keySize, keySize))

                if(key==self.randomcharchoice1):
                    self.screen.blit(font_keyboard.render(key, True, color_for_diff_letter), (x_offset,y_offset))
                else:
                    pg.draw.rect(self.screen,key_color,pg.Rect(x_offset, y_offset, keySize, keySize))
                    if(key==self.randomcharchoice1):
                        pg.draw.rect(self.screen,color_for_diff_box,pg.Rect(x_offset, y_offset, keySize, keySize))
                        self.square_locationx, self.square_locationy = (x_offset,y_offset)
                        self.keysizeclass = keySize

                if(key==self.randomcharchoice1):
                    self.screen.blit(font_keyboard.render(key, True, color_for_diff_letter), (x_offset,y_offset))
                else:
                    self.screen.blit(font_keyboard.render(key, True, font_color), (x_offset,y_offset))

                ##random_letter = random.choice(letters)
                x_offset += key_size

            x_offset = 0
            y_offset += key_size


        color_dark = (100,100,100) 
        button = pg.Rect(width/2+200, height/2, 200, 100) 
        pg.draw.rect(self.screen, [100, 100, 100], button)  # draw button
        font_keyboard2 = pg.font.SysFont("Alata", 40)
        ##random_letter = random.choice(letters)
        self.screen.blit(font_keyboard2.render('START TEST', True, font_color), (width/2+225, height/2))
        self.timeshowchar = time.time()*1000

    def __init__(self):
        self.randomize_board()
        self.draw_board()

def start_window():
    pg.display.set_caption("BCI training")
    keyboard = create_keyboard()
    keyboard.__init__()
    ##random_letter = random.choice(letters)
    letter_index = 0
    running = True 
    keyboard.randomize_board()
    keyboard.draw_board()
    number_since_shuffle = 0
    SHUFFLE_FREQUENCY = 3
    DELAY_BETWEEN_CHARS_MS = 700
    show_next_char_time = time.time()*1000 + DELAY_BETWEEN_CHARS_MS

    while running:

        if (keyboard.randomcharchoice1 == '' and time.time() * 1000 > show_next_char_time):
            keyboard.randomcharchoice1 = random.sample(letters, 1)[0]

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            elif event.type == pg.KEYDOWN:
                keycodetest = pg.key.key_code(keyboard.randomcharchoice1)
                if event.key == keycodetest:
                    time_keys.append([keyboard.randomcharchoice1, keyboard.timeshowchar])
                    keyboard.randomcharchoice1 = ''
                    show_next_char_time = (time.time()*1000) + DELAY_BETWEEN_CHARS_MS

                    number_since_shuffle += 1
                    if SHUFFLE_FREQUENCY == number_since_shuffle:
                        number_since_shuffle = 0
                        keyboard.randomize_board()

                if event.key == pg.K_ESCAPE:
                    running = False

        if (int(time.time() * 4) % 2 == 0):
            keyboard.draw_board(color_for_diff_box=BLACK, color_for_diff_letter=WHITE)
        else:
            keyboard.draw_board(color_for_diff_box=RED, color_for_diff_letter=BLACK)
        


        pg.display.flip()

time_end_training = 0
time_start_training = int(time.time() * 1000)

try:
    start_window()
    time_end_training = int(time.time() * 1000)
except Exception as e:
    print(e.__str__())
    print("An error occurred. Please double check the file.")
    time_end_training = int(time.time() * 1000)
finally:
    file_name = f"{date_string}_{subject_name}_{collection_type}_{more_info}_{time_end_training}_{time_start_training}.stim"
    with open(file_name, "w") as fp:
        for input in time_keys:
            fp.write(f"{input[0]},{input[1]}\n")
