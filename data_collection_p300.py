import numpy as np  
from datetime import datetime
import time
import brainflow as bf

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
# https://docs.openbci.com/Cyton/CytonSDK/#channel-setting-commands
preset_file = "preset.txt"
preset_file_contents = ""
with open(preset_file) as fp:
    preset_file_contents = fp.read()

print(preset_file_contents)
board.config_board(preset_file_contents)

#start the data stream

# time.sleep(5)  # recommended window size for eeg metric calculation is at least 4 seconds, bigger is better
# data = np.array(board.get_board_data())

analog_channel = board.get_analog_channels(board_id)
eeg_channels = board.get_eeg_channels(board_id) 
eeg_names = board. get_eeg_names(board_id)
accel_channel = board.get_accel_channels(board_id)

print(f"eeg: {eeg_channels}")
print(f"eeg names: {eeg_names}")
print(f"analog channels: {analog_channel}")
print(f"acceleration channels: {accel_channel}")
#print(f"data shape: {data.shape}")

name = input("File prefix: ")

board.start_stream(45000)
time.sleep(0.1)
board.get_board_data()
data = []

for i in range(50):
    time.sleep(0.1)
    inter_data = board.get_board_data()
    print(inter_data.shape)
    for i in range(len(inter_data[0])):
        single_frame = [inter_data[c][i] for c in eeg_channels]
        data.append(single_frame)

board.stop_stream()

data = np.array(data)
print(data.shape)

output = ""
for d in data:
    for c in d:
        output += str(c) + ","
    output.rstrip(",")
    output += "\n"
output.rstrip("\n")

datetime.now
with open("raw_data.txt", "w") as fp:
    fp.write(output)

quit()