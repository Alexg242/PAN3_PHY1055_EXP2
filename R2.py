# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:00:53 2026

@author: alexg
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from R2_function_outlines import *


def main():
    y0 = np.array([0])
    t0 = 0  
    tf = 20  
    n = 101
    t = np.linspace(t0, tf, n)
    result = integrate.solve_ivp(fun=differential_rl, 
                                 t_span=(t0, tf),  
                                 y0=y0, 
                                 method="RK45",  
                                 t_eval=t) 
    y = result.y[0]
    t = result.t

    plt.plot(t,y,'k.', markersize=5, label="Calulated Values")

    
timestep = 0.5 #change in t
max_time = 20 #tmax

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
    Ncurrent = exact_solution_rl(tcurrent)
    timet.append(tcurrent)
    quanityt.append(Ncurrent)
    tcurrent = tcurrent + timestep
    
plt.plot(timet, quanityt, "b-", label="Exact Values")    

if __name__ == '__main__':
    main()

plt.title("Current vs Time")
plt.ylabel("Current (I)")
plt.xlabel("Time (s)")    
plt.legend()
plt.show()#%%   

