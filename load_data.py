import numpy as np
from datetime import datetime as dt

fn = "klementinum.csv"


def load_data():
    with open(fn) as f:
        header = f.readline()
    header = [l.strip() for l in header.split(",")]

    data = np.genfromtxt(fn, delimiter=',', skip_header=1)

    L = data.shape[0]
    cols2date = lambda i: dt(*map(int, data[i, :3]))
    dates = np.array([cols2date(i) for i in range(L)])

    return header[3:7], dates, data[:, 3:7]


def view_array(x, n=3):
    L = x.shape[0]
    [print(x[i]) for i in range(n)]
    print("...")
    [print(x[L-n+i]) for i in range(n)]


if __name__ == "__main__":
    header, dates, data = load_data()
    view_array(dates)
    print(header)
    view_array(data)
    print(dates.dtype, data.dtype)