import matplotlib.pyplot as plt

from load_data import load_data
from moving_average import moving_average

markersize = .1
N = 365

if __name__ == "__main__":
    header, dates, data = load_data()
    avgT, maxT, minT = data[:,0], data[:,1], data[:,2]

    plt.plot(dates, maxT, 'r.', markersize=markersize)
    plt.plot(dates, minT, 'b.', markersize=markersize)
    plt.plot(dates, avgT, 'g.', markersize=2*markersize)

    plt.plot(dates, moving_average(avgT, 7), 'b', lw=.1)
    plt.plot(dates, moving_average(minT, N), 'b.')
    
    plt.grid()
    plt.show()