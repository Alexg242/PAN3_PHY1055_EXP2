# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:07:31 2026

@author: alexg
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

plt.rcParams['figure.dpi'] = 300


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))


def simple_pendulum(t, y):
    x, v = y  # extracts the x and v values from the tuple
    dydt = np.array([v, -x])  # generates an array with the rates of change: dxdt = v, dvdt = -x
    return dydt  # returns the array


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
    result = integrate.solve_ivp(fun=simple_pendulum,  # The function defining the derivative
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





"""
timestep = 0.01 #change in t
max_time = 10*np.pi #tmax

time0 = 0 ##t
quantity0 = 0 ## N0
    
timet = []
quanityt = []

timet.append(time0)
quanityt.append(quantity0)

tcurrent = time0
Ncurrent = quantity0
    
while tcurrent <= max_time:
    ##Ncurrent = V/R*(1 - np.exp(-(R*tcurrent)/L))
    Ncurrent = np.sin(tcurrent)
    timet.append(tcurrent)
    quanityt.append(Ncurrent)
    tcurrent = tcurrent + timestep
    

ax1.plot(timet, quanityt, "k", label="Sin(x)")   
"""

if __name__ == '__main__':
    main()
 
ax1.legend(loc=8)
ax1.set_xlabel("Time(s)")
ax1.set_ylabel("Amplitude(x or v)")
ax2.set_xlabel("v")
ax2.set_ylabel("x")
ax1.set_title("x and v v time")
ax2.set_title("x vs v")
fig.suptitle("R3: Harmonic Oscillator")

fig.show()  