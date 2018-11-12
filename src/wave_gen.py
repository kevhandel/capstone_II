import numpy as np
from scipy import fftpack
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
import pylab as pl

def function(omega, t, A):
    """Sinusoidal function."""
    # x = np.linspace(xmin,xmax,n)
    signal = np.sin(omega*t)
    rf = 2*np.abs(np.random.rand())
    signal += np.sin(omega*rf*t)
    noise = A*np.random.randn(t.size)
    # y = np.sin(2*np.pi*0.16*x)+np.sin(2*np.pi*0.70*x)+np.random.randn(x.size)/4.0
    return signal, noise

def fourier_transform(x,y):
    n = x.size #number of points
    dx = (max(x)-min(x))/n #discrete spatial step
    y_fft = scipy.fftpack.fft(y) #FFT algorithm
    x_fft = np.linspace(min(x),1.0/(2.0*dx),n/2) #scale x-axis
    y_fft = (2.0/n)*np.abs(y_fft[0:n//2]) #Take absolute value and scale
    return x_fft, y_fft


def fft_freqs_periods(x_fft, y_fft):
    """Print frequencies and periods."""
    bias = 0.03
    indices = argrelextrema(data=y_fft, comparator=lambda a,b:a>b+bias) #indices of local maxima from fft
    freqs = np.array([float('%.2f' % x_fft[i]) for i in indices[0]]) #f values at maxima
    T = np.array([float('%.2f' % (1.0/f)) for f in freqs]) #1/f values
    print("*--- Estimations ---*")
    for i in range(T.size):
            print("\nPeriod %s: %s" % (i+1, T[i]))
            print("Frequency %s: %s" % (i+1, freqs[i]))
    return freqs, T

def plot_simple(x, y, title='title'):
    fix, ax = plt.subplots(figsize=(5,3))
    ax.set_title(title)
    ax.scatter(x=x, y=y, marker='.', linewidths=1)
    ax.set_xlim(x[0], x.max())

def plot_both(x, y, title):
    t, freq = x
    y, Y = y
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(t,y)
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Amplitude')
    ax[0].set_title(title[0])
    ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
    ax[1].set_xlabel('Freq (Hz)')
    ax[1].set_ylabel('|Y(freq)|')
    ax[1].set_title(title[1])

def get_points(f, cycles, n):
    omega = 2*np.pi*f
    t_max = cycles/f
    t = np.linspace(0, t_max, n)
    return omega, t

def get_Y(y, n):
    Y = np.fft.fft(y)/n # fft computing and normalization
    Y = Y[range(int(n/2))]
    return Y

rate = 44000
ii = np.arange(0, 9218368)
t = ii / rate
n = 2048
Ts = 5
fs = np.random.randint(100, 20000, 5)
fmax = 2*fs.max()
fmin = fs.min()
#t = np.arange(0,Ts/fmin,Ts/fmin/n)
sig=0.
An = .1
for f in fs:
    A = np.random.random()
    # noise =
    sig += A*np.cos(2*np.pi*f*t) + An*np.random.random()
pl.plot(t, sig)
F = np.fft.fft(sig)/n
w = np.linspace(0,rate,len(F))
F_plot = F[0:len(F)//2]
w_plot = w[0:len(F)//2]
# pl.plot(w_plot,F_plot)
