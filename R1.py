# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:22:18 2026

@author: alexg
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

plt.rcParams['figure.dpi'] = 300

a = 1
b = 1

def nonlinear1(t,y):
    dydt = -y**3 + np.sin(t)
    return dydt

def main():
    y0 = np.array([0])
    t0 = 0  
    tf = 20  
    n = 101
    t = np.linspace(t0, tf, n)
    result = integrate.solve_ivp(fun=nonlinear1, 
                                 t_span=(t0, tf),  
                                 y0=y0, 
                                 method="RK45",  
                                 t_eval=t) 
    y = result.y[0]
    t = result.t

    plt.plot(t,y,'k.',label="Exact Values")
    plt.title("x Value vs Time")
    plt.ylabel("x Value (x)")
    plt.xlabel("Time (t)")
    plt.show()

if __name__ == '__main__':
    main()