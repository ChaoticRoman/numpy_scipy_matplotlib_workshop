import matplotlib.pyplot as plt

from load_data import load_data

markersize = 1

if __name__ == "__main__":
    header, dates, data = load_data()
    plt.plot(dates, data[:,0], 'g.', markersize=markersize)
    plt.plot(dates, data[:,1], 'r.', markersize=markersize)
    plt.plot(dates, data[:,2], 'b.', markersize=markersize)
    plt.show()