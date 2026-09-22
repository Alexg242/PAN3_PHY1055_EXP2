# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:14:25 2026

@author: alexg
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:00:58 2026

@author: alexg
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

plt.rcParams['figure.dpi'] = 300


fig,(axs) = plt.subplots(1, 1)



def driven_pendulum(t, y, b=0.1, A=1, omega0=1, omegad=1):
    x, v = y
    dxdt = v
    dvdt = -b*v-(omega0**2)*x -A*np.sin(omegad*t)
    dydt = np.array([dxdt, dvdt])
    return dydt


def loop_through(tf, n, omega_0, b, y0, A):

    x0 = 0# initial position
    v0 = 1# initial velocity
    y0 = (x0, v0)  # initial state
    t0 = 0  # initial time
    tf = 30*np.pi  # final time
    n = 1001  # Number of points at which output will be evaluated
    amplitudes = []  # Create empty list to store amplitudes
    t = np.linspace(t0, tf, n)  # Points at which output will be evaluated
    
    driving_freq = np.linspace(0, 2*omega_0, 100)
    
    # Loop through list of three driving frequencies (100%, 90%, 50% of omega0)
    for omega_d in driving_freq:
        # Define the anonymous function, including the changing omegad
        lfun = lambda t, y, : driven_pendulum(t, y, b, A, omega_0, omega_d)
        # Call the solver for this definition of lfun
        result = integrate.solve_ivp(fun=lfun,
                                     t_span=(0, tf),
                                     y0=y0,
                                     method="RK45",
                                     t_eval=t)

        # Store result of this run in variables t, x, v
        t = result.t
        v, x = result.y

        amplitudes.append((max(x)-min(x))/2)  # F
        # Plot the result x(t) for this run, lable it with omegad as well
    plt.plot(driving_freq, amplitudes)
    # End of loop, continue with next omegad
    # Out of the loop
    # Save and show plot
    axs.legend()  # Make the plot labels visibl


loop_through(30*np.pi, 1001, 1, 0.1, (0, 1), 1)
    

fig.show()  