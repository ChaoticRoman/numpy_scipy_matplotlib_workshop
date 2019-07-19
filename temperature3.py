import matplotlib.pyplot as plt

from load_data import load_data
from moving_average import moving_average

markersize = .1
N = 365

if __name__ == "__main__":
    header, dates, data = load_data()
    avgT, maxT, minT = data[:,0], data[:,1], data[:,2]

    plt.title("Roční a desetileté průměrné teploty z pražského Klementina")
    plt.plot(dates, moving_average(avgT, N), 'k', lw=.1)
    plt.plot(dates, moving_average(avgT, 10*N), 'r', lw=1)
    plt.grid()
    plt.ylabel("$\mathrm{T_{avg} [°C]}$")
    plt.show()
