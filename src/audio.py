
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def plot_both(x, y, title):
    t, freq = x
    y, Y = y
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(t,y)
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Amplitude')
    ax[0].set_title(title[0])
    ax[1].plot(freq,abs(Y),'r') # plotting the spectrum
    ax[1].set_xlabel('Freq (Hz)')
    ax[1].set_ylabel('|Y(freq)|')
    ax[1].set_title(title[1])

def plot_gauss():
    window = signal.gaussian(index, std=sigma)
    plt.plot(window)
    plt.title(f"Gaussian window ($\sigma$={sigma})")
    plt.ylabel("Amplitude")
    plt.xlabel("Sample")
    return window

def shrink(y, size=64):
    y = (y*64)//y.max()

def save_np(y, Y, fs):
    pass

# rate, aud_data = scipy.io.wavfile.read(file)
f_min, f_max, waves = 10000, 20000, 3
fs = np.random.randint(f_min, f_max, waves)
rate = 2*fs.max()
rate = 44000
samples = int(rate**(3/2))
ii = np.arange(0, samples)
t = ii / rate
aud_data = np.zeros(len(t))
tmax = 10./fs.min()
index = int(tmax/(samples/rate/len(t)))

An = 0.9
sig = 0.
for f in fs:
    A = np.random.random()
    noise = An*np.random.random(t.size)
    sig += A*np.sin(2*np.pi*f*t) + noise
mean = sig.mean()
sig -= mean

len_data = len(sig)

channel_1 = np.zeros(2**(int(np.ceil(np.log2(len_data)))))
channel_1[0:len_data] = sig

fourier = np.fft.fft(channel_1)
w = np.linspace(0, rate, len(fourier))

# First half is the real component, second half is imaginary
fourier_to_plot = fourier[0:len(fourier)//2]
w = w[0:len(fourier)//2]
f_scale = len(fourier)/rate
f_range = np.array([10000,20000])
w_range = (f_scale*f_range).astype(int)
jump=t.size//400
x_plot = [t[:index],w[w_range[0]:w_range[1]]]
y_plot = [sig[:index],fourier_to_plot[w_range[0]:w_range[1]]]
title=[f'{sorted(fs)}','FFT']
plot_both(x_plot, y_plot, title)
rookie_plot=f'../figs/rookie_{waves}.png'
plt.savefig(rookie_plot)
#  plt.show()
square = 2**10 ## **10 = 1024
sig_pic = sig[:index]
sig_pic += abs(sig_pic.min())
sig_pic = square*(sig_pic//(sig_pic.max()))
sigma = sig_pic.size/square
#window = plot_gauss()
