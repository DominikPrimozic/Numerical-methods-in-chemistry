# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:39:20 2024

@author: domin
"""

#No numoy :)


roots=dict()

import cmath


def check(root,roots):
    for r in roots.keys():
        if ((abs(root.real-r.real)<1e-6) and (abs(root.imag-r.imag)<1e-6)): return roots
    roots[round(root.real,6)+1j*round(root.imag,6)]=[]
    return roots






xmax=2
ymax=2
step=0.02

from math import tan,exp
def f(x):
    return cmath.sin(x)

def df(x):
    return cmath.cos(x)


def newton(x,f,df):

    for i in range(1000):
        xk=x-f(x)/df(x)
        if ((abs(xk.real-x.real)<1e-6) and (abs(xk.imag-x.imag)<1e-6)): return xk
        x=xk
    return None

def ranger(a,b,step):
    current=a
    while (current>=a and current<b):
        yield current
        current+=step
        
for i in ranger(-xmax,xmax,step):
    for j in ranger(-ymax,ymax,step):
        x=i
        y=j
        
        possible_root=newton(complex(x,y),f,df)
        if possible_root!=None:
            roots=check(possible_root,roots)
            
            roots[round(possible_root.real,6)+1j*round(possible_root.imag,6)].append((x,y))
            
        
import matplotlib.pyplot as plt

for key in roots.keys():
    x_plot=[]
    y_plot=[]
    for x,y in roots[key]:
        x_plot.append(x)
        y_plot.append(y)
    plt.plot(x_plot,y_plot,"o", markersize=1)        
                
        