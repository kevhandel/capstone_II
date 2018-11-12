import numpy as np
import matplotlib.pyplot as plt

def get_Y(y, n):
    Y = np.fft.fft(y)/n # fft computing and normalization
    Y = Y[range(int(n/2))]
    return Y

def plot_both(x, y):
    t, freq = x
    y, Y = y
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(t,y)
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Amplitude')
    ax[1].plot(freq,abs(Y),'r') # plotting the spectrum
    ax[1].set_xlabel('Freq (Hz)')
    ax[1].set_ylabel('|Y(freq)|')

Fs = 150.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0,1,Ts) # time vector

ff = 5;   # frequency of the signal
y = np.sin(2*np.pi*ff*t)

n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
freq = k/T # two sides frequency range
freq = freq[range(int(n/2))] # one side frequency range
freq = freq/Ts
Y = get_Y(y, n)
x = [t, freq]
y = [y, Y]
# plot_both(x, y)

N = 1000
t = np.arange(N)

m = 200
nu = float(m)/N
f = np.sin(2*np.pi*nu*t)
ft = np.fft.fft(f)
freq = np.fft.fftfreq(N)*N*N/m
plt.plot(freq, ft.real**2 + ft.imag**2)
plt.show()

#plot_url = py.plot_mpl(fig, filename='mpl-basic-fft')
