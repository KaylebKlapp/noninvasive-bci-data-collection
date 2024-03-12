import numpy as np  
from datetime import datetime
import time
import os
import brainflow as bf


# Type of collections
__collection_name__ = input("File prefix: ")
name = input("Name: ")

def write_data(data):
    data = np.array(data)
    print(data.shape)

    output = ""
    for d in data:
        for c in d:
            output += str(c) + ","
        output = output.rstrip(",")
        output += "\n"
    output = output.rstrip("\n")

    with open(f"data/{collect_key}_{name}_{_date_time_}_{__collection_name__}_{0}_{0}.stm", "a") as fp:
        fp.write(output)
    
    data = []

# Fancy unnecessary network stuff
# parser = argparse.ArgumentParser()
# args = parser.parse_args()
collect_key = int(time.time())
with open("collect_key.txt", "w") as fp:
    fp.write(f"{collect_key}")
    fp.close()


# Define board and serial port
board_type_id = bf.BoardIds.CYTON_BOARD
port = '/dev/ttyUSB0'
params = bf.BrainFlowInputParams()
params.serial_port = port
board = bf.BoardShim(board_type_id, params)
board_id = board.get_board_id()

board.prepare_session()

# Read the preset file, and send it to the board. This file was stolen from the BCI GUI saved file
# https://docs.openbci.com/Cyton/CytonSDK/#channel-setting-commands

file_suffix = "_" + name
preset_file = f"preset{file_suffix}.txt"
preset_file_contents = ""
with open(preset_file) as fp:
    preset_file_contents = fp.read()

print(preset_file_contents)
board.config_board(preset_file_contents)

#start the data stream

# time.sleep(5)  # recommended preset.txt.txtindow size for eeg metric calculation is at least 4 seconds, bigger is better
# data = np.array(board.get_board_data())

analog_channel = board.get_analog_channels(board_id)
eeg_channels = board.get_eeg_channels(board_id) 
eeg_names = board. get_eeg_names(board_id)
accel_channel = board.get_accel_channels(board_id)

print(f"eeg: {eeg_channels}")
print(f"eeg names: {eeg_names}")
print(f"analog channels: {analog_channel}")
print(f"acceleration channels: {accel_channel}")

"""
File handling variables
"""

# preferably your name
__subject_name__ = name

# Date time string
_date_time_ = datetime.now().strftime("%y_%m_%d_%H_%M_%S")

def start_data_stream():
    data = []
    inputText = ""
    __collection_name__ = inputText
    
    while (inputText != "quit"):
        try:
            board.start_stream(45000)
            time.sleep(0.1)
            board.get_board_data()

            while True:
                time.sleep(0.1)
                inter_data = board.get_board_data()
                for i in range(len(inter_data[0])):
                    single_frame = [inter_data[c][i] for c in eeg_channels]
                    new_row = [int(time.time() * 10000)]
                    new_row.extend(single_frame)
                    data.append(new_row)
                if (len(data)) > 1000:
                    write_data(data)
                    data = []
        except:
            print(f"Writing data to file {len(data)}")
            write_data(data)
            board.stop_stream()
            break

    
end_time = 0
start_time = time.time() * 1000


with open(f"data/{collect_key}_{name}_{_date_time_}_{__collection_name__}_{0}_{0}.stm", "w"):
    pass
          
start_data_stream()
