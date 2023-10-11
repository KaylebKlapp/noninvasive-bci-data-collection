import pygame
import numpy as np  
from datetime import datetime
import time
import brainflow as bf
import argparse
import random

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Alata", 700)
fonts = pygame.font.get_fonts()

time_keys = []
alphabet = [chr(i) for i in range(int("A"), int("Z"))]
nontraining_letters = alphabet

training_letters = ['K', 'W', 'E']
for let in training_letters:
    nontraining_letters.remove(let)
    
keys = [pygame.K_k, pygame.K_w, pygame.K_e]

def get_random_color():
    return (random.randrange(256), random.randrange(256), random.randrange(256))

def render_ront(str, font, color = (0, 0, 0)):
    text = font.render(str, True, (0,0,0))
    return text

def start_window():
    pygame.display.set_caption("BCI training")
    screen = pygame.display.set_mode((550, 500))
    
    letter_index = 0
    running = True;
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == keys[letter_index]:
                    time_keys.append([training_letters[letter_index], int(time.time() * 1000)])
                    letter_index += 1
                    letter_index %= len(training_letters)
                    
        screen.fill((205, 205, 205))
        text = render_ront(training_letters[letter_index])
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
