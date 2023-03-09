# exercise 5.9
import numpy as np
import matplotlib.pyplot as plt

vi = 10  # initial velocity m/s
g = 9.81  # acceleration due to gravity m/s/s
t_values = np.linspace(0, 2 * vi / g, 50)  # starting value, ending value, how many values
y_values = np.empty(len(t_values))  # empty array of 50 values


def y(t):
    return (vi * t) - (1 / 2 * (g * t ** 2))


for i, t in enumerate(t_values):  # the value of the array at index i
    # enumerate^ will assign new value below into the corresponding index
    y_values[i] = y(t)

plt.plot(t_values, y_values, color='pink', label='y(t)')
plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.show()
