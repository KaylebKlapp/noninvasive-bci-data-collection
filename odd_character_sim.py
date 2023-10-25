import pygame
import numpy as np  
from datetime import datetime
import time
import brainflow as bf
import argparse
import random

# Initialize Pygame Things
pygame.init()
pygame.font.init()
pygame.display.set_caption("BCI training")

KEY_WORD_PROB = 0.3             #How often a word with a key letter is used
NORMAL_CHAR_COLOR = (0, 0, 0)   #Color of all non-odd letters, Defaut it black. Do not change.

FONT = pygame.font.SysFont("Alata", 50)
FONTS = pygame.font.get_fonts()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 550
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

time_keys = []
alphabet = [chr(i) for i in range(ord("A"), ord("Z"))]
nontraining_letters = alphabet

training_letters = ['K', 'W', 'E']
for let in training_letters:
    nontraining_letters.remove(let)
    
keys = [pygame.K_k, pygame.K_w, pygame.K_e]

words_file_with_keys = open("words_with_keys.txt", "r")
words_file_with_keys_contents = words_file_with_keys.read()
words_with_keys = words_file_with_keys_contents.split("\n")
words_file_with_keys.close()

words_file_without_keys = open("words_without_keys.txt", "r")
words_file_without_keys_contents = words_file_without_keys.read()
words_without_keys = words_file_without_keys_contents.split("\n")
words_file_without_keys.close()

def get_random_word(words):
    return random.choice(words)

def get_random_wordbank():
    if random.random() < KEY_WORD_PROB:
        return words_without_keys
    else:
        return words_with_keys

def get_random_color(minimum_color = 50, maximum_color = 215):
    return (random.randint(minimum_color, maximum_color), random.randint(minimum_color, maximum_color), random.randint(minimum_color, maximum_color))

def render_font(str, font, color):
    text = font.render(str, True, color)
    return text

def render_word(word, odd_char_color, odd_char_index):
    for i in range(len(word)):
        if i == odd_char_index:
            text = render_font(word[i], FONT, odd_char_color)
            SCREEN.blit(text, (i*15+25, SCREEN_HEIGHT/2))
        else:
            text = render_font(word[i], FONT, NORMAL_CHAR_COLOR)
            SCREEN.blit(text, (i*15+25, SCREEN_HEIGHT/2))

def start_window():

    word_bank = get_random_wordbank()
    word = get_random_word(word_bank)
    odd_char_color = (255, 0, 0)    #Color of odd letter. Default is red
    odd_char_index = 0              #Index of odd char
    
    #letter_index = 0
    running = True;
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;
                break
            elif event.type == pygame.KEYDOWN:
                odd_char_color = get_random_color()
                word = get_random_word(word_bank)
                odd_char_index = random.randint(0,len(word)-1)
                print(odd_char_index)

                """
                if event.key == pygame.K_RETURN:
                    time_keys.append([training_letters[letter_index], int(time.time() * 1000)])
                    letter_index += 1
                    letter_index %= len(training_letters)
                
                if event.key == keys[letter_index]:
                    time_keys.append([training_letters[letter_index], int(time.time() * 1000)])
                    letter_index += 1
                    letter_index %= len(training_letters)
                """
        SCREEN.fill((205, 205, 205))
        render_word(word, odd_char_color, odd_char_index)
        pygame.display.flip();                    

start_window()
"""
try:
    start_window()
except:
    print("An error occurred. Please double check the file.")
finally:
    with open("test.csv", "w") as fp:
        for input in time_keys:
            fp.write(f"{input[0]},{input[1]}\n")
"""
