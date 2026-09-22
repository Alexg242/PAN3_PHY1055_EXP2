# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:00:58 2026

@author: alexg
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from R6_excerpt import *

plt.rcParams['figure.dpi'] = 300


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))



def driven_pendulum(t, y, b=0.1, A=1, omega0=1, omegad=1):
    x, v = y
    dxdt = v
    dvdt = -b*v-(omega0**2)*x -A*np.sin(omegad*t)
    dydt = np.array([dxdt, dvdt])
    return dydt


def loop_through(omega, b, tf, y0):
    """
        THIS ISN'T REALLY A USABLE FUNCTION. IT'S INTENDED TO BE MERGED INTO YOUR REAL CODE

        This code plots the response for three different driving frequencies and displays
        the results on the same graph. It's important to note that the command plot(t,x)
        is placed within the loop.
    """
    x0 = 0# initial position
    v0 = 1# initial velocity
    y0 = (x0, v0)  # initial state
    t0 = 0  # initial time
    tf = 30*np.pi  # final time
    n = 1001  # Number of points at which output will be evaluated
    # creates an array of the time steps
    t = np.linspace(t0, tf, n)  # Points at which output will be evaluated

    # Loop through list of three driving frequencies (100%, 90%, 50% of omega0)
    for omegad in (omega, 0.9 * omega, 0.5 * omega):
       
        # Define the anonymous function, including the changing omegad
        lfun = lambda t, y,: driven_pendulum(t, y, b, omega, omegad)
        # Call the solver for this definition of lfun
        result = integrate.solve_ivp(fun=lfun,
                                     t_span=(0, tf),
                                     y0=y0,
                                     method="RK45",
                                     t_eval=t)
        # Store result of this run in variables t, x, v
        t = result.t
        x, v = result.y
        # Plot the result x(t) for this run, lable it with omegad as well
        ax1.plot(t, x, label='$x(t): \omega_d =${}'.format(omegad))
        ax2.plot(x, v)
    # End of loop, continue with next omegad
    # Out of the loop
    # Save and show plot
    ax1.legend()  # Make the plot labels visibl


loop_through(1, 0.1, 100*np.pi, (0, 1))

"""
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
    main()"""
 
    
ax1.legend()
ax1.set_xlabel("Time(s)")
ax1.set_ylabel("Amplitude(x)")
ax2.set_xlabel("v")
ax2.set_ylabel("x")
ax1.set_title("Multiple ")
ax2.set_title("x vs v")
ax2.axis("Equal")
fig.suptitle("R6: Driven Oscillator")

fig.show()  