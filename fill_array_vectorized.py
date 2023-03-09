# exercise 5.3
import numpy as np

x_values = np.linspace(-4, 4, 41)  # starting value, ending value, how many values


def h(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp((-1 / 2) * x ** 2)


y_values = h(x_values)

print(x_values)
print(y_values)
