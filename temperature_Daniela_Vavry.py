import sys

import matplotlib.pyplot as plt

from load_data import load_data
from moving_average import moving_average



def process_month():
    header, dates, data = load_data()
    avgT, maxT, minT = data[:,0], data[:,1], data[:,2]

    data = [(d.year, avgT[i]) for i, d in enumerate(dates) if d.month == 7]

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

    # https://www.chmi.cz/files/portal/docs/aktuality/2025/Klementinum_cervenec_2025.pdf
    x_DV = [2025]
    t_DV = [21.4]

    plt.title('Průměr červencových teplot')
    plt.plot(x, t, 'r.')
    plt.plot(x_DV, t_DV, 'b.')
    plt.ylabel("T [˚C]")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    process_month()
