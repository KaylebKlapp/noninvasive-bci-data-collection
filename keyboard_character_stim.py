import argparse
import time
from datetime import datetime
import brainflow as bf
import numpy as np
import pygame
from tkinter import *

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Alata", 700)

time_keys = []
letters = ['K', 'W', 'E']
keys = [pygame.K_k, pygame.K_w, pygame.K_e]
height_buffer = 0.05
width_buffer = 0.05

def render_ront(str, color = (255, 255, 255)):
    text = font.render(str, True, color)
    return text

def render_screen():
    root = Tk()
    # Get the bounds of the pygame window. Establishes window size and the
    # size of space between the screen and the size of your screen
    screen_width = root.winfo_screenwidth()
    w_buffer = screen_width*width_buffer
    screen_height = root.winfo_screenheight()
    h_buffer = screen_height*height_buffer

    # Establish the screen
    screen = pygame.display.set_mode((screen_width-w_buffer, screen_height-h_buffer))
    return screen

def start_window():
    pygame.display.set_caption("BCI training")
    screen = render_screen()
    
    letter_index = 0
    running = True;
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == keys[letter_index]:
                    time_keys.append([letters[letter_index], int(time.time() * 1000)])
                    letter_index += 1
                    letter_index %= len(letters)
                    
        screen.fill((205, 205, 205))
        text = render_ront(letters[letter_index])
        screen.blit(text, (50, 50))
        pygame.display.flip();                    

try:
    start_window()
except:
    print("An error occurred. Please double check the file.")
finally:
    with open("test.csv", "w") as fp:
        for input in time_keys:
            fp.write(f"{input[0]},{input[1]}\n")
