# Program to try and work out the power spectrum
# https://github.com/arunprasaad2711/Python_IISC_SIAM_2017/blob/master/Programs_Session3/06_FFT_IFFT_example.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftfreq

N = 512 # Number of points
T = 1/512 # Spacing between points
# if T is the time/distance, 1/T is the frequency /wavenumber

x = np.linspace(0, 2*np.pi*N*T, N)
# x is time, so 1/x is frequency
y1 = np.cos(20*x)
y2 = np.sin(10*x)
y3 = np.sin(5*x)

y = y1 + y2 + y3 # Produces a signal

mean_y = np.mean(y)
std_y = np.std(y)
var_y = std_y**2.0

print(mean_y, std_y, var_y)

plt.figure(1)
plt.title('Original Signal')
plt.plot(x, y, color='xkcd:salmon', label='original')
plt.legend()
plt.show(block=False)


fy = fft(y) # finds the fft
xf = np.linspace(0.0, 1.0/(2.0*T), int(N/2))

plt.figure(2)
plt.stem(xf[0:50], (2.0/N)*np.abs(fy[0:int(50)]), label="frequency specturm")
plt.legend()
plt.show(block=False)

plt.figure(3)
y4 = ifft(fy)
plt.plot(x, np.real(y4), 'b', label="inverse Fourier")
plt.legend()
plt.show(block=False)

act = y1 + y2
# Creates all the necessary data after taking out y3

plt.figure(4)
plt.plot(x, act, color='black', label='theoretically filtered')
plt.legend()
plt.show(block=False)

fy_act = fft(act) # finds the fft
xf = np.linspace(0.0, 1.0/(2.0*T), int(N/2))

plt.figure(5)
plt.plot(xf[0:50], (2.0/N)*np.abs(fy_act[0:int(50)]), label="frequency specturm")
plt.legend()
plt.show(block=False)


freqs = fftfreq(N)
# wave numbers
nwaves = freqs*N

# fft values
fft_vals = fft(y)

# Fourier filtering of 5 Hz signal
fft_new = np.copy(fft_vals)
fft_new[np.abs(nwaves)==5] = 0.0

# inverse fourier transform to reconstruct the filtered data
filt_data = np.real(ifft(fft_new))


plt.figure(6)
plt.plot(x, filt_data, color='green', linestyle='dashed', label='via Fourier filtering')
plt.legend()
plt.show(block=False)


plt.figure(7)
plt.title('Data Filtering example')
plt.plot(x, act, color='black', label='theoretical')
plt.plot(x, filt_data, color='green', linestyle='dashed', label='via fourier filtering')
plt.legend()
plt.show(block=False)



