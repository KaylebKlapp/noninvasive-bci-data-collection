import numpy as np
from glob import glob
from os import chdir

chdir("data")
files_eeg = glob("*.eeg")
files_stm = glob("*.stm")

for file in files_stm:
    print(file)

