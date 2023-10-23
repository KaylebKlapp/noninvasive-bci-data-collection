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

time_keys = []
letters = ['K', 'W', 'E']
keys = [pg.K_k, pg.K_w, pg.K_e]
font_color = (255,255,255)
key_color = (0,0,0)
key_buffer = 0.95

#keyboard = [
 #           [pg.K_q,pg.K_w,pg.K_e,pg.K_r,pg.K_t,pg.K_y,pg.K_u,pg.K_i,pg.K_o,pg.K_p],
  #          [pg.K_a,pg.K_s,pg.K_d,pg.K_f,pg.K_g,pg.K_h,pg.K_j,pg.K_k,pg.K_l],
   #         [pg.K_z,pg.K_x,pg.K_c,pg.K_v,pg.K_b,pg.K_n,pg.K_m]


class create_keyboard(object):
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    timeshowchar = 0
    def flash_color(self, letter):
        flash_COLOR = RED   
        flash_time = 0.2
        font_keyboard = pg.font.SysFont("Alata", 60)
        self.screen.fill((205, 205, 205))  # Clear the screen
        pg.draw.rect(self.screen, key_color, pg.Rect(100, 100, 60, 60))  # Draw a key
        self.screen.blit(font_keyboard.render(letter, True, flash_COLOR), (50, 50))  # Flash the letter
        pg.display.flip()  # Update the display
        time.sleep(flash_time)  # Wait for the flash to disappear

    def draw_board(self):
        keyboard = [[] for i in range(5)]
        alphabet = [chr(i) for i in range(ord("A"), ord("Z"))]
        for index, key_row in enumerate(keyboard):
            key_row = random.sample(alphabet,5)
            keyboard[index] = key_row
            for letter in key_row:
                alphabet.remove(letter)

        REDLETTER1 = random.choice(letters)
        
        ##screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
        self.screen.fill((205, 205, 205))

        width, height = pg.display.get_surface().get_size()
        max = 0
        for row in keyboard:
            if(row.__len__() > max):
                max = row.__len__()

        num_rows = keyboard.__len__()
        key_size = width/max
        if( (key_size * num_rows) > height ):
            key_size = height/max

        x_offset = height*0.005
        y_offset = (height-(key_size*keyboard.__len__()))/2

        for row in keyboard:
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
                    pg.draw.rect(self.screen,key_color,pg.Rect(x_offset, y_offset, keySize, keySize))
                    first = False
                
                else:
                    pg.draw.rect(self.screen,key_color,pg.Rect(x_offset, y_offset, keySize, keySize))

                if(key==REDLETTER1):
                    self.screen.blit(font_keyboard.render(key, True, RED), (x_offset,y_offset))
                if(key!=REDLETTER1):
                    self.screen.blit(font_keyboard.render(key, True, font_color), (x_offset,y_offset))

                ##random_letter = random.choice(letters)
                x_offset += key_size

            x_offset = 0
            y_offset += key_size

        # dark shade of the button                     random_letter = random.choice(letters)
        color_dark = (100,100,100) 
        button = pg.Rect(width/2+200, height/2, 200, 100) 
        pg.draw.rect(self.screen, [100, 100, 100], button)  # draw button
        font_keyboard2 = pg.font.SysFont("Alata", 40)
        ##random_letter = random.choice(letters)
        self.screen.blit(font_keyboard2.render('START TEST', True, font_color), (width/2+225, height/2))

        pg.display.flip()
        self.timeshowchar = time.time()*1000
        
    def __init__(self):
        self.draw_board

def start_window():
    pg.display.set_caption("BCI training")
    keyboard = create_keyboard()
    keyboard.__init__()
    ##random_letter = random.choice(letters)
    letter_index = 0
    running = True 
    ##show_time = end_time + random.randrange(5500, 6500)

    while running:
        ##write a section that changes the flash

        for event in pg.event.get():
            
            keyboard.draw_board()
            
            if event.type == pg.QUIT:
                running = False
                break
            elif event.type == pg.KEYDOWN:
                if event.key == keys[letter_index]:
                    time_keys.append([letters[letter_index], keyboard.timeshowchar])
                    letter_index += 1
                    letter_index %= len(letters)

                elif event.key == pg.K_ESCAPE:
                    running = False
            time.sleep(3)
        
    #text = render_font(letters[letter_index])
    #screen.blit(text, (50, 50))
    #pg.draw.rect(screen,key_color,pg.Rect(100, 100, 60, 60))
    #pg.display.flip();         

try:
    start_window()
except:
    print("An error occurred. Please double check the file.")
finally:
    with open("TambakisTest.csv", "w") as fp:
        for input in time_keys:
            fp.write(f"{input[0]},{input[1]}\n")
