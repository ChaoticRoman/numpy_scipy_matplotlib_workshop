import numpy as np
import matplotlib.pyplot as plt

from load_data import load_data

from moving_average import moving_average
from fourier_filter import fourier_lowpass
from polyfit import polyfit

day_in_year = 365

if __name__ == "__main__":
    header, dates, data = load_data()
    avgT, maxT, minT = data[:,0], data[:,1], data[:,2]

    year_avgs = moving_average(avgT, day_in_year)

    avg = np.mean(avgT)
    line = polyfit(avgT, 1)
    quad = polyfit(avgT, 2)
    cube = polyfit(avgT, 3)

    for years in [1, 5, 10, 20]:
        days = years * day_in_year

        plt.figure()
        plt.title(f"{years} years")
        plt.grid()

        plt.plot(dates, year_avgs, "k.", ms=0.05)

        plt.plot([dates[0], dates[-1]], [avg, avg], 'k--')
        plt.plot(dates, line)
        plt.plot(dates, quad)
        plt.plot(dates, cube, 'k')

        plt.plot(dates, moving_average(avgT, days), 'r')
        plt.plot(dates, fourier_lowpass(avgT, days), 'g')
        plt.show()
