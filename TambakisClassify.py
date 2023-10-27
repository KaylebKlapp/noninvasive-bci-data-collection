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
keys = [pg.K_k, pg.K_w, pg.K_e]
font_color = (255,255,255)
key_color = (0,0,0)
key_buffer = 0.95
date_string = datetime.now().strftime("%y_%m_%d_%H_%M_%S")
collection_type = "checkerboard"
subject_name = "Aristomenes"
more_info = ""

file_name = f"{date_string}_{subject_name}_{collection_type}_{more_info}.txt"

#keyboard = [
 #           [pg.K_q,pg.K_w,pg.K_e,pg.K_r,pg.K_t,pg.K_y,pg.K_u,pg.K_i,pg.K_o,pg.K_p],
  #          [pg.K_a,pg.K_s,pg.K_d,pg.K_f,pg.K_g,pg.K_h,pg.K_j,pg.K_k,pg.K_l],
   #         [pg.K_z,pg.K_x,pg.K_c,pg.K_v,pg.K_b,pg.K_n,pg.K_m]


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
        self.keyboard = [[] for i in range(5)]
    square_locationx, square_locationy = (0,0)
    keysizeclass= 0
    
    def randomizeboard(self): 
        pass
    def draw_board(self):
        keyboard = [[] for i in range(5)]
        alphabet = [chr(i) for i in range(ord("A"), ord("Z"))]
        for index, key_row in enumerate(self.keyboard):
            key_row = random.sample(alphabet,5)
            self.keyboard[index] = key_row
            for letter in key_row:
                alphabet.remove(letter)

        REDLETTER1 = random.choice(letters)
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
                    if(key==REDLETTER1):
                        pg.draw.rect(self.screen,(255,255,255),pg.Rect(x_offset, y_offset, keySize, keySize))
                        self.square_locationx, self.square_locationy = (x_offset,y_offset)
                        self.keysizeclass = keySize
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

       
        self.timeshowchar = time.time()*1000
        pg.display.flip()
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
    keyboard.draw_board()

    while running:
        ##write a section that changes the flash
        ##keyboard.draw_board()
        for event in pg.event.get():
           
            if event.type == pg.QUIT:
                running = False
                break
            elif event.type == pg.KEYDOWN:
                keyboard.randomize_board()
                keycodetest = pg.key.key_code(keyboard.randomcharchoice1)
                if event.key == keycodetest:
                    time_keys.append([keyboard.randomcharchoice1, keyboard.timeshowchar])
                    ##print(time_keys[1])
                    keyboard.draw_board()
                    ##callrandomize board here
                    if ((time.time())*3) % 2 ==0 :
                        
                        pg.draw.rect(keyboard.screen,(0,0,0),pg.Rect(keyboard.square_locationx, keyboard.square_locationy, keyboard.keysizeclass, keyboard.keysizeclass))
                        pg.display.flip()
                    ##else:
                        ##pg.draw.rect(keyboard.screen,(255,255,255),pg.Rect(keyboard.square_locationx, keyboard.square_locationy, keyboard.keysizeclass, keyboard.keysizeclass))
                    
                    letter_index += 1
                    letter_index %= len(letters)

                if event.key == pg.K_ESCAPE:
                    running = False

        if (int(time.time() * 2) % 2 == 0):
            keyboard.draw_board(color_for_diff_box=BLACK, color_for_diff_letter=WHITE)
        else:
            keyboard.draw_board(color_for_diff_box=RED, color_for_diff_letter=BLACK)
        


        pg.display.flip()
        
            #time.sleep(3)
        
    #text = render_font(letters[letter_index])
    #screen.blit(text, (50, 50))
    #pg.draw.rect(screen,key_color,pg.Rect(100, 100, 60, 60))
    #pg.display.flip();         

try:
    start_window()
except Exception as e:
    print(e.__str__())
    print("An error occurred. Please double check the file.")
finally:
    with open("TambakisTest.csv", "w") as fp:
        for input in time_keys:
            fp.write(f"{input[0]},{input[1]}\n")
