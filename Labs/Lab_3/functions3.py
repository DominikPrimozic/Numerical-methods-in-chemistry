# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 08:02:52 2024

@author: domin
"""

def trapez_integration(f,a:float,b:float,N:int, *args):
    S=f(a,*args)+f(b,*args)
    interval=(b-a)/(N-1)
    for i in range(1,N-1):
        S+=2*f(a+i*interval,*args)
    return S*interval/2

def simpson_integration(f,a:float,b:float,N:int, *args):
    if N%2==0: raise Exception("Must have odd number of points")
    S=f(a,*args)+f(b,*args)
    interval=(b-a)/(N-1)
    for i in range(1,N-1):
        if (i%2==1):
            S+=4*f(a+i*interval,*args)
        else:
            S+=2*f(a+i*interval,*args)
    return S*interval/3

def monte_carlo_integration(f,a:list,b:list,N:int,*args):
    import random
    
    hit=0    
    for i in range(N):
        x=[]
        for xi in range(len(a)):
            x.append(random.uniform(a[xi],b[xi]))
        print(x)
        if (x[-1] <f(*x[:-1],*args)):
            hit+=1
    volume=1
    for i in range(len(a)):
        volume*=(b[i]-a[i])
    return hit/N * volume

def monte_carlo_integration_visual(f,a:list,b:list,N:int,*args): 
    import random
    import matplotlib.pyplot as plt
    import numpy as np
    
    hit=0    
    hit_points=[]
    unhit_points=[]
    for i in range(N):
        x=[]
        for xi in range(len(a)):
            x.append(random.uniform(a[xi],b[xi]))
        if (x[-1] <f(*x[:-1])):
            hit+=1
            hit_points.append(x)
        else:
            unhit_points.append(x)
    volume=1
    for i in range(len(a)):
        volume*=(b[i]-a[i])
        
    
    hits=np.array(hit_points)
    unhits=np.array(unhit_points)
    plt.plot(hits[:,0],hits[:,1],"o",c="orange")
    plt.plot(unhits[:,0],unhits[:,1],"o",c="pink")
    plt.show()
    return hit/N * volume

def riemann_integration(f,a:list,b:list,N:int,ty=0,*args):
    #ty is [-1,0,1] for left mid right, not error proof cause ehh
    interval=(b-a)/(N-1)
    fx=0
    integral=0
    for i in range(N-1): #i think lol
        dx=interval
        match ty:
            case -1:
                fx=f(a+i*interval)
            case 0:
                fx=f(a+(i+0.5)*interval)
            case 1:
                fx=f(a+(i+1)*interval)
            case _:
                raise Exception("fuck you")
        
        integral+=dx*fx
    return integral
        



def monte_carlo_sphere(f,a:list,b:list,N:int,*args): #i hate it, i dont want to change the other one for complex because of the roots
    import random
    hit=0    
    for i in range(N):
        x=[]
        for xi in range(len(a)):
            x.append(random.uniform(a[xi],b[xi]))
        
        if (f(*x,*args)):
            hit+=1
    volume=1
    for i in range(len(a)):
        volume*=(b[i]-a[i])
    return hit/N * volume










