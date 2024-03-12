import numpy as np
from glob import glob
from os import chdir


"""*****************************************************************************
Helper Functions
*****************************************************************************"""


def get_index_in_training_chars(stim_char):
    for char in training_chars:
        if char == stim_char:
            return training_chars.index(char)
    raise ValueError

"""
Compile time constants
"""

training_chars = ['up', 'down', 'left', 'right', 'down']
subjects = ['jayden']
length_of_input = 0.5
num_samples_in_datapoint = 255 * length_of_input

"""**************************************************************************
File stuff
**************************************************************************"""

chdir("data")
files_eeg = glob("*.stm")

"""**************************************************************************
Begin Preprocessing
**************************************************************************"""

split_files = [[] for _ in training_chars]
for file in files_eeg:
    for direction in training_chars 

# Downsize the arrays to all be the same size
# for i in range(len(char_times)):
#     char_times[i] = downsize_array(char_times[i], min_num_samples)
# non_train_times = downsize_array(non_train_times, min_num_samples)

in_eeg_file = [[] for file in files_eeg]

for file in files_eeg:
    start_time, end_time = file.split("_")[-1:-3]
    print(start_time, end_time) 
 

