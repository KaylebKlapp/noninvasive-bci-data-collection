import numpy as np  
from datetime import datetime
import time
import brainflow as bf
import argparse

# Fancy unnecessary network stuff
# parser = argparse.ArgumentParser()
# args = parser.parse_args()

# Define board and serial port
board_type_id = bf.BoardIds.CYTON_BOARD
port = '/dev/ttyUSB0'
params = bf.BrainFlowInputParams()
params.serial_port = port
board = bf.BoardShim(board_type_id, params)
board_id = board.get_board_id()

board.prepare_session()

# Read the preset file, and send it to the board. This file was stolen from the BCI GUI saved file
preset_file = "preset.txt"
preset_file_contents = ""
with open(preset_file) as fp:
    preset_file_contents = fp.read()

print(preset_file_contents)
board.config_board(preset_file_contents)

#start the data stream
board.start_stream(45000)

time.sleep(5)  # recommended window size for eeg metric calculation is at least 4 seconds, bigger is better
data = np.array(board.get_board_data())


analog_channel = board.get_analog_channels(board_id)
eeg_channels = board.get_eeg_channels(board_id) 
eeg_names = board. get_eeg_names(board_id)
accel_channel = board.get_accel_channels(board_id)


print(f"eeg: {eeg_channels}")
print(f"eeg names: {eeg_names}")
print(f"analog channels: {analog_channel}")
print(f"acceleration channels: {accel_channel}")
print(f"data shape: {data.shape}")
board.stop_stream()

for i in eeg_channels:
    print(i, end=": ")
    print(data[i][250], end = ", ")
    print(data[i][500], end = ", ")
    print(data[i][750])

quit()