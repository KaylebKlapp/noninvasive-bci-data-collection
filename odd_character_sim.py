import pygame
import numpy as np  
from datetime import datetime
import time
import brainflow as bf
import argparse
import random

"""
Strings for file formatting, these should be standard between all programs
"""
date_string = datetime.now().strftime("%y_%m_%d_%H_%M_%S")
collection_type = "flashing_stim"
subject_name = "Sam"
more_info = ""

# Initialize Pygame Things
pygame.init()
pygame.font.init()
pygame.display.set_caption("BCI training")

KEY_WORD_PROB = 1             #How often a word with a key letter is used
NORMAL_CHAR_COLOR = (0, 0, 0)   #Color of all non-odd letters, Defaut it black. Do not change.
MIN_FONT_SIZE = 50
MAX_FONT_SIZE = 150

KEY_LETTER_1 = 'k'
KEY_LETTER_2 = 'v'
KEY_LETTER_3 = 'e'

fonts = pygame.font.get_fonts()
unreadable_font_indexes =[3, 22, 37, 40, 49, 51, 52, 58, 69, 70, 71, 72, 73, 74, 75, 76, 78, 83, 87, 92, 95, 96, 98, 99, 103, 105, 109, 115, 116, 119, 120, 121, 122, 125, 127, 131, 133, 136, 137, 139, 140, 143, 144, 148, 150, 151, 152]

#Removing the fonts in reverse order, so that I dont mess up the indexes
unreadable_font_indexes.reverse()
for inx in unreadable_font_indexes:
    del fonts[inx]


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 550
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# The array used for file output
time_keys = []

# Build the alphabet array, and segment into training and non-training letters
alphabet = [chr(i) for i in range(ord("a"), ord("z"))]
nontraining_letters = alphabet
training_letters = [KEY_LETTER_1, KEY_LETTER_2, KEY_LETTER_3]
training_keys = [pygame.key.key_code(letter) for letter in training_letters]

for let in training_letters:
    nontraining_letters.remove(let)
    
"""
# Gets a random key and (if its a training key) it returns the keycode as well
def get_random_letter_key_pair():
    if (random.random() <= .50):
        rand_index = random.randint(0,len(training_keys))
    else:
        return nontraining_letters[random.randrange(0, len(nontraining_letters) - 1)], None
    return (training_letters[rand_index], training_keys[rand_index])
"""

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

def get_random_letter_inx(word):
    return random.randint(0,len(word)-1)

def get_key_index(word):
    while(True):
        inx = random.randint(0, len(word)-1)
        if word[inx] in training_letters:
            return inx
        
def get_odd_char_index(word, word_bank):
    if set(word_bank).union(set(training_letters)):  #Get odd char index. If key word, make sure its a key, otherwise randomize
        return get_key_index(word)
    return get_random_letter_inx(word)

def get_random_wordbank():
    if random.random() < KEY_WORD_PROB:
        return words_with_keys
    else:
        return words_without_keys
    
def get_random_font():
    return random.choice(fonts)

def get_random_color(minimum_color = 50, maximum_color = 215):
    return (random.randint(minimum_color, maximum_color), random.randint(minimum_color, maximum_color), random.randint(minimum_color, maximum_color))

def get_letter_key_code(letter):
    return pygame.key.key_code(letter)

def randomize_font(font, randomize_attributes = True):
    font_made = pygame.font.Font(None, font.get_height())
    if (randomize_attributes):
        random_float = random.random()
        if random_float < 0.20:
            pygame.font.Font.set_bold(font_made, True)
        
        random_float = random.random()
        if random_float < 0.20:
            pygame.font.Font.set_italic(font_made, True)
        
        random_float = random.random()
        if random_float < 0.20:
            pygame.font.Font.set_strikethrough(font_made, True)

        random_float = random.random()
        if random_float < 0.20:
            pygame.font.Font.set_underline(font_made, True)
        
    return font_made

def render_font(str, font, color):
    text = font.render(str, True, color)
    return text

def render_word(word, font, odd_font, odd_char_color, odd_char_index):
    len_word = 0  # Initialize the total width of the word
    for letter in word:
        text = render_font(letter, font, NORMAL_CHAR_COLOR)
        len_word += text.get_width()

    # Calculate the starting x-coordinate to center the word
    start_x = (SCREEN_WIDTH - len_word) // 2

    len_prev_chars = start_x

    for i in range(len(word)):
        if i == odd_char_index:
            text = render_font(word[i], odd_font, odd_char_color)
        else:
            text = render_font(word[i], font, NORMAL_CHAR_COLOR)

        len_letter = text.get_width()
        SCREEN.blit(text, (len_prev_chars, SCREEN_HEIGHT/2))
        len_prev_chars += len_letter

def start_window():

    word_bank = get_random_wordbank()
    word = get_random_word(word_bank)
    odd_char_color = (255, 0, 0)        #Color of odd letter. Default is red
    odd_char_index = get_odd_char_index(word, word_bank)


    odd_char = word[odd_char_index]

    sys_font = get_random_font()
    font = pygame.font.SysFont(sys_font, random.randint(MIN_FONT_SIZE, MAX_FONT_SIZE))    #Font
    odd_font = randomize_font(font) #Font
    start_time = time.time()*1000
    
    #letter_index = 0
    running = True;
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;
                break
            elif event.type == pygame.KEYDOWN:
                if odd_char in training_letters and int(event.key) == int(get_letter_key_code(odd_char)):
                    time_keys.append([odd_char, start_time])
                elif odd_char not in training_letters:
                    time_keys.append([odd_char, start_time])

                word_bank = get_random_wordbank()           #Get a wordbank, one with key letters or one without
                odd_char_color = get_random_color()         #Odd character color
                word = get_random_word(word_bank)           #Get random word from wordbank
                odd_char_index = get_odd_char_index(word, word_bank)    #get odd char index
                odd_char = word[odd_char_index]             #Get odd char for time_keys (data collection)

                sys_font = get_random_font()
                font = pygame.font.SysFont(sys_font, random.randint(MIN_FONT_SIZE, MAX_FONT_SIZE))
                odd_font = randomize_font(font)

                SCREEN.fill((205, 205, 205))
                pygame.display.flip()
                pygame.time.wait(random.randint(0,3000))

        SCREEN.fill((205, 205, 205))
        render_word(word, font, odd_font, odd_char_color, odd_char_index)
        pygame.display.flip()
        start_time = time.time() * 1000
                    

try:
    start_window()
    print(time_keys)
except:
    print("An error occurred. Please double check the file.")
finally:
    with open("test.csv", "w") as fp:
        for input in time_keys:
            fp.write(f"{input[0]},{input[1]}\n")
