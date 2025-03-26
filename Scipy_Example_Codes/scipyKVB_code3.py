"""
==== Demonstration of Scipy (hanning window) filtering using a simulated blood pressure signal 
==== Source code written by Prof. Kartik Bulusu
==== CS and MAE Department, SEAS GWU
==== Description:
======== Imports data from a CSV file
======== Performs basic filtering
======== 
==== Requirements:
============ The program requires Python 3.10.6 dependent interpreter and plug-ins:
============ numpy, scipy, matplotlib and csv libraries
============ Companion Avg_Pressure_drop.csv file with average pressure drop data
======== It has been written exclusively for CS3907 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.
==== Testing:
==== 1. Developed on 03/30/2023 using Python 3.10.6 on Macbook Pro using Thonny IDE
==== 2. Modified on  using Python 3.10.6 on Macbook Pro using Thonny IDE
"""

import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import csv

T = []
data = []

with open('Avg_Pressure_drop.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        T.append(float(row[0]))
        data.append(float(row[1])+np.random.random(1)[0])

sampleRate = 1/(T[1]-T[0])

times = np.arange(len(data))/sampleRate

# apply a 3-pole lowpass filter at 0.1x Nyquist frequency
b, a = scipy.signal.butter(3, 0.1)
filtered = scipy.signal.filtfilt(b, a, data)

plt.figure(figsize=(10, 4))
plt.plot(data, '.-', alpha=.5, label="data")
plt.show(block=False)

# plot the original data next to the filtered data
plt.figure(figsize=(10, 4))

plt.subplot(121)
plt.plot(times, data)
plt.title("ECG Signal with Noise")
plt.margins(0, .05)

plt.subplot(122)
plt.plot(times, filtered)
plt.title("Filtered ECG Signal")
plt.margins(0, .05)

plt.tight_layout()
plt.show(block=False)


# create a normalized Hanning window
windowSize = 40
window = np.hanning(windowSize)
window = window / window.sum()

# filter the data using convolution
filtered = np.convolve(window, data, mode='valid')

plt.figure(figsize=(10, 4))

plt.subplot(131)
plt.plot(window)
plt.title("Window")
plt.margins(0, .05)

plt.subplot(132)
plt.plot(data)
plt.title("Data")
plt.margins(0, .05)

plt.subplot(133)
plt.plot(filtered)
plt.title("Filtered")
plt.margins(0, .05)

plt.tight_layout()
plt.show(block=False)