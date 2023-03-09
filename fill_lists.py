# exercise 5.1
from math import pi, exp, sqrt
import numpy as np

x_values_array = np.linspace(-4, 4, 41)  # starting value, ending value, how many values
xlist = []
hlist = []

for x in x_values_array:
    xlist.append(x)
    h = (1 / sqrt(2 * pi)) * exp((-1 / 2) * x ** 2)
    hlist.append(h)
    print(f'{x}, {h}')
# ^prints values of x and h side by side for all x in x_values_array. more readable than printing xlist and hlist
