import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from load_data import load_data
from moving_average import moving_average

N = 365

if __name__ == "__main__":
    _, dates, data = load_data()
    temperature = data[:,0]
    temperature_max = data[:,1]
    percipitation = data[:,3]

    first_year, last_year = dates[0].year, dates[-1].year

    x = range(first_year, last_year + 1)
    y = range(0, 365)

    dt2day_of_year = lambda dt: dt.timetuple().tm_yday

    result = np.empty((len(y), len(x)))
    for i, val in enumerate(percipitation):
        dt = dates[i]
        x_i = dt.year - first_year
        y_i = dt2day_of_year(dt) - 1
        if y_i < 365:
            result[y_i,x_i] = val

    result = np.log10(result)

    fig, ax = plt.subplots()
    im = ax.imshow(result, origin='lower', interpolation='none',
        cmap=cm.jet, #vmin=np.min(val), vmax=np.max(T),
        extent=[first_year, last_year, 1, 365],
        aspect="auto")

    plt.show()
