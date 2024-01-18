"""   
    Makoto preprocessing data 
     Change the option to use double precision
    Import data
    Downsample if necessary
    High-pass filter the data at 1-Hz (for ICA, ASR, and CleanLine)
    Import channel info
    Remove line noise using CleanLine
    Apply clean_rawdata() only to reject bad channels.
    Interpolate all the removed channels
    Re-reference the data to average
    Apply clean_rawdata() only to perform Artifact Subspace Reconstruction (ASR).
    Re-reference the data to average again--this is to reset the data to be zero-sum across channels again.
    Run AMICA using calculated data rank with 'pcakeep' option (or runica() using 'pca' option)
    Estimate single equivalent current dipoles
    Search for and estimate symmetrically constrained bilateral dipoles """


import numpy as np
from scipy import signal 
from scipy.signal import lfilter
import matplotlib.pyplot as plt


#import the array of doubes, high pass cutoff, and samplerate
def preprocess_Makoto_PREP(arr, high_pass_cutoff=1.0, sampling_rate=100.0):

    plt.subplot(2, 1, 1)
    x  = np.tile(np.arange(1, 1001), (8, 1))
    plt.plot(x, arr, linewidth=2, linestyle="-", c="b")  # smooth by filter

    # Down-sample data? Only want to evaluate to 250Hz to remove unecessary data

    #High pass filter section
    b, a = signal.butter(N=4, Wn=high_pass_cutoff, btype='high', analog=False, output='ba')

    # Apply the high-pass filter
    filtered_arr = signal.filtfilt(b, a, arr)

    ##clean up line noise here
    n = 15  ##higher the n the smother the curve will be 
    b = [1.0/n] * n 
    noise_cleaned = lfilter(b,a,filtered_arr)


    ##common averaging stuff
    average_signal = np.mean(noise_cleaned,axis=1, keepdims=True)
    avg_final = noise_cleaned-average_signal



    Norm_array = (avg_final-np.min(avg_final)/np.max(avg_final)-np.min(avg_final))
    process_finalarr = np.sqrt(Norm_array)
    
    plt.subplot(2, 1, 2)
    plt.plot(x, process_finalarr, linewidth=2, linestyle="-", c="b")  # smooth by filter
    plt.tight_layout()
    plt.show()
    return process_finalarr


np.random.seed(42)

# Create a double array of random doubles
double_array = np.random.rand(8, 1000)
##double_array[1][1] = 2.4455
print(double_array)
finalaray1 = preprocess_Makoto_PREP(double_array)
print(finalaray1)

