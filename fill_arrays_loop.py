# exercise 5.2
import numpy as np
from math import sqrt, pi, exp

x_values_array = np.linspace(-4, 4, 41)  # starting value, ending value, how many values


for x in x_values_array:
    h = (1 / sqrt(2 * pi)) * exp((-1 / 2) * x ** 2)
    x_array = np.array(x_values_array)
    y_array = np.array(h)
    #x_array.append(x)
    #y_array.append(h)
print(x_array)
print(y_array)
