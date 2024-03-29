import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

from load_data import load_data
from moving_average import moving_average

N = 365

if __name__ == "__main__":
    _, dates, data = load_data()
    temperature = data[:,1]

    dt2day_of_year = lambda dt: dt.timetuple().tm_yday

    pairs = list(zip(dates, temperature))

    condition = lambda t: t > 30

    x = [dt.year for (dt, t) in pairs if condition(t)]
    y = [dt2day_of_year(dt) for (dt, t) in pairs if condition(t)]
    temperature = [t for t in temperature if condition(t)]
    print(len(x), len(y), len(temperature))

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x, y, temperature, 'r.', ms=2)
    plt.show()
