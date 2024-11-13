# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:50:57 2024

@author: domin
"""
import numpy as np
import plotly.graph_objects as go

def bisection(function, a : float, b : float, ep : float=1e-8):
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
    return c;
        


def tangent_root_scan(f, a:float, b:float, step:float=0.1,ep:float=1e-6, df=0):
    roots=[]
    while a<=b:
        root=tangent(f, a,ep, df=df);
        is_simi=[True for x in roots if abs(x-root)<ep];
        if not any(is_simi):
            roots.append(root)
        a+=step;
    return roots


def secant(function, a : float, b : float, ep : float=1e-9, *args):
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
    if (function(a,*args)*function(b,*args)>0): raise Exception("No zero")
    c: float=a;
    while abs(function(c,*args))>ep:
        c=a-function(a,*args)*(b-a)/(function(b,*args)-function(a,*args));
        if (function(a,*args)*function(c,*args)<0):
            b=c;
        else:
            a=c;
    return c;



def plot(function, x_range, n=1000, *args):
    x=np.linspace(x_range[0],x_range[1],n)
    y=function(x, *args)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='f(x)', line=dict(color='blue')))

    # Add the horizontal line at y=0
    fig.add_trace(go.Scatter(x=[x_range[0],x_range[1]], y=[0, 0], mode='lines', name='y=0', line=dict(color='orange', dash='dash')))
    fig.update_layout(
    xaxis_title="x",
    yaxis_title="f(x)",
    )
    fig.show("browser")
    
    
def tangent(function, df, x0 , ep : float=1e-6):
    """
    Function uses numerical differentiation with central difference with step of 0.01
    Parameters
    ----------
    function : TYPE
        function to find zero of 
    x0 :
       starting point for newton's method'
    ep : float, optional
        tolerance. The default is 1e-9.

    Returns
    -------
    TYPE
        zero of function found by Newton's mehod

    """
    df=df if df!=None else lambda x:(function(x+0.01)-function(x-0.01))/0.02
    norm=2*ep;
    while abs(norm)>ep:
        xk:float = x0 - function(x0)/df(x0)
        norm=abs(xk-x0);
        x0=xk;
    return x0;

def bisection_root_scan(f,a,b,step):
    roots=[]
    while a<b:
        if f(a)*f(a+step)<0:
            root=bisection(f, a, a+step)
            is_simi=[True for x in roots if abs(x-root)<1e-6];
            if not any(is_simi):
                roots.append(root)
        a+=step
        
    return roots
    
def tangent_complex_root_scan(f,df, a:list, b:list, step:list=[0.1,0.1],ep:float=1e-6):
    roots=[]
    x0=a[0];x1=a[1];y0=b[0];y1=b[1]
    Nr=int((x1-x0)/step[0]) +1
    Ni=int((y1-y0)/step[1]) +1
    for ix in range(Nr):
        for iy in range(Ni):
            root=tangent(f, df, complex(x0+step[0]*ix,y0+step[1]*iy))
            is_simi = [(abs(x.real - root.real) < 1e-4 and abs(x.imag - root.imag) < 1e-4) for x in roots]
            if not any(is_simi):
                roots.append(root)
    return roots    
    
    
    
    
    
    
    
    
    
    
    
    
    