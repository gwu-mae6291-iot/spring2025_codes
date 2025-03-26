# Program to try and work out the power spectrum
# https://github.com/arunprasaad2711/Python_IISC_SIAM_2017/blob/master/Programs_Session3/06_FFT_IFFT_example.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft

n = 1024 # Number of points
Lx = 100
# Distance in meters or time period (in seconds)
omg = 2.0*np.pi/Lx
# Spacing between points
# if T is the time/distance, 1/T is the frequency /wavenumber

x = np.linspace(0, Lx, n)
y1 = 1.0*np.cos( 5.0*omg*x)
y2 = 1.0*np.sin(10.0*omg*x)
y3 = 0.5*np.sin(20.0*omg*x)

y = y1 + y2 + y3
act = y1 + y2

yd_true = (omg)*( -5.0*1.0*np.sin(5.0*omg*x) + 10.0*1.0*np.cos(10.0*omg*x) + 20.0*0.5*np.cos(20.0*omg*x))

mean_y = np.mean(y)
std_y = np.std(y)
var_y = std_y**2.0

print(mean_y, std_y, var_y)

# Creates all the necessary frequencies
freqs = fftfreq(n)

# # Arranges the frequencies in ascending order
# idx = np.argsort(freqs)

# wave numbers
nwaves = freqs*n
# nwaves_2pi = omg*nwaves

# mask array to be used for power spectra.
# ignoring half the values, as they are complex conjucates of the other
mask = freqs > 0

# fft values
fft_vals = fft(y)
xf = np.linspace(0.0, n/2, int(n/2))


# Fourier filtering
fft_new = np.copy(fft_vals)
fft_new[np.abs(nwaves)==20] = 0.0

# inverse fourier transform to reconstruct the filtered data
filt_data = np.real(ifft(fft_new))

# # derivative of y in frequency spectrum
# yd_fft = 1.0j*nwaves_2pi*fft_vals
# yd_recon = np.real(ifft(yd_fft))

# # this is the power spectra
# ps = 2.0*np.abs(fft_vals/n)**2.0

# # power by variance
# pow_var = ps/var_y*100.0
# 
# # freq.power spectra - for variance preserving form
# fps = ps*freqs

# #print(fft_vals)
# #print(np.abs(fft_vals*2.0/n))
# print(np.sum(ps[mask]))

plt.figure(1)
plt.title('Original Signal')
plt.plot(x, y, color='xkcd:salmon', label='original')
plt.legend()
plt.show(block=False)


plt.figure(2)
plt.stem(xf[0:50], (2.0/n)*np.abs(fft_vals[0:int(50)]), label="frequency specturm")
plt.legend()
plt.show(block=False)

# plt.figure(2)
# plt.plot(nwaves[mask], ps[mask], label='wavenumber vs spectra')
# plt.title('Power Spectrum Example - wavenumber vs spectra')
# plt.legend()

plt.figure(3)
plt.title('Data Filtering example')
plt.plot(x, act, color='black', label='theoretical')
plt.plot(x, filt_data, color='cyan', label='via fourier filtering')
plt.legend()
plt.show(block=False)

# plt.figure(4)
# plt.title('Derivative of the signal')
# plt.plot(x, yd_true, color='black', label='theoretical')
# plt.plot(x, yd_recon, color='cyan', label='via spectral method')
# plt.legend()
# plt.show()
