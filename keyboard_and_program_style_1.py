import pygame as pg
from datetime import datetime
import random

date_string = datetime.now().strftime("%y_%m_%d_%H_%M_%S")
collection_type = "keyboard_stim"
subject_name = "jayden"
more_info = ""

time_keys = []
LETTERS = ['K', 'E', 'V']
KEYS = [pg.K_k, pg.K_e, pg.K_v]
FONT_COLOR = tuple((255,255,255))
KEY_COLOR = tuple((0,0,0))
FLASH_COLOR = tuple((255,0,0))
SCREEN_BACKGROUND = tuple((205,205,205))
KEY_BUFFER = 0.95
KEYBOARD_FONT = "Alata"
ENLARGE_KEY_SIZE = 2
ENLARGE_LETTER_SIZE = 1.5
FLASH = True
TIME_UNTIL_NEXT_STIM_CONST_RANGE = [1500,3000]
TIME_BETWEEN_CHARS_CONST_RANGE = [2000,5000]
TRAINING_KEY_PERCENTAGE = 0.30
RANDOM_METHOD = False
RANDOM_KEYBOARD_KEYS = False
RANDOM_KEYBOARD_SIZE = False
NEW_KEYBOARD_FREQUENCY_RANGE = [3,5]

# Method 1 = flash, 2 = enlarge, 3 = disappear
METHOD = 1
KEYBOARD_ROW_RANGE = [3,5]

alphabet = [chr(i) for i in range(ord("A"), ord("Z"))]
nontraining_letters = alphabet

for let in LETTERS:
    nontraining_letters.remove(let)

letter = "V"
key = pg.key.key_code(letter)
LETTERS = [letter]
KEYS = [key]

# [character, size, coordinate]
keyboard = [
            [['Q',0,tuple],['W',0,tuple],['E',0,tuple],['R',0,tuple],['T',0,tuple],['Y',0,tuple],['U',0,tuple],['I',0,tuple],['O',0,tuple],['P',0,tuple]],
            [['A',0,tuple],['S',0,tuple],['D',0,tuple],['F',0,tuple],['G',0,tuple],['H',0,tuple],['J',0,tuple],['K',0,tuple],['L',0,tuple]],
            [['Z',0,tuple],['X',0,tuple],['C',0,tuple],['V',0,tuple],['B',0,tuple],['N',0,tuple],['M',0,tuple]]
]

def randomize_board_keys():
    global keyboard
    alphabet = [chr(i) for i in range(ord("A"), ord("Z")+1)]
    for row in range(keyboard.__len__()):
        for col in range(keyboard[row].__len__()):
            replacement = random.sample(alphabet,1)
            keyboard[row][col][0] = replacement[0]
            alphabet.remove(replacement[0])

def randomize_board_size():
    global keyboard
    alphabet_size = 26
    keyb_length = random.randint(KEYBOARD_ROW_RANGE[0],KEYBOARD_ROW_RANGE[1])
    keyboard.clear()
    keyboard = [[] for i in range(keyb_length)]
    start = int(alphabet_size/keyb_length) - 2
    end = int(alphabet_size/keyb_length) + 2
    col_range = [start, end]
    for row in range(keyboard.__len__()):
        num_cols = random.randint(col_range[0],col_range[1])
        if( num_cols > alphabet_size ):
            num_cols = alphabet_size
        
        keyboard[row] = [['A',0,tuple] for i in range(num_cols)]
        alphabet_size -= num_cols

        if( row >= (keyboard.__len__()-1) and alphabet_size != 0 ):
            while(alphabet_size != 0):
                min_row = 100
                index = 0
                for i in range(keyboard.__len__()):
                    if( keyboard[i].__len__() < min_row ):
                        min_row = keyboard[i].__len__()
                        index = i

                keyboard[index].append(['A',0,tuple]) 
                alphabet_size -= 1


if( RANDOM_KEYBOARD_SIZE ):
    randomize_board_size()
        
if( RANDOM_KEYBOARD_KEYS ):
    randomize_board_keys()