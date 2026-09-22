# code courtesy of Adam Dempsey
# modified for PHY1055 by Oisín Creaner

# This file isn't a complete template, but rather gives an outline of what you need the function to do.
# If you're feeling ambitious, you can keep these functions in a separate file and import them.
# Look up how to do so for yourself, or experiment based on what you see in library imports

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


V = 10
R = 50
L = 100

def differential_rl(t, i):
    """
    Calculates the change in current over time from the formula
    L(dI/dt) = V - RI
    :param v: Float for voltage
    :param r:
    :param l/:
    :param i:
    :return:
    """
    dIdt = (V - R*i)/L
    
    return dIdt

    # complete the docstring
    # do some maths to calculate the difference
    # return the difference
    pass # this is a placeholder. Replace it with a return value


def exact_solution_rl(t):
    """
    Calculates the change in current over time from the formula
    I = (V/R)(1-exp(-Rt/L))
    :param v: Float for voltage
    :param r:
    :param l:
    :param t:
    :return:
    """
    
    Sol =  V/R*(1 - np.exp(-(R*t)/L))
    
    return Sol
    
    
    # complete the docstring
    # do some maths to calculate the exact solution at a given time
    # return the difference
     # this is a placeholder. Replace it with a return value

