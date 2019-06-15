import matplotlib.pyplot as plt

from load_data import load_data

if __name__ == "__main__":
    header, dates, data = load_data()
    plt.plot(dates, data[:,0], 'g.')
    plt.plot(dates, data[:,1], 'r.')
    plt.plot(dates, data[:,2], 'b.')
    plt.show()