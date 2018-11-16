import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sg

def sine(f, t):
    return np.sin(2*np.pi*f*t)

def sawtooth(f, t):
    return sg.sawtooth(2*np.pi*f*t)

def square(f, t):
    return sg.square(2*np.pi*f*t)

    Fs = 200.0  # sampling rate
Fs = 2000000
Ts = 1.0/Fs # sampling interval
t = np.arange(0,.0005,Ts) # time vector

ff = 14000   # frequency of the signal
fff = 15000
A = 1.
noise = np.random.random(t.size)
y =  np.sin(2*np.pi*ff*t) + .5*np.sin(2*np.pi*fff*t)
# y = sawtooth(ff, t)
y = square(ff, t)
y += A*noise
#y = y[::10]
n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(n//2)] # one side frequency range

Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(n//2)]

fig, ax = plt.subplots(2, 1)
ax[0].plot(t[::10],y[::10])
ax[0].set_xlabel('time (sec)')
ax[0].set_ylabel('Amplitude')
ax[0].set_title(f'Amplitude vs Time (w/ noise)')
ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
ax[1].set_title(f'Amplitude vs Frequency')
#ax[1].set_xscale("log", nonposx='clip')
ax[1].set_xlim(left=0, right=500000)
plt.tight_layout()
