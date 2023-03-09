# exercise 5.4
import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(-4, 4)   # starting value, ending value, how many values
y_values = np.empty(len(x_values))  # empty array of 41 values


def h(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp((-1 / 2) * x ** 2)


for i, x in enumerate(x_values):  # the value of the array at index i
    # enumerate^ will assign new value below into the corresponding index
    y_values[i] = h(x)

plt.plot(x_values, y_values, color='yellow', label='h(x)')
plt.xlabel('x values')
plt.ylabel('h(x)')
plt.show()
