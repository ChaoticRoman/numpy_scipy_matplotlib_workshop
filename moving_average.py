import numpy as np

def moving_average(x, n, centered=True):
    # prepare input
    x = np.array(x, dtype=np.float64)
    L = len(x)
    assert L >= n

    # prepare output variable
    result = np.zeros_like(x)
    result[:n-1] = np.nan

    # moving average:
    result[n-1:] = sum([x[n-i-1:L-i] for i in range(n)]) / n

    if centered:
        result = np.hstack((result[n//2:], result[:n//2]))

    return result

if __name__ == "__main__":
    print(moving_average([1, 2, 3], 1))
    print(moving_average([1, 2, 3], 2))
    print(moving_average([1, 2, 3], 3))
    try:
        print(moving_average([1, 2, 3], 4))
    except AssertionError:
        print("Rightly failed...")