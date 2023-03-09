# exercise 5.33
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

""" The goal is to not have any variables outside of the definition
statements so that if we need heatwave2.py in another py file,
variables are not redefined"""


# setting up constants and variables
def build_array():
    period1 = 365 * 24 * 60 * 60  # period 365 days to seconds
    period2 = 24 * 60 * 60  # period 24 hours to seconds
    delta_time = period2 / 10  # intervals of time given
    time_array = np.arange(0, period1 + 1, delta_time)
    depth_array = np.linspace(0, 20, len(time_array))  # need the same amount of intervals as time_array to plot
    return time_array, depth_array


# temperature as a function of depth z and time t
def temperature(z, t):
    k = 1E-6  # m^2/s thermal diffusivity
    amplitude1 = 15  # degrees celsius
    amplitude2 = 7  # degrees celsius
    period1 = 365 * 24 * 60 * 60  # period 365 days to seconds
    period2 = 24 * 60 * 60  # period 24 hours to seconds
    omega1 = 2 * np.pi / period1  # hz
    omega2 = 2 * np.pi / period2  # hz
    alpha1 = np.sqrt(omega1 / 2 * k)  # 1/m^2
    alpha2 = np.sqrt(omega2 / 2 * k)  # 1/m^2
    temp_initial = 0
    function = temp_initial + amplitude1 * np.exp(-alpha1 * z) * (np.sin(omega1 * t - alpha1 * z)) \
               + amplitude2 * np.exp(-alpha2 * z) * (np.sin(omega2 * t - alpha2 * z))
    return function


# frames = np.linspace(initial time, final time, intervals)
# def update(frames):
# def animate(final_time, delta_time, depth, function_array):
if __name__ == "__main__":
    print(temperature(build_array()[0], build_array()[1]))
