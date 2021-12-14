import numpy as np
from datetime import datetime as dt

KLEMENTINUM = "klementinum.csv"
MILESOVKA = "milesovka.csv"


def load_data(dataset=KLEMENTINUM):
    if dataset == KLEMENTINUM:
        return load_klementinum()
    if dataset == MILESOVKA:
        return load_milesovka()

def load_klementinum():
    fn = KLEMENTINUM
    with open(fn) as f:
        header = f.readline()
    header = [l.strip() for l in header.split(",")]

    data = np.genfromtxt(fn, delimiter=',', skip_header=1)

    L = data.shape[0]
    cols2date = lambda i: dt(*map(int, data[i, :3]))
    dates = np.array([cols2date(i) for i in range(L)])

    return header[3:7], dates, data[:, 3:7]


def load_milesovka():
    fn = MILESOVKA
    data = np.genfromtxt(fn, delimiter=',', skip_header=1)

    N_rows = data.shape[0]

    dates = []
    Tavg = []
    for i in range(N_rows):
        row = data[i]
        year = int(row[0])
        month = int(row[1])
        for day in range(1, 32):
            value = row[1 + day]
            if np.isnan(value):
                break
            d = dt(year, month, day)
            dates.append(d)
            Tavg.append(value)
            #print(f"{d} {value}")

    return np.array(dates), np.array(Tavg)


def view_array(x, n=3):
    L = x.shape[0]
    M = x.shape[1]
    print(f"{L}x{M}")
    [print(x[i]) for i in range(n)]
    print("...")
    [print(x[L-n+i]) for i in range(n)]


if __name__ == "__main__":
    header, dates, data = load_data()
    view_array(dates)
    print(header)
    view_array(data)
    print(dates.dtype, data.dtype)
