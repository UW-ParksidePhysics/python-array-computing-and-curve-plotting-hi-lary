# exercise 5.2
import numpy as np

x_values = np.linspace(-4, 4, 41)  # starting value, ending value, how many values
y_values = np.empty(len(x_values))  # empty array of 41 values


def h(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp((-1 / 2) * x ** 2)


for i,x in enumerate(x_values):  # the value of the array at index i
    # enumerate^ will assign new value below into the corresponding index
    y_values[i] = h(x)

print(x_values)
print(y_values)
