# exercise 5.3
import numpy as np
from math import sqrt, pi, exp

x_values_array = np.linspace(-4, 4, 41)  # starting value, ending value, how many values
x_array = np.empty(41)
y_array = np.empty(41)
for x in x_values_array:
    x_array.append(x)
    h = (1 / sqrt(2 * pi)) * exp((-1 / 2) * x ** 2)
print(x_array)
