import numpy as np

def fourier_lowpass(data, period=365):
    L = len(data)
    fourier = np.fft.fft(data)

    f = int(L/period)
    fourier[f:L - f + 1] = 0

    inv = np.fft.ifft(fourier)

    return np.abs(inv)