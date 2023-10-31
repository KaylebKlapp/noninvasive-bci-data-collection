import pygame
import numpy as np  
from datetime import datetime
import time
import argparse
import random

"""
Strings for file formatting, these should be standard between all programs
"""
date_string = datetime.now().strftime("%y_%m_%d_%H_%M_%S")
collection_type = "flashing_stim"
subject_name = "kayleb"
more_info = ""


# Admin Stuff for pygame
pygame.init()
pygame.font.init()

# Font managing, the fronts in these arrays are not human readable
font = pygame.font.SysFont("Alata", 500)
fonts = pygame.font.get_fonts()
unreadable_font_indexes = [22, 37, 49, 51, 70, 71, 73, 75, 87, 92, 95, 96, 105, 115, 119, 121, 137, 139, 140, 143, 144, 149, 150, 151, 152]
unreadable_letter_font_indexes = [3, 38, 48, 54, 65, 66, 67, 68, 70, 75, 86, 87, 91, 96, 102, 106, 109, 100, 111, 115, 117, 127]

#Removing the fonts in reverse order, so that I dont mess up the indexes
unreadable_font_indexes.reverse()
for inx in unreadable_font_indexes:
    print(inx)
    del fonts[inx]

unreadable_letter_font_indexes.reverse()
for inx in unreadable_letter_font_indexes:
    print(inx)
    del fonts[inx]

# Screen Constants
screen_width = 1200
screen_height = 1000
length_of_flash = 300

# The array used for file output
time_keys = []

# Build the alphabet array, and segment into training and non-training letters
alphabet = [chr(i) for i in range(ord("A"), ord("Z"))]
nontraining_letters = alphabet
training_letters = ['K', 'V', 'E']
training_keys = [pygame.key.key_code(letter) for letter in training_letters]

for let in training_letters:
    nontraining_letters.remove(let)

# Gets a random key and (if its a training key) it returns the keycode as well
def get_random_letter_key_pair():
    if (random.random() <= .50):
        rand_index = random.randint(0,len(training_keys))
    else:
        return nontraining_letters[random.randrange(0, len(nontraining_letters) - 1)], None
    return (training_letters[rand_index], training_keys[rand_index])

# Get a random color, decreasing the max color makes the letters darker, increasing min makes it lighter
def get_random_color(min_range = 0, max_range = 220):
    return (random.randrange(min_range, max_range), random.randrange(min_range, max_range), random.randrange(min_range, max_range))

# Using the font arrays declared earlier, we randomize just about everything with the font.
def get_random_font(randomize_attributes = False):
    font_index = random.randint(0, len(fonts))
    font = fonts[font_index]
    font_made = pygame.font.SysFont(font, random.randrange(400, 750))
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

# Main pygame loop
def start_window():
    """
    Beginning loop admin
    """
    # Setting this to false gives a brief pause on starting the program
    showing_character = False
    font_index = random.randint(0, len(fonts))
    pygame.display.set_caption("BCI training")
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = get_random_font(randomize_attributes=True)
    color = get_random_color()
    
    """
     Admin for showing first character. In this configuration, the first letter will show
     at only the random number (in ms) generated below after the program is started.

     end_time is the time that the letter will stop showing
     show_time is the time that the next letter will start
    """
    end_time = time.time()
    show_time = end_time + random.randrange(5500, 6500)

    # Randomizing for the first character
    character, character_key = get_random_letter_key_pair()
    font_index = random.randint(0, len(fonts))
    font = get_random_font(randomize_attributes=True)
    color = get_random_color()
    
    running = True
    while running:

        # If we are past the time that we should be showing the letter, stop showing the letter
        if (time.time() * 1000 > end_time):
            showing_character = False
        
        # If we are past the time to show a new character, generate a new character.
        if (time.time() * 1000 > show_time):
            showing_character = True
            end_time = (time.time() * 1000) + length_of_flash
            character, character_key = get_random_letter_key_pair()
            font = get_random_font(randomize_attributes=True)
            color = get_random_color()

            # Some portion of the time, we want to pause for an extended period of time.
            if (random.randint(0,10) == 0):
                show_time = end_time + random.randrange(5500, 6500)

                # And we can mark it in the data
                time_keys.append(["~", end_time + 1000])
            else:
                show_time = end_time + random.randrange(500, 2500)

        # Events manager
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                showing_character = False
                if event.key == pygame.K_BACKSPACE:
                    del time_keys[-1]
                if character in training_letters and event.key == character_key:
                    time_keys.append([character, show_time])
                   
        screen.fill((205, 205, 205))

        # Only show the character if the showing_character is true. Also center it.
        if (showing_character):
            text = font.render(character, True, color)
            width_mid = (screen_width - text.get_width()) // 2
            height_mid = (screen_height - text.get_height()) // 2
            screen.blit(text, (width_mid, height_mid))

        pygame.display.flip()

time_end_training = 0
time_start_training = int(time.time() * 1000)
start_window()
time_end_training = int(time.time() * 1000)

try:
    pass
except Exception as e:
    print(e.__str__())
    print("An error occurred. Please double check the file.")
    time_end_training = int(time.time() * 1000)
finally:
    file_name = f"{date_string}_{subject_name}_{collection_type}_{more_info}_{time_end_training}_{time_start_training}.txt"
    with open(file_name, "w") as fp:
        for input in time_keys:
            fp.write(f"{input[0]},{input[1]}\n")
