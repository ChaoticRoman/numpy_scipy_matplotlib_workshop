import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

from load_data import load_data
from moving_average import moving_average

N = 365

if __name__ == "__main__":
    _, dates, data = load_data()
    temperature = data[:,0]

    dt2day_of_year = lambda dt: dt.timetuple().tm_yday

    x = [dt.year for dt in dates]
    y = [dt2day_of_year(dt) for dt in dates]

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x, y, temperature, 'k.')
    plt.show()
