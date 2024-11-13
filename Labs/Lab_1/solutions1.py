# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:47:04 2024

@author: domin
"""

import functions1 as f1

class solutions():
    
    def bisection_one(self):
        f=lambda x:x*x*x*x*x - 2* x*x*x*x -3*x*x*x +4*x*x+2*x;
        f1.plot(f,-10,10)
        e=float(input("Konvergenčni pogoj: "))
        cont="y";
        while cont=="y":
            a=float(input("prva meja: "))
            b= float(input("Druga meja: "))
            print(f1.bisection(f, a,b,e))
            cont=input("Continue, [y/n] ")
            
        #these are actual solutuions if you do not want to play around
        print(f"prva ničla: {f1.bisection(f,-2,-1.3):.4f}")
        print(f"druga ničla: {f1.bisection(f,-1,-0.3):.4f}")
        print(f"tretja ničla: {f1.bisection(f,-0.1,0.05):.4f}") 
        print(f"četrta ničla: {f1.bisection(f,0.3,1.5):.4f}")
        print(f"peta ničla: {f1.bisection(f,1.5,3):.4f}")
        
    def tangent_one(self):
        f=lambda x: -x*x*x + 4*x*x-2*x+2
        df = lambda x: -3*x*x +8*x -2
        
        f1.plot(f,-10,10)
        
        #print(f"{f1.tangent(f,df,0,1e-6):.4f}")
        #print(f"{f1.tangent(f,df,1.5,1e-6):.4f}") #both fail
        print(f"{f1.tangent(f,df,3,1e-6):.4f}")
        
    def tangent_two(self):
        f=lambda x: x*x*x - 3*x*x + 2*x
        df = lambda x: 3*x*x -6*x +2
     
        f1.plot(f,-10,10)
    
        print(f"{f1.tangent(f,df,1.447,1e-6):.4f}")
        print(f"{f1.tangent(f,df,1.4475,1e-6):.4f}")
        print(f"{f1.tangent(f,df,1.448,1e-6):.4f}")
        
    def task_one(self):
        f=lambda x: x*x*x -2 *x +2 
        
        f1.plot(f, -5, 5)
        cont="y";
        while cont=="y":
            a=float(input("prva meja: "))
            b= float(input("Druga meja: "))
            print(f"{f1.bisection(f,a,b,1e-6):.4f}")
            cont=input("Continue, [y/n] ")
            
        a1=-3;b1=-1.5;
        print(f"{f1.bisection(f,a1,b1,1e-6):.4f}")
        
    def task_two_a(self):
        f=lambda x: x*x*x +x*x -x-1 
        
        f1.plot(f, -5, 5)
        cont="y";
        while cont=="y":
            a=float(input("prva meja: "))
            b= float(input("Druga meja: "))
            print(f"{f1.bisection(f,a,b,1e-6):.4f}")
            cont=input("Continue, [y/n] ")
            
        a1=0.2;
        b1=2;
        print(f"{f1.bisection(f,a1,b1,1e-6):.4f}") #there is only one odd zero
        
    def task_two_b(self):
        f=lambda x: x*x*x+3*x*x+3*x+1
        
        f1.plot(f, -5, 5)
        cont="y";
        while cont=="y":
            a=float(input("prva meja: "))
            b= float(input("Druga meja: "))
            print(f"{f1.bisection(f,a,b,1e-6):.4f}")
            cont=input("Continue, [y/n] ")
            
        print(f"{f1.bisection(f,-1.5,0.55,1e-6):.4f}") 
        
    def task_two_c(self):
        f=lambda x:  x*x*x*x*x + 1.8 *x*x*x*x - 9*x*x*x - 9*x*x +23*x
        
        f1.plot(f, -5, 5)
        cont="y";
        while cont=="y":
            a=float(input("prva meja: "))
            b= float(input("Druga meja: "))
            print(f"{f1.bisection(f,a,b,1e-6):.4f}")
            cont=input("Continue, [y/n] ")
            
        print(f"{f1.bisection(f,-3.1,-2.6,1e-6):.4f}") 
        print(f"{f1.bisection(f,-2.6,-2,1e-6):.4f}") 
        print(f"{f1.bisection(f,-1.5,0.55,1e-6):.4f}") 
        print(f"{f1.bisection(f,1,1.55,1e-6):.4f}") 
        print(f"{f1.bisection(f,1.7,2.5,1e-6):.4f}")
        
    def task_three(self):
        import cmath
        f=lambda x: x*x*x - x*x +x -0.5;
        df=lambda x: 3*x*x -2*x +1
        f1.plot(f, -10, 10)
        
        #there is only real zero
        print(f"{f1.secant(f,0,2,1e-6):.4f}") 
        

        roots=f1.root_scan(f, df, -10, 10, 1)
        for r in roots:
            print(f"{r:.4f}")
         
    def task_four(self):
        """
        root(612)=?
        f=x*x-612
        """
        f=lambda x: x*x-612;
        df=lambda x: 2*x
        print(f"{f1.tangent(f,df, 25,1e-6):.4f}") 
        from math import sqrt
        print(f"{sqrt(612):.4f}") 
        
    
    def task_five(self):
        f=lambda x:x*x*x-2*x*x+2;
        df=lambda x: 3*x*x-2*x
        f1.plot(f, -1,1)
        #print(f"{tangent(f,0,1e-6):.4f}")
        #print(f"{tangent(f,1,1e-6):.4f}")
        """
        function gets stuck between two values for 0 and 1
        """
        print(f"{f1.tangent(f,df,0.5,1e-6):.4f}")
    
    def task_six(self):
        f=lambda x:x*x*x-2*x*x+2;

        f1.plot(f, -1,0)

        a=-1;
        b=0;
        print(f"{f1.secant(f,a,b,1e-6):.4f}")
        
        
        
        
        
        
        
        
        
        
        
        
