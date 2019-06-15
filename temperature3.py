import matplotlib.pyplot as plt

from load_data import load_data
from moving_average import moving_average

markersize = .1
N = 365

if __name__ == "__main__":
    header, dates, data = load_data()
    avgT, maxT, minT = data[:,0], data[:,1], data[:,2]
    plt.plot(dates, avgT, 'g.', markersize=markersize)

    plt.plot(dates, moving_average(avgT, N), 'g', lw=.1)
    plt.plot(dates, moving_average(avgT, 5*N), 'g', lw=.5)
    plt.plot(dates, moving_average(avgT, 10*N), 'g', lw=1)
    plt.plot(dates, moving_average(avgT, 25*N), 'g', lw=2.5)
    plt.plot(dates, moving_average(avgT, 50*N), 'g', lw=5)

    plt.show()
