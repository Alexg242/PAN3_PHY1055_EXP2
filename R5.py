# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:40:58 2026

@author: alexg
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

plt.rcParams['figure.dpi'] = 300


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))


def damped_pendulum(t, y, b=0.1, omega0=1):
    x, v = y
    dxdt = v
    dvdt = -b*v-(omega0**2)*x
    dydt = np.array([dxdt, dvdt])
    return dydt

lfun = lambda t, y, : damped_pendulum(t, y, b=0.1, omega0=1)

print(lfun)

def main():
    # define the initial parameters
    x0 = 0# initial position
    v0 = 1# initial velocity
    y0 = (x0, v0)  # initial state
    t0 = 0  # initial time
    tf = 10*np.pi  # final time
    n = 1001  # Number of points at which output will be evaluated
    # creates an array of the time steps
    t = np.linspace(t0, tf, n)  # Points at which output will be evaluated

    # Calls the method integrate.solve_ivp()
    result = integrate.solve_ivp(fun=lfun,  # The function defining the derivative
                                 t_span=(t0, tf),  # Initial and final times
                                 y0=y0,  # Initial state
                                 method="RK45",  # Integration method
                                 t_eval=t)  # Time points for result to be defined at

    # Read the solution and time from the result array returned by Scipy
    x, v = result.y
    t = result.t

    # plot position ad velocity as a function of time.
    ax1.plot(t, x,"-" , label=r"$x(t)$")
    ax1.plot(t, v, label=r"$v(t)$")
    ax2.plot(v, x, "k-" )
    ax2.axis("Equal")


if __name__ == '__main__':
    main()
 
ax1.legend()
ax1.set_xlabel("Time(s)")
ax1.set_ylabel("Amplitude(x or v)")
ax2.set_xlabel("v")
ax2.set_ylabel("x")
ax1.set_title("x and v v time")
ax2.set_title("x vs v")
fig.suptitle("R3: Harmonic Oscillator")

fig.show()  