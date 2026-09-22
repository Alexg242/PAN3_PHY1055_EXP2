# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:34:27 2026

@author: alexg
"""

from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 300


fig,(axs) = plt.subplots(1, 1)



def driven_pendulum(t, y, b=0.1, A=1, omega0=1, omegad=1):
    x, v = y
    dxdt = v
    dvdt = -b*v-(omega0**2)*x -A*np.sin(omegad*t)
    dydt = np.array([dxdt, dvdt])
    return dydt


def loop_through(omega, b, tf, y0, A):
    
    t0 = 0  # initial time
    n = 1001  # Number of points at which output will be evaluated



    damping_coefficients = [1, 0.9, 0.7, 0.5, 0.2]

    driving_frequencies = []
    
    omega = 1.
    a = 0
    while a < omega*2:
        driving_frequencies.append(a)
        a = a + 0.005
    
    
 
    t = np.linspace(t0, tf, n)  # Points at which output will be evaluated
        
    # Loop through list of three driving frequencies (100%, 90%, 50% of omega0)
    for b in damping_coefficients:
        amplitudes = [] # Clear list to store amplitudes needs to be done for each b

        # Second (inner) loop through driving freq. define earlier!
        for omegad in driving_frequencies:
            # Define the anonymous function, including the changing omegad
            lfun = lambda t, y, : driven_pendulum(t, y, b, A, omega, omegad)

            # Call the solver for this definition of lfun
            result = integrate.solve_ivp(fun=lfun,
                                         t_span=(0, tf),
                                         y0=y0,
                                         method="RK45",
                                         t_eval=t)
            # Store result of this run in variables t, x, v
            t = result.t
            v, x = result.y
            amplitudes.append((max(x)-min(x))/2)  # Find peak to peak amplitude
            # End of inner loop, continue with next omegad

        # Out of the inner loop
        # Save plot of amplitudes
        axs.plot(driving_frequencies, amplitudes, label=r"$v(t)$")
    # End of loop, continue with next om
    axs.legend()  # Make the plot labels visibl


loop_through(1, 0.1, 50, (0, 1), 1)
    
axs.set_xlabel("Time(s)")
axs.set_ylabel("Amplitude(x)")
fig.suptitle("R8: Resonance")

fig.show()  