#https://www.youtube.com/watch?v=twi_KN1mL_E&list=PLNmACol6lYY6vMIuE1Wspug9QYURHltOR&index=34
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
#This is necessary!

N = 64 # Number of points
T = 1/64 # Spacing between points
# if T is the time/distance, 1/T is the frequency /wavenumber

x = np.linspace(0, 2*np.pi*N*T, N)
# x is time, so 1/x is frequency
y1 = np.cos(20*x)
y2 = np.sin(10*x)
y3 = np.sin(5*x)

y = y1 + y2 + y3 # Produces a signal

fy = fft(y) # finds the fft
xf = np.linspace(0.0, 1.0/(2.0*T), int(N/2))

plt.figure(1)
plt.plot(x, y, 'r', linewidth=3, label="original signal")
plt.legend()
plt.show(block=False)

plt.figure(2)
plt.stem(xf, (2.0/N)*np.abs(fy[0:int(N/2)]), 'b', label="fft-signal")
plt.legend()
plt.show(block=False)

plt.figure(3)
y4 = ifft(fy)
plt.plot(x, y, 'r', linewidth=3, label="original signal")
plt.plot(x, np.real(y4), 'k--', label="fft-signal")
plt.legend()
plt.show(block=False)
