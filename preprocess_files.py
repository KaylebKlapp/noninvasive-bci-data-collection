import numpy as np
from glob import glob
from os import chdir

"""
Helper Functions
"""

def get_index_in_training_chars(stim_char):
    for char in training_chars:
        if char == stim_char:
            return training_chars.index(char)
    raise ValueError

"""
Compile time constants
"""

training_chars = ['k', 'v', 'e']
subjects = ['kayleb', 'jayden', 'sam', 'aris']
methods = ['flashing', 'keyboard', 'checkerboard', 'dictionary']
acceptable_difference = 1
num_samples_in_datapoint = 1000

"""
File stuff
"""

chdir("data")
files_eeg = glob("*.eeg")
files_stm = glob("*.stm")

char_times = [[] for _ in range(len(training_chars))]

for stim_file in files_stm:
    with open(stim_file) as stm:
        line = stm.readline()
        stim, time = line.split(",")[0:1]
        
        if stim in training_chars:
            char_index = get_index_in_training_chars(stim)
            char_times[char_index].append(time)
                    









