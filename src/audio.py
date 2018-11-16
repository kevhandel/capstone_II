
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imsave
from scipy import signal as sg
import cv2

def sine(f, t):
    return np.sin(2*np.pi*f*t)

def sawtooth(f, t):
    return sg.sawtooth(2*np.pi*f*t)

def square(f, t):
    return sg.square(2*np.pi*f*t)

def create_raw(waveforms, fs):
    for wave in waveforms:
        sig = 0.
        wave_name = wave.__name__
        for f in fs:
            A = np.random.random()
            noise = An*np.random.random(t.size)
            sig += wave(f,t) + noise
        sig -= sig.mean()
        wave_all[wave_name] = sig
    return wave_all

def transform(wave_all, rate, sq):
    pics = {}
    for wave_name in wave_all.keys():
        print('sig: ',wave_name)
        sig = wave_all[wave_name]
        w, fourier = FFT(sig, rate) ## First half is the real component, second half is imaginary
        Zpic = getZ(w, fourier, f_range, rate, sq)
        Zpic = normalize_pic(Zpic, sq)
        pic = create_2D_pic(Zpic, sq)
        pics[wave_name] = pic
    return pics

def FFT(signal, rate):
    sig = signal
    len_data = len(sig)
    channel_1 = np.zeros(2**(int(np.ceil(np.log2(len_data)))))
    channel_1[0:len_data] = sig
    fourier = np.fft.fft(channel_1)
    w = np.linspace(0, rate, len(fourier))
    return w, fourier

def getZ(w, f, f_range, rate, sq):  ## preps the FT data for image generation
    half = len(f)//2
    fourier_to_plot = f[0:half]
    w = w[0:half]
    f_scale = len(f)/rate
    w_range = (f_scale*f_range).astype(int)
    Y_np = abs(fourier_to_plot[w_range[0]:w_range[1]])
    Y_np = np.asarray(Y_np/Y_np.max()*sq)
    window_size = Y_np.size//sq
    drop = Y_np.size%window_size
    Z = Y_np.reshape(Y_np.size,1)[:-drop]
    Zpic = condense_pic(Z,window_size,1)
    return Zpic

def condense_pic(a, r, c):  ## average r rows for a 2D array a with c columns
    z = a.transpose().reshape(-1,r).sum(1).reshape(c,-1).transpose()
    z = z - z.min() ## zero out the image
    return z

def normalize_pic(z, sq):
     return (z/z.max()*sq).astype(int)

def create_2D_pic(z, sq):
    pic = np.zeros((sq,1))
    for x in z.ravel():
        each = np.hstack((np.zeros((sq-x)), np.ones((x)))).reshape(sq,1)  ## create columns
        pic = np.hstack((pic,each))  ## stack columns horizontally
    return np.delete(pic,0,1)  ## lose the initial zeros column

def save_figs(pics, waves, sq, fs):
    x = np.random.randint(1000, 9999)
    print(x)
    for wave_name in wave_all.keys():
        pic = pics[wave_name]
        imsave(f'../figs/{wave_name}/{wave_name}_{fs[0]}_{x}_{sq}.png', pic)

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
    return fig

def plot_gauss():
    window = signal.gaussian(index, std=sigma)
    plt.plot(window)
    plt.title(f"Gaussian window ($\sigma$={sigma})")
    plt.ylabel("Amplitude")
    plt.xlabel("Sample")
    return window

def shrink(y, size=64):
    y = (y*64)//y.max()

f_min, f_max, waves = 1000, 5000, 1
power = 6 ## 2^6 = 64;  2^10 = 1024
sq = 2**power
An = 2.  ## Amplitude of noise
sig = 0.
waveforms = [square, sawtooth]
wave_all = {}

repeat = 10  ## num of samples to create
for i in range(repeat):
    print(f'{i} of {repeat}')
    fs = np.random.randint(f_min, f_max, waves)
    rate = 2*fs.max()  ## generalize/play around with sampling rate
    rate = 44000
    samples = int(rate**(3/2))
    ii = np.arange(0, samples)  ## index for the samples
    t = ii / rate
    tmax = 10./fs.min() ## Periods/f_min; max time for plotting
    index = int(tmax/(samples/rate/len(t)))
    f_range = np.array([8000,22000])  ## plotting f range

    wave_all = create_raw(waveforms, fs)
    pics = transform(wave_all, rate, sq)
    save_figs(pics, waves, sq, fs)  ## save the generated FT images

def get_small_x_raw(f, rate, Ts):
    high_index = int(Ts/f*rate)
    high_time = Ts/f
    x = np.round(np.linspace(0, x, high_index),1)
    return x
    # wave_plot =
    # x_np_sq = np.linspace(f_range[0], f_range[1], sq).astype(int)
    # x_np_plot = [t[:index],x_np_sq]
    # y_np_plot = [sig[:index],Zpic.ravel()]
    #
    # title=[f'{sorted(fs)}','FFT']
    # plot_both(x_np_plot, y_np_plot, title)
    # rookie_plot=f'../figs/{waves}_{wave_name}_raw.png'
    # print(rookie_plot)
    # plt.savefig(rookie_plot)
    # plt.show()
plt.close('all')
# sig_pic = sig[:index]
# sig_pic += abs(sig_pic.min())
# sig_pic = sq*(sig_pic//(sig_pic.max()))
# sigma = sig_pic.size/sq
# window = plot_gauss()
