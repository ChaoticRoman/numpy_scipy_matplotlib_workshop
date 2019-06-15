import matplotlib.pyplot as plt

from load_data import load_data
from moving_average import moving_average

N = 365

if __name__ == "__main__":
    header, dates, data = load_data()
    srazky = data[:,3]
    plt.plot(dates, srazky, 'b.', markersize=.5)

    plt.plot(dates, moving_average(srazky, N), 'b', lw=1)

    plt.plot(dates, moving_average(srazky, 10*N), 'k', lw=1)

    plt.show()