from datetime import timedelta

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from load_data import load_data
from moving_average import moving_average

markersize = .1
N = 365

def plot_dates(dates, avgT, baseline=None, additional_curve=None):
    plt.figure()
    plt.grid()
    plt.ylabel("$\mathrm{T_{avg} [°C]}$")
    title = f"Roční a desetileté průměrné teploty z pražského Klementina\n{dates[0].year}-{dates[-1].year}"

    if baseline:
        plt.plot([dates[0], dates[-1]], 2 * [baseline], 'k--')
        title += f"\ndashed line = {baseline:.2f}°C"

    if additional_curve is not None:
        plt.plot(additional_curve[0] ,additional_curve[1], 'k-')

    plt.plot(dates, moving_average(avgT, N), 'k', lw=.1)
    plt.plot(dates, moving_average(avgT, 10*N), 'r', lw=1)

    plt.title(title)
    plt.show()

if __name__ == "__main__":
    header, dates, data = load_data()
    avgT = data[:,0]
    
    average_avgT = np.mean(avgT)
    plot_dates(dates, avgT, average_avgT)

    index_1850 = [i for i, d in enumerate(dates) if d.year >= 1850][0]
    dates_pre, dates_post = dates[:index_1850], dates[index_1850:]
    avgT_pre, avgT_post = avgT[:index_1850], avgT[index_1850:]

    average_avgT_pre, average_avgT_post = np.mean(avgT_pre), np.mean(avgT_post)

    plot_dates(dates_pre, avgT_pre, average_avgT_pre)
    plot_dates(dates_post, avgT_post, average_avgT_post)
    
    days_indices = np.array([i / 1e6 for i, _ in enumerate(dates_post)])
    exp_model = lambda i, A, B, C: A + B * np.exp(C * i)
    params, _ = curve_fit(exp_model, days_indices,  avgT_post)
    print(params)
    A, B, C = params

    avgT_exp_fit = exp_model(days_indices, A, B, C)
    plot_dates(dates_post, avgT_post, None, (dates_post, avgT_exp_fit))

    extra_years = 50
    last_available_day, day = dates_post[-1], timedelta(days = 1)
    extended_dates = np.array(
        list(dates_post) + [last_available_day + i*day for i in range(1, 365*extra_years)])

    extended_dates_indices = np.array([i / 1e6 for i, _ in enumerate(extended_dates)])
    extended_avgT_exp_fit = exp_model(extended_dates_indices, A, B, C)
    plot_dates(dates_post, avgT_post, None, (extended_dates, extended_avgT_exp_fit))
