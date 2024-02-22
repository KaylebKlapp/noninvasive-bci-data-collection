import numpy as np
from glob import glob
from os import chdir
import random


"""*****************************************************************************
Helper Functions
*****************************************************************************"""


def get_index_in_training_chars(stim_char):
    for char in training_chars:
        if char == stim_char:
            return training_chars.index(char)
    raise ValueError

def downsize_array(array, newsize):
    num_to_remove = len(array) - newsize
    if num_to_remove <= 0:
        return array
    else:
        samples_to_remove = random.sample(array, num_to_remove)
        for sample in samples_to_remove:
            array.remove(sample)
        return array

"""
*****************************************************************************
Compile time constants
*****************************************************************************
"""

training_chars = ['k', 'v', 'e']
subjects = ['kayleb', 'jayden', 'sam', 'aris']
methods = ['flashing', 'keyboard', 'checkerboard', 'dictionary']
acceptable_difference = 5
num_samples_in_datapoint = 1000


"""**************************************************************************
File stuff
**************************************************************************"""

chdir("data")
files_eeg = glob("*.eeg")
files_stm = glob("*.stm")

char_times = [[] for _ in range(len(training_chars))]
non_train_times = []
stim_file_ids = []


"""**************************************************************************
Begin Preprocessing
**************************************************************************"""

# Start by getting all of the samples we want to train on, and an equal number of non trianing samples

for stim_file in files_stm:
    stim_id = stim_file.split("_")[0]
    if stim_id is not int:
        print(f"Improper file name format: {stim_file}")
        continue

    stim_file_ids.append(stim_id)
    with open(stim_file) as stm:
        line = stm.readline()
        while line != "":
            stim, time = line.split(",")[0:2]
            stim = stim.lower()
            
            if stim in training_chars:
                char_index = get_index_in_training_chars(stim)
                char_times[char_index].append(time)
            else:
                non_train_times.append(time)
            line = stm.readline()

# Find the array with the smallest 
min_num_samples = len(char_times[0])
for array in char_times:
    if len(array) < min_num_samples:
        min_num_samples = len(array)

min_num_samples = min(min_num_samples, len(non_train_times))

# Downsize the arrays to all be the same size
for i in range(len(char_times)):
    char_times[i] = downsize_array(char_times[i], min_num_samples)
non_train_times = downsize_array(non_train_times, min_num_samples)

in_eeg_file = [[] for file in files_eeg]

for file in files_eeg:
    start_time, end_time = file.split("_")[-1:-3]
    print(start_time, end_time) 
 

