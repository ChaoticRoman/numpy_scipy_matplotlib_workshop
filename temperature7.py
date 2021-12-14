import numpy as np
import matplotlib.pyplot as plt

from load_data import load_data
from moving_average import moving_average

markersize = .1
N = 365

if __name__ == "__main__":
    plt.suptitle(
        "Roční a desetileté průměrné teplot\n"
        "Data: ČHMÚ, Zpracování: Roman Pavelka")
    plt.ylabel("$\mathrm{T_{avg} [°C]}$")

    # Klementinum
    header, dates, data = load_data()
    avgT, maxT, minT = data[:,0], data[:,1], data[:,2]
    plt.plot(dates, moving_average(avgT, N), 'r', lw=.1)
    plt.plot(dates, moving_average(avgT, 10*N), 'r', lw=1, label="Klementinum")

    avg = np.mean(avgT)
    plt.plot([dates[0], dates[-1]], [avg, avg], 'r--', lw=.8)

    # Milesovka
    dates_m, avgT_m = load_data("milesovka.csv")
    plt.plot(dates_m, moving_average(avgT_m, N), 'b', lw=.1)
    plt.plot(dates_m, moving_average(avgT_m, 10*N), 'b', lw=1, label="Milešovka")

    avg_m = np.mean(avgT_m)
    plt.plot([dates_m[0], dates_m[-1]], [avg_m, avg_m], 'b--', lw=.8)

    plt.legend()
    plt.grid()
    plt.show()
