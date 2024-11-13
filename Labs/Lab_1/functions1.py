# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:46:52 2024

@author: domin
"""

def bisection(function, a : float, b : float, ep : float=1e-6):
    """
    Parameters
    ----------
    function : 
        DESCRIPTION.
    a : float
        left interval boundary
    b : float
        right interval boundary
    ep : float, optional
        tolerance. The default is 1e-6.

    Raises
    ------
    Exception
        raises exception if there is no odd zero on the interval

    Returns
    -------
    TYPE
        function performs bisection on given interval [a,b]

    """
    if (function(a)*function(b)>0): raise Exception("No zero")
    while abs(a-b)>ep:
        c=(a+b)/2;
        if (function(a)*function(c)<0):
            b=c;
        else:
            a=c;
    return (a+b)/2;

def secant(function, a : float, b : float, ep : float=1e-9):
    """
    secant method

    Parameters
    ----------
    function : TYPE
        function to perform secant method on
    a : float
        left interval boundary
    b : float
        right interval boundary
    ep : float, optional
        tolerance. The default is 1e-9.

    Raises
    ------
    Exception
        on [a,b] there is no zero

    Returns
    -------
    TYPE
        zero found on [a,b] with secant method 

    """
    if (function(a)*function(b)>0): raise Exception("No zero")
    c: float=a;
    while abs(function(c))>ep:
        c=a-function(a)*(b-a)/(function(b)-function(a));
        if (function(a)*function(c)<0):
            b=c;
        else:
            a=c;
    return c;

def tangent(function, df, x0 : float, ep : float=1e-9, h:float=1e-2):
    """
    Function uses numerical differentiation with central difference with step of 0.01
    Parameters
    ----------
    function : TYPE
        function to find zero of 
    df : 
        derivative of function
    x0 : float
       starting point for newton's method'
    ep : float, optional
        tolerance. The default is 1e-9.

    Returns
    -------
    TYPE
        zero of function found by Newton's mehod

    """
    norm=2*ep;
    while abs(norm)>ep:
        xk:float = x0 - function(x0)/df(x0)
        norm=xk-x0;
        x0=xk;
    return x0;

def plot(f,a,b,y1=-1,y2=1, n=100):
    import numpy as np
    import matplotlib.pyplot as plt
    x=np.linspace(a, b,100)
    plt.plot(x,f(x))
    plt.hlines(0,a,b, "orange")
    plt.ylim(y1,y2)
    plt.show()
    
def root_scan(f, df,a:float, b:float, step:float=0.1,ep:float=1e-6):
    """
    Uses Newton's method to find zeroes on a given interval

    Parameters
    ----------
    f : TYPE
        Function
    a : float
        Left bound
    b : float
        Right bound
    step : float, optional
        Step size. The default is 0.1.
    ep : float, optional
        Tolerance. The default is 1e-6.

    Returns
    -------
    roots : list
        List of roots.

    """
    
    
    roots=[]
    while a<=b:
        root=tangent(f,df, a,ep);
        is_simi=[True for x in roots if abs(x-root)<ep];
        if not any(is_simi):
            roots.append(root)
        a+=step;
    return roots
