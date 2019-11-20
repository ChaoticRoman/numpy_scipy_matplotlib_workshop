﻿import matplotlib.pyplot as plt

from load_data import load_data
from moving_average import moving_average

if __name__ == "__main__":
    header, dates, data = load_data()
    avgT, maxT, minT = data[:,0], data[:,1], data[:,2]

    data = [(d.year, avgT[i]) for i, d in enumerate(dates)]

    year2temps = dict()

    for y, t in data:
        if y in year2temps:
            year2temps[y].append(t)
        else:
            year2temps[y] = [t]

    x, t = [], []
    for y in year2temps:
        x.append(y)
        temps = year2temps[y]
        t.append(sum(temps)/len(temps))

    plt.plot(x, t, 'ro')
    plt.plot(x, moving_average(t, 10), 'k')
    plt.grid()
    plt.show()