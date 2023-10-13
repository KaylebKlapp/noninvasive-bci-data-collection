import time
from datetime import datetime
import brainflow as bf
import numpy as np
import pygame as pg

pg.init()
pg.font.init()
font = pg.font.SysFont("Alata", 700)

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
#]
keyboard = [
            ['q','w','e','r','t','y','u','i','o','p'],
            ['a','s','d','f','g','h','j','k','l'],
            ['z','x','c','v','b','n','m']
]

def render_font(str):
    text = font.render(str, True, font_color)
    return text

def render_screen():
    # Sets the pg screen to fit the entire screen
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
    return screen

class create_keyboard(object):
    def __init__(self):
        screen = render_screen()
        screen.fill((205, 205, 205))

        #first row = 10
        #second row = 9
        #third row = 7
        width, height = pg.display.get_surface().get_size()

        max = 0
        for row in keyboard:
            if(row.__len__() > max):
                max = row.__len__()

        key_size = width/max
        x_offset = height*0.005
        y_offset = (height-(key_size*keyboard.__len__()))/2

        for row in keyboard:
            num_keys = row.__len__()
            if(num_keys == max ):
                row_offset = 0
            else:
                row_offset = (max-num_keys)*(key_size/2)
            
            first = True
            for key in row:
                if(first):
                    x_offset += row_offset
                    Rect = pg.draw.rect(screen,key_color,pg.Rect(x_offset, y_offset, key_size*key_buffer, key_size*key_buffer))
                    first = False
                else:
                    Rect = pg.draw.rect(screen,key_color,pg.Rect(x_offset, y_offset, key_size*key_buffer, key_size*key_buffer))

                screen.blit(font.render(key, True, key_color, (200,100)))
                x_offset += key_size
            x_offset = 0
            y_offset += key_size

        pg.display.flip()
        

def start_window():
    pg.display.set_caption("BCI training")
    keyboard = create_keyboard()
    keyboard.__init__()

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
                
    
    #text = render_font(letters[letter_index])
    #screen.blit(text, (50, 50))
    #pg.draw.rect(screen,key_color,pg.Rect(100, 100, 60, 60))
    #pg.display.flip();         

try:
    start_window()
except:
    print("An error occurred. Please double check the file.")
finally:
    with open("test.csv", "w") as fp:
        for input in time_keys:
            fp.write(f"{input[0]},{input[1]}\n")
