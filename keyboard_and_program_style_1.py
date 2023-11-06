import pygame as pg
from datetime import datetime
import random

date_string = datetime.now().strftime("%y_%m_%d_%H_%M_%S")
collection_type = "keyboard_stim"
subject_name = "jayden"
more_info = ""

time_keys = []
LETTERS = ['K', 'W', 'E']
KEYS = [pg.K_k, pg.K_w, pg.K_e]
FONT_COLOR = tuple((255,255,255))
KEY_COLOR = tuple((0,0,0))
FLASH_COLOR = tuple((255,0,0))
SCREEN_BACKGROUND = tuple((205,205,205))
KEY_BUFFER = 0.95
KEYBOARD_FONT = "Alata"
ENLARGE_KEY_SIZE = 2
ENLARGE_LETTER_SIZE = 1.5
FLASH = True
TIME_UNTIL_NEXT_STIM_CONST_RANGE_START = 1500
TIME_UNTIL_NEXT_STIM_CONST_RANGE_END = 3000
TIME_BETWEEN_CHARS_CONST_RANGE_START = 2000
TIME_BETWEEN_CHARS_CONST_RANGE_END = 5000
TRAINING_KEY_PERCENTAGE = 0.50
RANDOM_METHOD = True
RANDOM_KEYBOARD = True
NEW_KEYBOARD_FREQUENCY_START = 3
NEW_KEYBOARD_FREQUENCE_END = 5
METHOD = 1

training_keys = [pg.key.key_code(letter) for letter in LETTERS]

alphabet = [chr(i) for i in range(ord("A"), ord("Z"))]
nontraining_letters = alphabet

for let in LETTERS:
    nontraining_letters.remove(let)

# [character, size, coordinate]
keyboard = [
            [['Q',0,tuple],['W',0,tuple],['E',0,tuple],['R',0,tuple],['T',0,tuple],['Y',0,tuple],['U',0,tuple],['I',0,tuple],['O',0,tuple],['P',0,tuple]],
            [['A',0,tuple],['S',0,tuple],['D',0,tuple],['F',0,tuple],['G',0,tuple],['H',0,tuple],['J',0,tuple],['K',0,tuple],['L',0,tuple]],
            [['Z',0,tuple],['X',0,tuple],['C',0,tuple],['V',0,tuple],['B',0,tuple],['N',0,tuple],['M',0,tuple]]
]

def randomize_board():
    alphabet = [chr(i) for i in range(ord("A"), ord("Z")+1)]
    for row in range(keyboard.__len__()):
        for col in range(keyboard[row].__len__()):
            replacement = random.sample(alphabet,1)
            #print(replacement)
            keyboard[row][col][0] = replacement[0]
            alphabet.remove(replacement[0])

if( RANDOM_KEYBOARD ):
    randomize_board()