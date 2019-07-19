import numpy as np

def polyfit(y, deg=1):
    x = np.arange(len(y))
    coef = np.polyfit(x, y, deg)
    
    result = np.zeros_like(y)
    x_power = np.ones_like(y)

    for c in coef[::-1]:
        result += c * x_power
        x_power *= x

    return result